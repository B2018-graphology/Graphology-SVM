import numpy as np
import cv2

class DataSet:
    def __init__(self,file_name):
        self.file_name = file_name
        self.image = cv2.imread('images/'+self.file_name)
        self.pro_image = self.image.copy()
        self.hpList = []
        self.Lines = []
        self.Words = []

    # function for bilateral filtering
    def noiseRemoval(self, d, img=None):
        if img is None: img = self.image 
        self.pro_image = cv2.bilateralFilter(img,d,50,50)
        return self.pro_image

    # function for INVERTED binary threshold
    # convert to grayscale and binarize the image by INVERTED binary thresholding
    def inversion(self, t):
        self.pro_image = cv2.cvtColor(self.pro_image, cv2.COLOR_BGR2GRAY)
        ret,self.pro_image = cv2.threshold( self.pro_image,t,255,cv2.THRESH_BINARY_INV)
        return self.pro_image

    # function for dilation of objects in the image
    # dilate the handwritten lines in image with a suitable kernel for contour operation
    def dilate(self, kernalSize):
        kernel = np.ones(kernalSize, np.uint8)
        self.pro_image = cv2.dilate(self.pro_image, kernel, iterations=1)
        return self.pro_image

    ''' function to calculate horizontal projection of the image pixel rows and return it '''
    def horizontalProjection(self, img):
        # Return a list containing the sum of the pixels in each row
        (h, w) = img.shape[:2]
        sumRows = []
        for j in range(h):
            row = img[j:j+1, 0:w] # y1:y2, x1:x2
            sumRows.append(np.sum(row))
        return sumRows
    
    ''' function to calculate vertical projection of the image pixel columns and return it '''
    def verticalProjection(self, img):
        # Return a list containing the sum of the pixels in each column
        (h, w) = img.shape[:2]
        sumCols = []
        for j in range(w):
            col = img[0:h, j:j+1] # y1:y2, x1:x2
            sumCols.append(np.sum(col))
        return sumCols

    ''' function to extract lines of handwritten text from the image using horizontal projection '''
    def LineSegmentation(self, img):
        ANCHOR_POINT = 6000
        # apply bilateral filter
        filtered = self.noiseRemoval(5, img)
        
        # convert to grayscale and binarize the image by INVERTED binary thresholding
        # it's better to clear unwanted dark areas at the document left edge and use a high threshold value to preserve more text pixels
        thresh = self.inversion(160)
        #cv2.imshow('thresh', lthresh)

        # extract a python list containing values of the horizontal projection of the image into 'hp'
        self.hpList = self.horizontalProjection(thresh)
        
        # FIRST we extract the straightened contours from the image by looking at occurance of 0's in the horizontal projection.
        lineTop = 0
        lineBottom = 0
        indexCount = 0
        setLineTop = True
        lines = [] # a 2D list storing the vertical start index and end index of each contour
        
        # we are scanning the whole horizontal projection now
        for i, sum in enumerate(self.hpList):
            # sum being 0 means blank space
            if sum==0:
                indexCount += 1
            # sum greater than 0 means contour
            if sum>0:
                if(setLineTop):
                    lineTop = indexCount
                    setLineTop = False # lineTop will be set once for each start of a new line/contour
                indexCount += 1
                lineBottom = indexCount
                if(i<len(self.hpList)-1): # this condition is necessary to avoid array index out of bound error
                    if(self.hpList[i+1]>0): # if the next horizontal projectin is > 0, keep on counting, it's still in contour
                        continue
                        
                    # if the line/contour is too thin <10 pixels (arbitrary) in height, we ignore it.
                    # Also, we add the space following this and this contour itself to the previous space to form a bigger space: spaceBottom-lineTop.
                    if(lineBottom-lineTop<20):
                        setLineTop = True # next time we encounter value > 0, it's begining of another line/contour so we set new lineTop
                        continue
                
                # append the top and bottom horizontal indices of the line/contour in 'lines'
                lines.append([lineTop, lineBottom])
                setLineTop = True # next time we encounter value > 0, it's begining of another line/contour so we set new lineTop
        
        '''
        # Printing the values we found so far.
        for i, line in enumerate(lines):
            print()
            print (i)
            print (line[0], line[1], len(self.hpList[line[0]:line[1]]))
            print (self.hpList[line[0]:line[1]])
        for i, line in enumerate(lines):
            cv2.imshow("line "+str(i), img[line[0]:line[1], : ])
        '''
        
        # SECOND we extract the very individual lines from the lines/contours we extracted above.
        fineLines = [] # a 2D list storing the horizontal start index and end index of each individual line
        for i, line in enumerate(lines):
            anchor = line[0] # 'anchor' will locate the horizontal indices where horizontal projection is > ANCHOR_POINT for uphill or < ANCHOR_POINT for downhill(ANCHOR_POINT is arbitrary yet suitable!)
            anchorPoints = [] # python list where the indices obtained by 'anchor' will be stored
            upHill = True # it implies that we expect to find the start of an individual line (vertically), climbing up the histogram
            downHill = False # it implies that we expect to find the end of an individual line (vertically), climbing down the histogram
            segment = self.hpList[line[0]:line[1]] # we put the region of interest of the horizontal projection of each contour here
            
            for j, sum in enumerate(segment):
                if(upHill):
                    if(sum<ANCHOR_POINT):
                        anchor += 1
                        continue
                    anchorPoints.append(anchor)
                    upHill = False
                    downHill = True
                if(downHill):
                    if(sum>ANCHOR_POINT):
                        anchor += 1
                        continue
                    anchorPoints.append(anchor)
                    downHill = False
                    upHill = True
                    
            #print (anchorPoints)
            
            # we can ignore the contour here
            if(len(anchorPoints)<2):
                continue
            
            # len(anchorPoints) > 3 meaning contour composed of multiple lines
            lineTop = line[0]
            for x in range(1, len(anchorPoints)-1, 2):
                # 'lineMid' is the horizontal index where the segmentation will be done
                lineMid = (anchorPoints[x]+anchorPoints[x+1])/2
                lineBottom = lineMid
                # line having height of pixels <20 is considered defects, so we just ignore it
                # this is a weakness of the algorithm to extract lines (anchor value is ANCHOR_POINT, see for different values!)
                if(lineBottom-lineTop < 20):
                    continue
                fineLines.append([lineTop, lineBottom])
                lineTop = lineBottom
            if(line[1]-lineTop < 20):
                continue
            fineLines.append([lineTop, line[1]])    
        
        '''
        # showing the final extracted lines
        for i, line in enumerate(fineLines):
            cv2.imshow("fineLine "+str(i), img[int(line[0]):int(line[1]), : ])
        print (lines)
        print (fineLines)
        '''

        self.Lines = fineLines
        return lines

    ''' function to extract words from the lines using vertical projection '''
    def WordSegmentation(self, img):
        # apply bilateral filter
        filtered = self.noiseRemoval(5, img)
        
        # convert to grayscale and binarize the image by INVERTED binary thresholding
        thresh = self.inversion(180)
        #cv2.imshow('thresh', lthresh)

        width = thresh.shape[1] # Width of the whole document
        words = [] # a 2D list storing the coordinates of each word: y1, y2, x1, x2

        # Isolated words or components will be extacted from each line by looking at occurance of 0's in its vertical projection.
        for i, line in enumerate(self.Lines):
            extract = self.pro_image[int(line[0]):int(line[1]), 0:width] # y1:y2, x1:x2
            vp = self.verticalProjection(extract)
            #print (i)
            #print (vp)

            wordStart = 0
            wordEnd = 0
            indexCount = 0
            setWordStart = True
            
            # we are scanning the vertical projection
            for j, sum in enumerate(vp):
                # sum being 0 means blank space
                if(sum==0):
                    indexCount += 1
                    
                # sum greater than 0 means word/component
                if(sum>0):
                    if(setWordStart):
                        wordStart = indexCount
                        setWordStart = False # wordStart will be set once for each start of a new word/component
                    indexCount += 1
                    wordEnd = indexCount
                    if(j<len(vp)-1): # this condition is necessary to avoid array index out of bound error
                        if(vp[j+1]>0): # if the next horizontal projectin is > 0, keep on counting, it's still in non-space zone
                            continue
                    
                    # append the coordinates of each word/component: y1, y2, x1, x2 in 'words'
                    # we ignore the ones which has height smaller than half the average letter size
                    # this will remove full stops and commas as an individual component
                    count = 0
                    for k in range(int(line[1])-int(line[0])):
                        row = self.pro_image[int(line[0]+k):int(line[0]+k+1), wordStart:wordEnd] # y1:y2, x1:x2
                        if(np.sum(row)):
                            count += 1
                    try:
                        if(count > int(self.letter_size/2)):
                            words.append([line[0], line[1], wordStart, wordEnd])
                    except:
                        words.append([line[0], line[1], wordStart, wordEnd])
                        
                    setWordStart = True # next time we encounter value > 0, it's begining of another word/component so we set new wordStart
        
        self.Words = words

