import os 
import features

class Labelling:
	def __init__(self, fList):
		self.fList = fList
		self.labelList = [-1,-1,-1,-1,-1]

	def determineOpenness(self):
		# trait_1 = Right Margin & Slant | 1 = High, 0 = Low
		if (self.fList[4] == 2 or self.fList[3] == 0):
			self.labelList[0] = 0
		elif (self.fList[3] == 1):
			self.labelList[0] = 1
		
	def determineConscientiousness(self):
		# trait_2 = Letter Size, Top Margin & Slant | 2 = high, 1 = average, 0 = low
		if (self.fList[1] in [0,1] or self.fList[2] == 1 or self.fList[4] == 2):
			self.labelList[1] = 2
		elif (self.fList[1] == 2 or self.fList[4] == 4):
			self.labelList[1] = 1
		elif (self.fList[2] == 3 or self.fList[4] == 6):
			self.labelList[1] = 0
		
	def determineExtroversion(self):
		# trait_3 = Letter Size, Top Margin, Right Margin & Slant | 2 = high, 1 = average, 0 = low
		if (self.fList[1] == 3 or self.fList[2] == 0 or self.fList[3] == 0 or self.fList[4] in [5,4,3]):
			self.labelList[2] = 2
		elif (self.fList[1] == 2 or self.fList[2] == 2 or self.fList[4] == 2):
			self.labelList[2] = 1
		elif (self.fList[1] in [0,1] or self.fList[2] == 3 or self.fList[3] in [2,3] or self.fList[4] in [0,1]):
			self.labelList[2] = 0
		
	def determineAgreeableness(self):
		# trait_4 = Letter Size, Top Margin, Right Margin & Slant | 2 = high, 1 = average, 0 = low
		if (self.fList[2] == 1 or self.fList[3] == 0 or self.fList[4] == 3):
			self.labelList[3] = 2
		elif (self.fList[1] == 1 or self.fList[3] == 1 or self.fList[4] in [4,6]):
			self.labelList[3] = 1
		elif (self.fList[1] == 3 or self.fList[2] in [0,3] or self.fList[3] == 3 or self.fList[4] in [0,1]):
			self.labelList[3] = 0
		
	def determineNeuroticism(self):
		# trait_5 = Baseline, Letter Size, Right Margin & Slant | 1 = High, 0 = Low
		if (self.fList[0] == 2 or self.fList[1] == 1 or self.fList[3] in [0,2,3] or self.fList[4] in [0,5,6]):
			self.labelList[4] = 1
		elif (self.fList[0] == 1 or self.fList[1] == 2 or self.fList[3] == 1 or self.fList[4] == 2):
			self.labelList[4] = 0
	
	def giveLabel(self):
		self.determineOpenness()
		self.determineConscientiousness()
		self.determineExtroversion()
		self.determineAgreeableness()
		self.determineNeuroticism()
		return self.labelList

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
	
	if new or not present: # If new images are found or the label_list is not present
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

