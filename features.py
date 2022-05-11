import numpy as np
import cv2
import math
import image_processing as ipr

class Feature(ipr.DataSet):
    def __init__(self,file_name):
        super().__init__(file_name)
        self.st_image = None
        self.baseline_angle = 0.0
        self.letter_size = 0.0
        self.top_margin = 0.0
        self.right_margin = 0.0
        self.slant_angle = 0.0

    ''' function for finding baseline angle using contours and straightening them horizontally '''
    def straighten(self):        
        angle = 0.0
        angle_sum = 0.0
        contour_count = 0

        positive_angle_sum = 0.0
        negative_angle_sum = 0.0
        positive_count = 0
        negative_count = 0

        self.st_image = self.image.copy()

        filtered = self.noiseRemoval(5)
        #cv2.imshow('filtered',filtered)
        
        thresh = self.inversion(180)
        #cv2.imshow('thresh',thresh)
        
        dilated = self.dilate((5 ,100))
        #cv2.imshow('dilated',dilated)
        
        ctrs,hier = cv2.findContours(self.pro_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #img2 = self.image.copy()
        #display = self.image.copy()
        #cv2.drawContours(img2, ctrs, -1, (0, 255, 0), 3)
        #cv2.imshow("Contours",img2)
        
        for i, ctr in enumerate(ctrs):
            x, y, w, h = cv2.boundingRect(ctr)
            #print("(",x,",",y,"):",w,h)
            
            # We can be sure the contour is not a line if height > width or height is < 20 pixels. Here 20 is arbitrary.
            if h>w or h<20:
                continue
                
            # We extract the region of interest/contour to be straightened.
            roi = self.st_image[y:y+h, x:x+w]
            
            # If the length of the line is less than one third of the document width, especially for the last line,
            # ignore because it may yeild inacurate baseline angle which subsequently affects proceeding features.
            if w < self.st_image.shape[1]/2 :
                roi = 255
                self.st_image[y:y+h, x:x+w] = roi
                continue
                
            # minAreaRect is necessary for straightening
            rect = cv2.minAreaRect(ctr)
            center = rect[0]
            angle = rect[2]
            #print("original: "+str(i)+" "+str(angle))

            # anti-clockwise point distribution starting from 0 as lowest value of y
            # so angle (0,45] is asc baseline and (45,90] is decs baseline
            if angle > 45.0:
                angle -= 90.0
                #print("-90 "+str(i)+" "+str(angle))
            
            rot = cv2.getRotationMatrix2D(center, angle, 1)
            #extract = cv2.warpAffine(roi, rot, (w,h))
            #extract = cv2.warpAffine(roi, rot, (w,h), borderMode=cv2.BORDER_TRANSPARENT)
            extract = cv2.warpAffine(roi, rot, (w,h), borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255))
            
            # image is overwritten with the straightened contour
            self.st_image[y:y+h, x:x+w] = extract
            
            '''
            # Please Ignore. This is to draw visual representation of the contour rotation.
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(display,[box],-1,(0,255,0),3)
            cv2.rectangle(display,(x,y),( x + w, y + h ),(0,255,0),1)
            cv2.imshow('rotatn',display)
            '''

            angle_sum += angle
            contour_count += 1
            
            # sum of all the angles of asc baseline
            if(angle>0.0):
                positive_angle_sum += angle
                positive_count += 1
            # sum of all the angles of desc baseline
            else:
                negative_angle_sum += angle
                negative_count += 1
        
        # avg angle of the contours
        if(positive_count == 0): positive_count = 1
        if(negative_count == 0): negative_count = 1
        average_positive_angle = positive_angle_sum / positive_count
        average_negative_angle = negative_angle_sum / negative_count
        average_angle = average_positive_angle + average_negative_angle
        #print("positive_angle_sum & count:"+str(positive_angle_sum)+" "+str(positive_count))
        #print("positive_angle_sum & count:"+str(negative_angle_sum)+" "+str(negative_count))
        #print("average_positive_angle: "+str(average_positive_angle))
        #print("average_negative_angle: "+str(average_negative_angle))
        #print("average_angle: "+str(average_angle))

        # mean angle of the contours
        if(contour_count == 0): contour_count = 1
        mean_angle = angle_sum / contour_count
        #print("angle_sum & count:"+str(angle_sum)+" "+str(contour_count))
        #print("mean_angle: "+str(mean_angle))

        self.baseline_angle = round(mean_angle,2)
        return self.st_image

    ''' function for finding the size of letter '''
    def letterSize(self):
        MIDZONE_THRESHOLD = 10000
        # Each line is extracted first for LETTER SIZE and TOP MARGIN
        self.LineSegmentation(self.st_image)
        
        # LETTER SIZE will be extracted here
        # We will count the total number of pixel rows containing upper and lower zones of the lines and add the space_zero/runs of 0's(excluding first and last of the list ) to it.
        # We will count the total number of pixel rows containing midzones of the lines for letter size.
        # For this, we set an arbitrary (yet suitable!) threshold MIDZONE_THRESHOLD = 15000 in horizontal projection to identify the midzone containing rows.
        # These two total numbers will be divided by number of lines (having at least one row>MIDZONE_THRESHOLD) to find average line spacing and average letter size.
        midzone_row_count = 0
        lines_having_midzone_count = 0
        flag = False
        for i, line in enumerate(self.Lines):
            segment = self.hpList[int(line[0]):int(line[1])]
            for j, sum in enumerate(segment):
                if(sum>=MIDZONE_THRESHOLD):
                    midzone_row_count += 1
                    flag = True
                    
            # This line has contributed at least one count of pixel row of midzone
            if flag:
                lines_having_midzone_count += 1
                flag = False
        
        # error prevention ^-^
        if lines_having_midzone_count == 0 : lines_having_midzone_count = 1
        
        # letter size is actually height of the letter and we are not considering width
        self.letter_size = round(float(midzone_row_count) / lines_having_midzone_count,2)
        # error prevention ^-^
        if(self.letter_size == 0): self.letter_size = 1.0
        #print(self.letter_size)
        return

    ''' function to calculate top and right margin '''
    def marginFeature(self):
        # calculating TOP MARGIN
        tm_count = 0
        for sum in self.hpList:
            if sum <= 255:
                tm_count += 1
            else:
                break
        
        self.top_margin = round(float(tm_count)/self.letter_size,2)
        #print ("(Top margin row count: "+str(tm_count)+")= "+str(self.right_margin))

        # calculating RIGHT MARGIN
        width = self.pro_image.shape[1] # Width of the whole document
        rm_count = 0
        row_count = 0
        for line in self.Lines:
            extract = self.pro_image[int(line[0]):int(line[1]), 0:width] # y1:y2, x1:x2
            vp = self.verticalProjection(extract)
            row_count += 1
            #print (vp)
            # we are scanning the vertical projection in reverse for blank space 
            for sum in vp[::-1]:
                if sum<=255:
                    rm_count += 1
                else:
                    break
        
        self.right_margin = round(float(rm_count)/(row_count * self.letter_size),2)
        #print ("(Right margin row count: "+str(rm_count/row_count)+")= "+str(self.right_margin))
        return

    ''' function to determine the average slant of the handwriting '''
    def extractSlant(self):
        # First we will extraxt words
        self.WordSegmentation(self.st_image)
        '''
        0.01 radian = 0.5729578 degree :: I had to put this instead of 0.0 becuase float comparission for 0 is ambigues in IEEE 754!
        5 degree = 0.0872665 radian :: Hardly noticeable or a very little slant
        15 degree = 0.261799 radian :: Easily noticeable or average slant
        30 degree = 0.523599 radian :: Above average slant
        45 degree = 0.785398 radian :: Extreme slant
        '''
        # We are checking for 9 different values of angle
        theta = [-0.785398, -0.523599, -0.261799, -0.0872665, 0.01, 0.0872665, 0.261799, 0.523599, 0.785398]
        #theta = [-0.785398, -0.523599, -0.436332, -0.349066, -0.261799, -0.174533, -0.0872665, 0, 0.0872665, 0.174533, 0.261799, 0.349066, 0.436332, 0.523599, 0.785398]

        # Corresponding index of the biggest value will be the index of the most likely angle in 'theta'
        s_function = [0.0] * 9
        count_ = [0]*9
        
        # loop for each value of angle in theta
        for i, angle in enumerate(theta):
            s_temp = 0.0 # overall sum of the functions of all the columns of all the words!
            count = 0 # just counting the number of columns considered to contain a vertical stroke and thus contributing to s_temp
            
            #loop for each word
            for j, word in enumerate(self.Words):
                original = self.pro_image[int(word[0]):int(word[1]), int(word[2]):int(word[3])] # y1:y2, x1:x2

                height = int(word[1])-int(word[0])
                width = int(word[3])- int(word[2])
                
                # the distance in pixel we will shift for affine transformation
                # it's divided by 2 because the uppermost point and the lowermost points are being equally shifted in opposite directions
                shift = (math.tan(angle) * height) / 2
                
                # the amount of extra space we need to add to the original image to preserve information
                pad_length = abs(int(shift))
                
                # create a new image that can perfectly hold the transformed and thus widened image
                blank_image = np.zeros((height,width+pad_length*2,3), np.uint8)
                new_image = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
                new_image[:, pad_length:width+pad_length] = original
                
                # points to consider for affine transformation
                (height, width) = new_image.shape[:2]
                x1 = width/2
                y1 = 0
                x2 = width/4
                y2 = height
                x3 = 3*width/4
                y3 = height
        
                pts1 = np.float32([[x1,y1],[x2,y2],[x3,y3]])
                pts2 = np.float32([[x1+shift,y1],[x2-shift,y2],[x3-shift,y3]])
                M = cv2.getAffineTransform(pts1,pts2)
                deslanted = cv2.warpAffine(new_image,M,(width,height))
                
                # find the vertical projection on the transformed image
                vp = self.verticalProjection(deslanted)
                
                # loop for each value of vertical projection, which is for each column in the word image
                for k, sum in enumerate(vp):
                    # the columns is empty
                    if(sum == 0):
                        continue
                    
                    # this is the number of foreground pixels in the column being considered
                    num_fgpixel = sum / 255

                    # if number of foreground pixels is less than onethird of total pixels, it is not a vertical stroke so we can ignore
                    if(num_fgpixel < int(height/3)):
                        continue
                    
                    # the column itself is extracted, and flattened for easy operation
                    column = deslanted[0:height, k:k+1]
                    column = column.flatten()
                    
                    # now we are going to find the distance between topmost pixel and bottom-most pixel
                    # l counts the number of empty pixels from top until and upto a foreground pixel is discovered
                    for l, pixel in enumerate(column):
                        if(pixel==0):
                            continue
                        break
                    # m counts the number of empty pixels from bottom until and upto a foreground pixel is discovered
                    for m, pixel in enumerate(column[::-1]):
                        if(pixel==0):
                            continue
                        break
                    
                    # the distance is found as delta_y
                    delta_y = height - (l+m)
                
                    # checking for the lines which contribute totaly in the column
                    h_sq = (float(num_fgpixel)/delta_y)**2
                    
                    # multiplying by a factor of num_fgpixel/height to the above function to yeild better result
                    h_wted = (h_sq * num_fgpixel) / height

                    '''
                    # just printing
                    if(j==0):
                        print (column)
                        print (str(i)+' h_sq='+str(h_sq)+' h_wted='+str(h_wted)+' num_fgpixel='+str(num_fgpixel)+' delta_y='+str(delta_y))
                    '''
                    
                    # add up the values from all the loops of ALL the columns of ALL the words in the image
                    s_temp += h_wted
                    
                    count += 1
                
                '''
                if(j==0):
                    cv2.imshow('Output '+str(i)+str(j), deslanted) 
                '''
                     
            s_function[i] = s_temp
            count_[i] = count
        
        # finding the largest value and corresponding index
        max_value = 0.0
        max_index = 4
        for index, value in enumerate(s_function):
            #print (str(index)+" "+str(value)+" "+str(count_[index]))
            if(value > max_value):
                max_value = value
                max_index = index
                
        # We will add another value 9 manually to indicate irregular slant behaviour.
        # This will be seen as value 4 (no slant) but 2 corresponding angles of opposite sign will have very close values.
        if(max_index == 0):
            angle = 45
            result =  " : Extremely right slanted"
        elif(max_index == 1):
            angle = 30
            result = " : Above average right slanted"
        elif(max_index == 2):
            angle = 15
            result = " : Average right slanted"
        elif(max_index == 3):
            angle = 5
            result = " : A little right slanted"
        elif(max_index == 5):
            angle = -5
            result = " : A little left slanted"
        elif(max_index == 6):
            angle = -15
            result = " : Average left slanted"
        elif(max_index == 7):
            angle = -30
            result = " : Above average left slanted"
        elif(max_index == 8):
            angle = -45
            result = " : Extremely left slanted"
        elif(max_index == 4):
            p = s_function[4] / s_function[3]
            q = s_function[4] / s_function[5]
            #print ('p='+str(p)+' q='+str(q))
            # the constants here are abritrary but suits the best
            if((p <= 1.2 and q <= 1.2) or (p > 1.4 and q > 1.4)):
                angle = 0
                result = " : No slant"
            elif((p <= 1.2 and q-p > 0.4) or (q <= 1.2 and p-q > 0.4)):
                angle = 0
                result = " : No slant"
            else:
                max_index = 9
                angle = 180
                result =  " : Irregular slant behaviour"

        self.slant_angle = round(angle,2)
        #print ("Slant angle(degree): "+str(self.slant_angle)+result)
        return