if __name__=="__main__":
    #file_name= 'a01-011x.png'
    #file_name= 'a01-043.png'
    #file_name= 'a01-058.png'
    #file_name= 'a01-063.png'
    #file_name= 'a01-063x.png'
    #file_name= 'a02-078.png'
    file_name= 'a03-020.png'

    img1 = DataSet(file_name)

    contour = img1.LineSegmentation(img1.image)
    # Printing Contours formed by overlapped lines
    print ("Total contours:",len(contour))
    for i, line in enumerate(contour):
        cv2.imshow("Contour "+str(i+1), img1.image[int(line[0]):int(line[1]), : ])

    # Final lines found after calculating through threshold pixel 
    print ("Total lines:",len(img1.Lines))
    for i, line in enumerate(img1.Lines):
        cv2.imshow("Line "+str(i+1), img1.image[int(line[0]):int(line[1]), : ])

    # Word extracted by spacing
    img1.WordSegmentation(img1.image)
    print ("Total words:",len(img1.Words))
    for i, word in enumerate(img1.Words):
        cv2.imshow("Word "+str(i+1), img1.image[int(word[0]):int(word[1]), int(word[2]):int(word[3])])

    '''
    ctrs,hier = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(ctrs),hier)
    print(enumerate(ctrs))
    cv2.drawContours(image, ctrs, -1, (0, 255, 0), 3)
    cv2.imshow("Contours",image)
    '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()