import os 
import features

class Labelling:
    def __init__(self, fList):
        self.fList = fList
        self.labelDict = {"Optimism":0 , "Pecimism":0 , "Depression":0 , "Joy":0 , "Fear":0 , "Goal Oriented":0 , "Self Esteem":0 , "Others Value":0 , "Observant":0 , "Vision":0 , "Self Confidence":0 , "Extrovert":0 , "Introvert":0 , "Generous":0 , "Selfish":0 , "Polite":0 , "Management":0 , "Honesty":0 , "Emotional":0 , "Practical":0 , "Adjustment":0 , "Concentration":0 , "Imagination":0 , "Conservative":0 , "Dependent":0 , "Self Control":0 , "Trust":0 , "Talkative":0 , "Relate":0 , "Stable":0 , "Expressive":0 , "Perfectionist":0 , "Initiation":0 , "Listner":0}
    
    def giveLabel(self):
        # for baseline
        if self.fList[0]==0:
            self.labelDict["Goal Oriented"] += 1
        elif self.fList[0]==1:
            self.labelDict["Optimism"] += 1
            self.labelDict["Joy"] += 1
        elif self.fList[0]==2:
            self.labelDict["Pecimism"] += 1
            self.labelDict["Depression"] += 1

        # for letter size
        if self.fList[1]==0:
            self.labelDict["Fear"] += 1
            self.labelDict["Observant"] += 1
            self.labelDict["Vision"] -= 1
            self.labelDict["Management"] -= 1
            self.labelDict["Concentration"] += 1
            self.labelDict["Imagination"] += 1
            self.labelDict["Conservative"] += 1
            self.labelDict["Perfectionist"] += 1
        elif self.fList[1]==1:
            self.labelDict["Pecimism"] += 1
            self.labelDict["Fear"] += 1
            self.labelDict["Observant"] += 1
            self.labelDict["Vision"] -= 1
            self.labelDict["Introvert"] += 1
            self.labelDict["Generous"] -= 1
            self.labelDict["Practical"] += 1
            self.labelDict["Adjustment"] -= 1
            self.labelDict["Concentration"] += 2
        elif self.fList[1]==2:
            self.labelDict["Observant"] += 1
            self.labelDict["Vision"] += 1
            self.labelDict["Self Confidence"] += 1
            self.labelDict["Extrovert"] += 1
            self.labelDict["Emotional"] += 1
            self.labelDict["Adjustment"] += 1
        elif self.fList[1]==3:
            self.labelDict["Optimism"] += 1
            self.labelDict["Self Esteem"] += 2
            self.labelDict["Others Value"] -= 2
            self.labelDict["Observant"] -= 1
            self.labelDict["Vision"] += 1
            self.labelDict["Self Confidence"] += 1
            self.labelDict["Extrovert"] += 1
            self.labelDict["Generous"] += 1
            self.labelDict["Polite"] -= 2
            self.labelDict["Management"] += 1

        # for top margin
        if self.fList[2]==0:
            self.labelDict["Extrovert"] += 1
            self.labelDict["Selfish"] += 1
            self.labelDict["Polite"] -= 1
            self.labelDict["Dependent"] += 1
            self.labelDict["Trust"] += 2
        elif self.fList[2]==1:
            self.labelDict["Generous"] += 1
            self.labelDict["Polite"] += 1
            self.labelDict["Self Control"] += 1
        elif self.fList[2]==2:
            self.labelDict["Introvert"] += 1
            self.labelDict["Adjustment"] -= 1
            self.labelDict["Listner"] += 1
        elif self.fList[2]==3:
            self.labelDict["Self Esteem"] += 1
            self.labelDict["Selfish"] += 1
            self.labelDict["Management"] -= 1

        # for right margin
        if self.fList[3]==0:
            self.labelDict["Others Value"] += 1
            self.labelDict["Extrovert"] += 1
            self.labelDict["Generous"] += 1
            self.labelDict["Concentration"] -= 1
            self.labelDict["Imagination"] -= 1
            self.labelDict["Initiation"] += 1
        elif self.fList[3]==1:
            self.labelDict["Optimism"] += 1
            self.labelDict["Honesty"] += 1
            self.labelDict["Self Control"] += 1
            self.labelDict["Relate"] -= 1
        elif self.fList[3]==2:
            self.labelDict["Pecimism"] += 1
            self.labelDict["Depression"] += 1
            self.labelDict["Fear"] += 1
            self.labelDict["Introvert"] += 1
            self.labelDict["Trust"] -= 1
        elif self.fList[3]==3:
            self.labelDict["Fear"] += 1
            self.labelDict["Introvert"] += 1
            self.labelDict["Practical"] -= 1
            self.labelDict["Trust"] -= 1

        # for letter slant
        if self.fList[4]==0:
            self.labelDict["Depression"] += 1
            self.labelDict["Self Esteem"] += 1
            self.labelDict["Introvert"] += 2
            self.labelDict["Honesty"] -= 1
            self.labelDict["Emotional"] -= 1
            self.labelDict["Adjustment"] -= 1
            self.labelDict["Conservative"] += 1
            self.labelDict["Dependent"] += 1
            self.labelDict["Talkative"] -= 1
            self.labelDict["Stable"] -= 1
            self.labelDict["Expressive"] -= 1
        elif self.fList[4]==1:
            self.labelDict["Fear"] += 1
            self.labelDict["Self Confidence"] -= 1
            self.labelDict["Introvert"] += 1
            self.labelDict["Honesty"] -= 1
            self.labelDict["Practical"] -= 1
            self.labelDict["Conservative"] += 1
            self.labelDict["Dependent"] += 1
            self.labelDict["Trust"] -= 1
            self.labelDict["Expressive"] -= 1
            self.labelDict["Perfectionist"] -= 1
        elif self.fList[4]==2:
            self.labelDict["Joy"] += 1
            self.labelDict["Self Esteem"] += 1
            self.labelDict["Observant"] += 1
            self.labelDict["Self Confidence"] += 1
            self.labelDict["Emotional"] += 1
            self.labelDict["Concentration"] += 1
            self.labelDict["Imagination"] += 1
            self.labelDict["Self Control"] += 1
            self.labelDict["Stable"] += 1
            self.labelDict["Perfectionist"] += 1
            self.labelDict["Dependent"] -= 2
        elif self.fList[4]==3:
            self.labelDict["Observant"] += 1
            self.labelDict["Polite"] += 1
            self.labelDict["Honesty"] += 1
            self.labelDict["Practical"] += 1
            self.labelDict["Adjustment"] += 1
        elif self.fList[4]==4:
            self.labelDict["Extrovert"] += 2
            self.labelDict["Emotional"] += 1
            self.labelDict["Concentration"] += 1
            self.labelDict["Imagination"] += 1
            self.labelDict["Dependent"] += 1
            self.labelDict["Stable"] -= 1
        elif self.fList[4]==5:
            self.labelDict["Goal Oriented"] -= 1
            self.labelDict["Self Confidence"] -= 1
            self.labelDict["Extrovert"] += 2
            self.labelDict["Polite"] -= 1
            self.labelDict["Dependent"] += 1
            self.labelDict["Self Control"] -= 1
            self.labelDict["Talkative"] += 1
            self.labelDict["Stable"] -= 1
            self.labelDict["Perfectionist"] += 1
            self.labelDict["Initiation"] += 1
        elif self.fList[4]==6:
            self.labelDict["Depression"] += 1
            self.labelDict["Fear"] += 1
            self.labelDict["Emotional"] -= 1
            self.labelDict["Practical"] -= 1
            self.labelDict["Adjustment"] += 1
            self.labelDict["Concentration"] -= 1
            self.labelDict["Self Control"] -= 1
            self.labelDict["Stable"] -= 1

        return list(self.labelDict.values())