class Categorize(Feature):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.category = []
    
    def determine_baseline_angle(self):
        comment = ""
        # rising
        if(self.baseline_angle >= 0.2):
            cat = 1
            comment = "ASCENDING"
        # falling
        elif(self.baseline_angle <= -0.3):
            cat = 2
            comment = "DESCENDING"
        # straight
        else:
            cat = 0
            comment = "STRAIGHT"
        
        self.category.append([cat,comment])
        return
    
    def determine_letter_size(self):
        comment = ""
        # large
        if(self.letter_size >= 18.0):
            cat = 3
            comment = "BIG"
        # medium
        elif(self.letter_size >= 14.0):
            cat = 2
            comment = "Medium"
        # small
        elif(self.letter_size >= 12.0):
            cat = 1
            comment = "SMALL"
        # very small
        else:
            cat = 0
            comment = "MICROSCOPIC"
        
        self.category.append([cat,comment])
        return
    
    def determine_top_margin(self):
        comment = ""
        # exaggerated
        if(self.top_margin >= 5.5):
            cat = 3
            comment = "EXAGGERATED"
        # big
        if(self.top_margin < 5.5 and self.top_margin >= 3.0):
            cat = 2
            comment = "BIG"
        # normal
        elif(self.top_margin < 3.0 and self.top_margin >= 1.7):
            cat = 1
            comment = "MEDIUM"
        # narrow
        else:
            cat = 0
            comment = "NARROW"
        
        self.category.append([cat,comment])
        return 
    
    def determine_right_margin(self):
        comment = ""
        bigger = 150/self.letter_size
        big = 90/self.letter_size
        avg = 50/self.letter_size
        # exaggerated
        if(self.right_margin >= bigger):
            cat = 3
            comment = "EXAGGERATED"
        # big
        elif(self.right_margin < bigger and self.right_margin >= big):
            cat = 2
            comment = "BIG"
        # normal
        elif(self.right_margin < big and self.right_margin >= avg):
            cat = 1
            comment = "MEDIUM"
        # narrow
        else:
            cat = 0
            comment = "SMALL OR ABSENT"
        
        self.category.append([cat,comment])
        return 
    
    def determine_slant_angle(self):
        comment = ""
        # extremely reclined
        if(self.slant_angle == -45.0 or self.slant_angle == -30.0):
            cat = 0
            comment = "EXTREMELY RECLINED"
        # a little reclined or moderately reclined
        elif(self.slant_angle == -15.0 or self.slant_angle == -5.0 ):
            cat = 1
            comment = "A LITTLE OR MODERATELY RECLINED"
        # a little inclined
        elif(self.slant_angle == 5.0 or self.slant_angle == 15.0 ):
            cat = 3
            comment = "A LITTLE INCLINED"
        # moderately inclined
        elif(self.slant_angle == 30.0 ):
            cat = 4
            comment = "MODERATELY INCLINED"
        # extremely inclined
        elif(self.slant_angle == 45.0 ):
            cat = 5
            comment = "EXTREMELY INCLINED"
        # straight
        elif(self.slant_angle == 0.0 ):
            cat = 2
            comment = "STRAIGHT"
        # irregular
        #elif(self.slant_angle == 180 ):
        else:
            cat = 6
            comment = "IRREGULAR"
        
        self.category.append([cat,comment])
        return 

