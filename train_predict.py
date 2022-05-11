import os
import itertools
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import traits
import unique_pers as personality

X_baseline_angle = []
X_letter_size = []
X_top_margin = []
X_right_margin = []
X_slant_angle = []
y_optimism, y_pecimism, y_depression, y_joy, y_fear, y_goal, y_esteem, y_value, y_observant, y_vision= [],[],[],[],[],[],[],[],[],[]
y_confidence, y_extrovert, y_introvert, y_generous, y_selfish, y_polite, y_management, y_honesty = [],[],[],[],[],[],[],[]
y_emotional, y_practical, y_adjustment, y_concentration, y_imagination, y_conservative, y_dependent = [],[],[],[],[],[],[]
y_control, y_trust, y_talkative, y_relate, y_stable, y_expressive, y_perfectionist, y_initiation, y_listner = [],[],[],[],[],[],[],[],[]
page_ids = []

if os.path.isfile("label_list"):
	print ("Info: label_list found.")
	#=================================================================
	with open("label_list", "r") as labels:
		for line in labels:
			content = line.split()
			
			baseline_angle = float(content[0])
			X_baseline_angle.append(baseline_angle)
			
			letter_size = float(content[1])
			X_letter_size.append(letter_size)
			
			top_margin = float(content[2])
			X_top_margin.append(top_margin)
			
			right_margin = float(content[3])
			X_right_margin.append(right_margin)
			
			slant_angle = float(content[4])
			X_slant_angle.append(slant_angle)
			
			trait_1 = float(content[5])
			y_optimism.append(trait_1)
			
			trait_2 = float(content[6])
			y_pecimism.append(trait_2)
			
			trait_3 = float(content[7])
			y_depression.append(trait_3)
			
			trait_4 = float(content[8])
			y_joy.append(trait_4)

			trait_5 = float(content[9])
			y_fear.append(trait_5)

			trait_6 = float(content[10])
			y_goal.append(trait_6)
			
			trait_7 = float(content[11])
			y_esteem.append(trait_7)
			
			trait_8 = float(content[12])
			y_value.append(trait_8)
			
			trait_9 = float(content[13])
			y_observant.append(trait_9)

			trait_10 = float(content[14])
			y_vision.append(trait_10)

			trait_11 = float(content[15])
			y_confidence.append(trait_11)
			
			trait_12 = float(content[16])
			y_extrovert.append(trait_12)
			
			trait_13 = float(content[17])
			y_introvert.append(trait_13)
			
			trait_14 = float(content[18])
			y_generous.append(trait_14)

			trait_15 = float(content[19])
			y_selfish.append(trait_15)

			trait_16 = float(content[20])
			y_polite.append(trait_16)
			
			trait_17 = float(content[21])
			y_management.append(trait_17)
			
			trait_18 = float(content[22])
			y_honesty.append(trait_18)
			
			trait_19 = float(content[23])
			y_emotional.append(trait_19)

			trait_20 = float(content[24])
			y_practical.append(trait_20)

			trait_21 = float(content[25])
			y_adjustment.append(trait_21)
			
			trait_22 = float(content[26])
			y_concentration.append(trait_22)
			
			trait_23 = float(content[27])
			y_imagination.append(trait_23)
			
			trait_24 = float(content[28])
			y_conservative.append(trait_24)

			trait_25 = float(content[29])
			y_dependent.append(trait_25)

			"""trait_26 = float(content[30])
			y_relation.append(trait_26)"""
			
			trait_27 = float(content[30])
			y_control.append(trait_27)
			
			trait_28 = float(content[31])
			y_trust.append(trait_28)
			
			trait_29 = float(content[32])
			y_talkative.append(trait_29)

			trait_30 = float(content[33])
			y_relate.append(trait_30)

			trait_31 = float(content[34])
			y_stable.append(trait_31)
			
			trait_32 = float(content[35])
			y_expressive.append(trait_32)
			
			trait_33 = float(content[36])
			y_perfectionist.append(trait_33)
			
			trait_34 = float(content[37])
			y_initiation.append(trait_34)

			trait_35 = float(content[38])
			y_listner.append(trait_35)

			page_id = content[39]
			page_ids.append(page_id)
	#===============================================================
	
	# Optimism
	X_t1 = []
	for a, b, c in itertools.zip_longest(X_baseline_angle, X_letter_size, X_right_margin):
		X_t1.append([a, b, c])
	
	# Pecimism
	X_t2 = []
	for a, b, c in itertools.zip_longest(X_baseline_angle, X_letter_size, X_right_margin):
		X_t2.append([a, b, c])
		
	# Depression
	X_t3 = []
	for a, b, c in itertools.zip_longest(X_baseline_angle, X_right_margin, X_slant_angle):
		X_t3.append([a, b, c])
		
	# Joy
	X_t4 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_slant_angle):
		X_t4.append([a, b])
		
	# Fear    
	X_t5 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_right_margin, X_slant_angle):
		X_t5.append([a, b, c])

	# Goal Oriented
	X_t6 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_slant_angle):
		X_t6.append([a, b])
	
	# Self Esteem
	X_t7 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_top_margin, X_slant_angle):
		X_t7.append([a, b, c])
		
	# Others Value
	X_t8 = []
	for a, b in itertools.zip_longest(X_letter_size, X_right_margin):
		X_t8.append([a, b])
		
	# Observant
	X_t9 = []
	for a, b in itertools.zip_longest(X_letter_size, X_slant_angle):
		X_t9.append([a, b])
		
	# Vision    
	X_t10 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_letter_size): # error correcction
		X_t10.append([a, b])

	# Self Confidence
	X_t11 = []
	for a, b in itertools.zip_longest(X_letter_size, X_slant_angle):
		X_t11.append([a, b])
	
	# Extrovert
	X_t12 = []
	for a, b, c, d in itertools.zip_longest(X_letter_size, X_top_margin, X_right_margin, X_slant_angle):
		X_t12.append([a, b, c, d])
		
	# Introvert
	X_t13 = []
	for a, b, c, d in itertools.zip_longest(X_letter_size, X_top_margin, X_right_margin, X_slant_angle):
		X_t13.append([a, b, c, d])
		
	# Generous
	X_t14 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_top_margin, X_right_margin):
		X_t14.append([a, b, c])
		
	# Selfish
	X_t15 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_top_margin): # error correction
		X_t15.append([a, b])

	# Polite
	X_t16 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_top_margin, X_slant_angle):
		X_t16.append([a, b, c])
	
	# Management
	X_t17 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_top_margin, X_slant_angle):
		X_t17.append([a, b, c])
		
	# Honesty
	X_t18 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_right_margin, X_slant_angle):
		X_t18.append([a, b, c])
		
	# Emotional
	X_t19 = []
	for a, b in itertools.zip_longest(X_letter_size, X_slant_angle):
		X_t19.append([a, b])
		
	# Practical    
	X_t20 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_right_margin, X_slant_angle):
		X_t20.append([a, b, c])

	# Adjustment
	X_t21 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_top_margin, X_slant_angle):
		X_t21.append([a, b, c])
	
	# Concentration
	X_t22 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_right_margin, X_slant_angle):
		X_t22.append([a, b, c])
		
	# Imagination
	X_t23 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_right_margin, X_slant_angle):
		X_t23.append([a, b, c])
		
	# Conservative
	X_t24 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_right_margin, X_slant_angle):
		X_t24.append([a, b, c])
		
	# Dependent    
	X_t25 = []
	for a, b in itertools.zip_longest(X_top_margin, X_slant_angle):
		X_t25.append([a, b])

	# Relations
	"""X_t26 = []
	for a, b, c in itertools.zip_longest(X_top_margin, X_right_margin, X_slant_angle):
		X_t26.append([a, b, c])"""
	
	# Self Control
	X_t27 = []
	for a, b, c in itertools.zip_longest(X_top_margin, X_right_margin, X_slant_angle):
		X_t27.append([a, b, c])
		
	# Trust
	X_t28 = []
	for a, b, c in itertools.zip_longest(X_top_margin, X_right_margin, X_slant_angle):
		X_t28.append([a, b, c])
		
	# Talkative
	X_t29 = []
	for a, b, c in itertools.zip_longest(X_letter_size, X_right_margin, X_slant_angle):
		X_t29.append([a, b, c])
		
	# Relate    
	X_t30 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_right_margin): # error correction
		X_t30.append([a, b])

	# Stable
	X_t31 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_slant_angle): # error correction
		X_t31.append([a, b])
	
	# Expressive
	X_t32 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_slant_angle): # error correction
		X_t32.append([a, b])
		
	# Perfectionist
	X_t33 = []
	for a, b in itertools.zip_longest(X_letter_size, X_slant_angle):
		X_t33.append([a, b])
		
	# Initiation
	X_t34 = []
	for a, b, c in itertools.zip_longest(X_top_margin, X_right_margin, X_slant_angle):
		X_t34.append([a, b, c])
		
	# Listner    
	X_t35 = []
	for a, b in itertools.zip_longest(X_baseline_angle, X_top_margin): # error correction
		X_t35.append([a, b])
	
	#print (X_t1)
	#print (type(X_t1))
	#print (len(X_t1))
	
	sum_acc = 0.0

	X_train, X_test, y_train, y_test = train_test_split(X_t1, y_optimism, test_size = .30, random_state=8)
	clf1 = SVC(kernel='rbf')
	clf1.fit(X_train, y_train)
	x=accuracy_score(clf1.predict(X_test), y_test)
	print ("Classifier 1(Optimism) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t2, y_pecimism, test_size = .30, random_state=16)
	clf2 = SVC(kernel='rbf')
	clf2.fit(X_train, y_train)
	x=accuracy_score(clf2.predict(X_test), y_test)
	print ("Classifier 2(Pecimism) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t3, y_depression, test_size = .30, random_state=32)
	clf3 = SVC(kernel='rbf')
	clf3.fit(X_train, y_train)
	x=accuracy_score(clf3.predict(X_test), y_test)
	print ("Classifier 3(Depression) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t4, y_joy, test_size = .30, random_state=64)
	clf4 = SVC(kernel='rbf')
	clf4.fit(X_train, y_train)
	x=accuracy_score(clf4.predict(X_test), y_test)
	print ("Classifier 4(Joy) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t5, y_fear, test_size = .30, random_state=42)
	clf5 = SVC(kernel='rbf')
	clf5.fit(X_train, y_train)
	x=accuracy_score(clf5.predict(X_test), y_test)
	print ("Classifier 5(Fear) accuracy: ",x)
	sum_acc += x

	X_train, X_test, y_train, y_test = train_test_split(X_t6, y_goal, test_size = .30, random_state=8)
	clf6 = SVC(kernel='rbf')
	clf6.fit(X_train, y_train)
	x=accuracy_score(clf6.predict(X_test), y_test)
	print ("Classifier 6(Goal Oriented) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t7, y_esteem, test_size = .30, random_state=16)
	clf7 = SVC(kernel='rbf')
	clf7.fit(X_train, y_train)
	x=accuracy_score(clf7.predict(X_test), y_test)
	print ("Classifier 7(Self Esteem) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t8, y_value, test_size = .30, random_state=32)
	clf8 = SVC(kernel='rbf')
	clf8.fit(X_train, y_train)
	x=accuracy_score(clf8.predict(X_test), y_test)
	print ("Classifier 8(Others Value) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t9, y_observant, test_size = .30, random_state=64)
	clf9 = SVC(kernel='rbf')
	clf9.fit(X_train, y_train)
	x=accuracy_score(clf9.predict(X_test), y_test)
	print ("Classifier 9(Observant) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t10, y_vision, test_size = .30, random_state=42)
	clf10 = SVC(kernel='rbf')
	clf10.fit(X_train, y_train)
	x=accuracy_score(clf10.predict(X_test), y_test)
	print ("Classifier 10(Vision) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t11, y_confidence, test_size = .30, random_state=8)
	clf11 = SVC(kernel='rbf')
	clf11.fit(X_train, y_train)
	x=accuracy_score(clf11.predict(X_test), y_test)
	print ("Classifier 11(Self-Confidence) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t12, y_extrovert, test_size = .30, random_state=16)
	clf12 = SVC(kernel='rbf')
	clf12.fit(X_train, y_train)
	x=accuracy_score(clf12.predict(X_test), y_test)
	print ("Classifier 12(Extrovert) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t13, y_introvert, test_size = .20, random_state=32)
	clf13 = SVC(kernel='rbf')
	clf13.fit(X_train, y_train)
	x=accuracy_score(clf13.predict(X_test), y_test)
	print ("Classifier 13(Introvert) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t14, y_generous, test_size = .30, random_state=64)
	clf14 = SVC(kernel='rbf')
	clf14.fit(X_train, y_train)
	x=accuracy_score(clf14.predict(X_test), y_test)
	print ("Classifier 14(Generous) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t15, y_selfish, test_size = .30, random_state=42)
	clf15 = SVC(kernel='rbf')
	clf15.fit(X_train, y_train)
	x=accuracy_score(clf15.predict(X_test), y_test)
	print ("Classifier 15(Selfish) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t16, y_polite, test_size = .30, random_state=8)
	clf16 = SVC(kernel='rbf')
	clf16.fit(X_train, y_train)
	x=accuracy_score(clf16.predict(X_test), y_test)
	print ("Classifier 16(Polite) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t17, y_management, test_size = .30, random_state=16)
	clf17 = SVC(kernel='rbf')
	clf17.fit(X_train, y_train)
	x=accuracy_score(clf17.predict(X_test), y_test)
	print ("Classifier 17(Management) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t18, y_honesty, test_size = .30, random_state=32)
	clf18 = SVC(kernel='rbf')
	clf18.fit(X_train, y_train)
	x=accuracy_score(clf18.predict(X_test), y_test)
	print ("Classifier 18(Honesty) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t19, y_emotional, test_size = .20, random_state=64)
	clf19 = SVC(kernel='rbf')
	clf19.fit(X_train, y_train)
	x=accuracy_score(clf19.predict(X_test), y_test)
	print ("Classifier 19(Emotional) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t20, y_practical, test_size = .20, random_state=42)
	clf20 = SVC(kernel='rbf')
	clf20.fit(X_train, y_train)
	x=accuracy_score(clf20.predict(X_test), y_test)
	print ("Classifier 20(Practical) accuracy: ",x)
	sum_acc += x

	X_train, X_test, y_train, y_test = train_test_split(X_t21, y_adjustment, test_size = .30, random_state=8)
	clf21 = SVC(kernel='rbf')
	clf21.fit(X_train, y_train)
	x=accuracy_score(clf21.predict(X_test), y_test)
	print ("Classifier 21(Adjustment) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t22, y_concentration, test_size = .20, random_state=16)
	clf22 = SVC(kernel='rbf')
	clf22.fit(X_train, y_train)
	x=accuracy_score(clf22.predict(X_test), y_test)
	print ("Classifier 22(Concentration) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t23, y_imagination, test_size = .20, random_state=32)
	clf23 = SVC(kernel='rbf')
	clf23.fit(X_train, y_train)
	x=accuracy_score(clf23.predict(X_test), y_test)
	print ("Classifier 23(Imagination) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t24, y_conservative, test_size = .30, random_state=64)
	clf24 = SVC(kernel='rbf')
	clf24.fit(X_train, y_train)
	x=accuracy_score(clf24.predict(X_test), y_test)
	print ("Classifier 24(Conservative) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t25, y_dependent, test_size = .30, random_state=42)
	clf25 = SVC(kernel='rbf')
	clf25.fit(X_train, y_train)
	x=accuracy_score(clf25.predict(X_test), y_test)
	print ("Classifier 25(Dependent) accuracy: ",x)
	sum_acc += x

	"""X_train, X_test, y_train, y_test = train_test_split(X_t26, y_relation, test_size = .30, random_state=8)
	clf26 = SVC(kernel='rbf')
	clf26.fit(X_train, y_train)
	print ("Classifier 26 accuracy: ",accuracy_score(clf26.predict(X_test), y_test))"""
	
	X_train, X_test, y_train, y_test = train_test_split(X_t27, y_control, test_size = .20, random_state=16)
	clf27 = SVC(kernel='rbf')
	clf27.fit(X_train, y_train)
	x=accuracy_score(clf27.predict(X_test), y_test)
	print ("Classifier 27(Self Control) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t28, y_trust, test_size = .30, random_state=32)
	clf28 = SVC(kernel='rbf')
	clf28.fit(X_train, y_train)
	x=accuracy_score(clf28.predict(X_test), y_test)
	print ("Classifier 28(Trust) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t29, y_talkative, test_size = .30, random_state=64)
	clf29 = SVC(kernel='rbf')
	clf29.fit(X_train, y_train)
	x=accuracy_score(clf29.predict(X_test), y_test)
	print ("Classifier 29(Talkative) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t30, y_relate, test_size = .30, random_state=42)
	clf30 = SVC(kernel='rbf')
	clf30.fit(X_train, y_train)
	x=accuracy_score(clf30.predict(X_test), y_test)
	print ("Classifier 30(Relate) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t31, y_stable, test_size = .30, random_state=8)
	clf31 = SVC(kernel='rbf')
	clf31.fit(X_train, y_train)
	x=accuracy_score(clf31.predict(X_test), y_test)
	print ("Classifier 31(Stable) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t32, y_expressive, test_size = .30, random_state=16)
	clf32 = SVC(kernel='rbf')
	clf32.fit(X_train, y_train)
	x=accuracy_score(clf32.predict(X_test), y_test)
	print ("Classifier 32(Expressive) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t33, y_perfectionist, test_size = .30, random_state=32)
	clf33 = SVC(kernel='rbf')
	clf33.fit(X_train, y_train)
	x=accuracy_score(clf33.predict(X_test), y_test)
	print ("Classifier 33(Perfectionist) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t34, y_initiation, test_size = .30, random_state=64)
	clf34 = SVC(kernel='rbf')
	clf34.fit(X_train, y_train)
	x=accuracy_score(clf34.predict(X_test), y_test)
	print ("Classifier 34(Initiation) accuracy: ",x)
	sum_acc += x
	
	X_train, X_test, y_train, y_test = train_test_split(X_t35, y_listner, test_size = .30, random_state=42)
	clf35 = SVC(kernel='rbf')
	clf35.fit(X_train, y_train)
	x=accuracy_score(clf35.predict(X_test), y_test)
	print ("Classifier 35(Listener) accuracy: ",x)
	sum_acc += x
	
	avg_acc = sum_acc/34
	print(avg_acc)
	#================================================================================================

	while True:
		direct = "dataset/"
		print ()
		file_name = input("Enter file name to predict or z to exit: ")
		if file_name == 'z':
			break
		labelDict = {"Optimism":0 , "Pecimism":0 , "Depression":0 , "Joy":0 , "Fear":0 , "Goal Oriented":0 , "Self Esteem":0 , "Others Value":0 , "Observant":0 , "Vision":0 , "Self Confidence":0 , "Extrovert":0 , "Introvert":0 , "Generous":0 , "Selfish":0 , "Polite":0 , "Management":0 , "Honesty":0 , "Emotional":0 , "Practical":0 , "Adjustment":0 , "Concentration":0 , "Imagination":0 , "Conservative":0 , "Dependent":0 , "Self Control":0 , "Trust":0 , "Talkative":0 , "Relate":0 , "Stable":0 , "Expressive":0 , "Perfectionist":0 , "Initiation":0 , "Listner":0}
		raw_features, category = traits.features.extract(direct+file_name)
		
		print ("Baseline Angle: "+category[0][1])
		print ("Letter Size: "+category[1][1])
		print ("Top Margin: "+category[2][1])
		print ("Right Margin: "+category[3][1])
		print ("Slant: "+category[4][1])
		print ()
		
		labelDict["Optimism"]= int(clf1.predict([[category[0][0], category[1][0], category[3][0]]]))
		labelDict["Pecimism"]= int(clf2.predict([[category[0][0], category[1][0], category[3][0]]]))
		labelDict["Depression"]= int(clf3.predict([[category[0][0], category[3][0], category[4][0]]]))
		labelDict["Joy"]= int(clf4.predict([[category[0][0], category[4][0]]]))
		labelDict["Fear"]= int(clf5.predict([[category[1][0], category[3][0], category[4][0]]]))
		labelDict["Goal Oriented"]= int(clf6.predict([[category[0][0], category[4][0]]]))
		labelDict["Self Esteem"]= int(clf7.predict([[category[1][0], category[2][0], category[4][0]]]))
		labelDict["Others Value"]= int(clf8.predict([[category[1][0], category[3][0]]]))
		labelDict["Observant"]= int(clf9.predict([[category[1][0], category[4][0]]]))
		labelDict["Vision"]= int(clf10.predict([[category[0][0], category[1][0]]]))
		labelDict["Self Confidence"]= int(clf11.predict([[category[1][0], category[4][0]]]))
		labelDict["Extrovert"]= int(clf12.predict([[category[1][0], category[2][0], category[3][0], category[4][0]]]))
		labelDict["Introvert"]= int(clf13.predict([[category[1][0], category[2][0], category[3][0], category[4][0]]]))
		labelDict["Generous"]= int(clf14.predict([[category[1][0], category[2][0], category[3][0]]]))
		labelDict["Selfish"]= int(clf15.predict([[category[0][0], category[2][0]]]))
		labelDict["Polite"]= int(clf16.predict([[category[1][0], category[2][0], category[4][0]]]))
		labelDict["Management"]= int(clf17.predict([[category[1][0], category[2][0], category[4][0]]]))
		labelDict["Honesty"]= int(clf18.predict([[category[1][0], category[3][0], category[4][0]]]))
		labelDict["Emotional"]= int(clf19.predict([[category[1][0], category[4][0]]]))
		labelDict["Practical"]= int(clf20.predict([[category[1][0], category[3][0], category[4][0]]]))
		labelDict["Adjustment"]= int(clf21.predict([[category[1][0], category[2][0], category[4][0]]]))
		labelDict["Concentration"]= int(clf22.predict([[category[1][0], category[3][0], category[4][0]]]))
		labelDict["Imagination"]= int(clf23.predict([[category[1][0], category[3][0], category[4][0]]]))
		labelDict["Conservative"]= int(clf24.predict([[category[1][0], category[3][0], category[4][0]]]))
		labelDict["Dependent"]= int(clf25.predict([[category[2][0], category[4][0]]]))
		"""labelDict["Relations"]= int(clf26.predict([[category[2][0], category[3][0], category[4][0]]]))"""
		labelDict["Self Control"]= int(clf27.predict([[category[2][0], category[3][0], category[4][0]]]))
		labelDict["Trust"]= int(clf28.predict([[category[2][0], category[3][0], category[4][0]]]))
		labelDict["Talkative"]= int(clf29.predict([[category[1][0], category[3][0], category[4][0]]]))
		labelDict["Relate"]= int(clf30.predict([[category[0][0], category[3][0]]]))
		labelDict["Stable"]= int(clf31.predict([[category[0][0], category[4][0]]]))
		labelDict["Expressive"]= int(clf32.predict([[category[0][0], category[4][0]]]))
		labelDict["Perfectionist"]= int(clf33.predict([[category[1][0], category[4][0]]]))
		labelDict["Initiation"]= int(clf34.predict([[category[2][0], category[3][0], category[4][0]]]))
		labelDict["Listner"]= int(clf35.predict([[category[0][0], category[2][0]]]))
		
		personality.output(labelDict)

		'''print()
		print ("Optimism: ", int(clf1.predict([[category[0][0], category[1][0], category[3][0]]])))
		print ("Pecimism: ", clf2.predict([[category[0][0], category[1][0], category[3][0]]]))
		print ("Depression: ", clf3.predict([[category[0][0], category[3][0], category[4][0]]]))
		print ("Joy: ", clf4.predict([[category[0][0], category[4][0]]]))
		print ("Fear: ", clf5.predict([[category[1][0], category[3][0], category[4][0]]]))
		print ("Goal Oriented: ", clf6.predict([[category[0][0], category[4][0]]]))
		print ("Self Esteem: ", clf7.predict([[category[1][0], category[2][0], category[4][0]]]))
		print ("Others Value: ", clf8.predict([[category[1][0], category[3][0]]]))
		print ("Observant: ", clf9.predict([[category[1][0], category[4][0]]]))
		print ("Vision: ", clf10.predict([[category[0][0], category[1][0]]]))
		print ("Self Confidence: ", clf11.predict([[category[1][0], category[4][0]]]))
		print ("Extrovert: ", clf12.predict([[category[1][0], category[2][0], category[3][0], category[4][0]]]))
		print ("Introvert: ", clf13.predict([[category[1][0], category[2][0], category[3][0], category[4][0]]]))
		print ("Generous: ", clf14.predict([[category[1][0], category[2][0], category[3][0]]]))
		print ("Selfish: ", clf15.predict([[category[0][0], category[2][0]]]))
		print ("Polite: ", clf16.predict([[category[1][0], category[2][0], category[4][0]]]))
		print ("Management: ", clf17.predict([[category[1][0], category[2][0], category[4][0]]]))
		print ("Honesty: ", clf18.predict([[category[1][0], category[3][0], category[4][0]]]))
		print ("Emotional: ", clf19.predict([[category[1][0], category[4][0]]]))
		print ("Practical: ", clf20.predict([[category[1][0], category[3][0], category[4][0]]]))
		print ("Adjustment: ", clf21.predict([[category[1][0], category[2][0], category[4][0]]]))
		print ("Concentration: ", clf22.predict([[category[1][0], category[3][0], category[4][0]]]))
		print ("Imagination: ", clf23.predict([[category[1][0], category[3][0], category[4][0]]]))
		print ("Conservative: ", clf24.predict([[category[1][0], category[3][0], category[4][0]]]))
		print ("Dependent: ", clf25.predict([[category[2][0], category[4][0]]]))
		"""print ("Relations: ", clf26.predict([[category[2][0], category[3][0], category[4][0]]]))"""
		print ("Self Control: ", clf27.predict([[category[2][0], category[3][0], category[4][0]]]))
		print ("Trust: ", clf28.predict([[category[2][0], category[3][0], category[4][0]]]))
		print ("Talkative: ", clf29.predict([[category[1][0], category[3][0], category[4][0]]]))
		print ("Relate: ", clf30.predict([[category[0][0], category[3][0]]]))
		print ("Stable: ", clf31.predict([[category[0][0], category[4][0]]]))
		print ("Expressive: ", clf32.predict([[category[0][0], category[4][0]]]))
		print ("Perfectionist: ", clf33.predict([[category[1][0], category[4][0]]]))
		print ("Initiation: ", clf34.predict([[category[2][0], category[3][0], category[4][0]]]))
		print ("Listner: ", clf35.predict([[category[0][0], category[2][0]]]))
		print ("---------------------------------------------------")
		print()'''
		
	#=================================================================================================
		
else:
	print ("Error: label_list file not found.")