os.chdir("images")
files = [f for f in os.listdir('.') if os.path.isfile(f)]
os.chdir("..")

def generate_feature_list():
	page_ids = []
	if os.path.isfile("raw_feature_list"):
		print ("Info: raw_feature_list already exists.")
		with open("raw_feature_list", "r") as label:
			for line in label:
				content = line.split()
				page_id = content[-1]
				page_ids.append(page_id)
			
	with open("raw_feature_list", "a") as raw_label, open("feature_list", "a") as label:
		count = len(page_ids)
		for fname in files:
			if(fname in page_ids):
				continue
			raw_features, category = features.extract(fname)
			raw_features.append(fname)
			category.append([fname])
			#print(raw_features)
			#print(category)
			for i in raw_features:
				raw_label.write("%s\t" % i)
			raw_label.write("\n")
			for i in category:
				label.write("%s\t" % i[0])
			label.write("\n")
			count += 1
			progress = (count*100)/len(files)
			print(str(count)+' '+fname+' '+str(round(progress,2))+'%')
		print("Done!")

present, new = False, False
# Now finding traits corresponding to features
if os.path.isfile("label_list"):
	print ("Error: label_list already exists.")
	present = True
elif not os.path.isfile("feature_list"):
	print ("Info: genetaring feature_list")
	generate_feature_list()
	
if os.path.isfile("feature_list"):
	with open("feature_list", "r") as categories:
		if len(list(categories)) < len(files):
			print ("Info: appending to feature_list")
			generate_feature_list()
			new = True
	
	if new or not present:
		print ("Info: feature_list found")
		with open("feature_list", "r") as categories, open("label_list", "w") as labels:
			for line in categories:
				temp = line.split()
				category = list(map(int, temp[:-1]))
				temp = temp[-1] # storing page_id
				l1 = Labelling(category)
				traits = l1.giveLabel()
				#print(traits)
				for x in category:
					labels.write("%s \t" % float(x))
				for x in traits:
					labels.write("%s \t" % x)
				labels.write("%s \n" % temp)
		print ("Done!")