def extract(file_name):
    f1 = Categorize(file_name)

    f1.straighten()
    f1.determine_baseline_angle()
    f1.letterSize()
    f1.determine_letter_size()
    f1.marginFeature()
    f1.determine_top_margin()
    f1.determine_right_margin()
    f1.extractSlant()
    f1.determine_slant_angle()

    return [f1.baseline_angle, f1.letter_size, f1.top_margin, f1.right_margin, f1.slant_angle], f1.category

if __name__=="__main__":
    #file_name= 'a02-078.png'
    file_name= 'a01-053.png'

    f1 = Categorize(file_name)

    img = f1.straighten()
    #cv2.imshow('straighten',img)

    # Raw features of image
    f1.letterSize()
    f1.marginFeature()
    f1.extractSlant()

    # classified features of image
    f1.determine_baseline_angle()
    f1.determine_letter_size()
    f1.determine_top_margin()
    f1.determine_right_margin()
    f1.determine_slant_angle()

    # Word extracted by spacing, not considering single character word or smaller
    '''
    print ("Total words:",len(f1.Words))
    for i, word in enumerate(f1.Words):
        cv2.imshow("Word "+str(i+1), f1.st_image[int(word[0]):int(word[1]), int(word[2]):int(word[3])])
    '''

    print([f1.baseline_angle, f1.letter_size, f1.top_margin, f1.right_margin, f1.slant_angle])
    print(f1.category)

    cv2.waitKey(0)
    cv2.destroyAllWindows()