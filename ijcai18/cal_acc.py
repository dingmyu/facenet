Right = 0
TP = 0#zheng zheng
TN = 0#fu fu
FP = 0#fu bei panwei zheng
FN = 0#zheng bei panwei fu
PP = 0#yuce de zheng
P = 0#shiji de zheng
f1 = open('feature_test.txt').readlines()
f2 = open('depression/newtest.txt').readlines()
for i in range(len(f1)):
	pic, label = f2[i].strip().split()
	label = int(label)
	pre1, pre2 = f1[i].strip().split()
	predict = 0 if float(pre1) > float(pre2) else 1
	if label == 1:
		P += 1
		if predict == 1:
			TP += 1
			Right += 1
			PP += 1
		if predict == 0:
			FN += 1
	if label == 0:
		if predict == 0:
			TN += 1
			Right += 1
		if predict == 1:
			FP += 1
			PP += 1

print Right
print "TP,TN,FP,FN,PP,P: ",TP,TN,FP,FN,PP,P
print "PPV: %f" %(float(TP)/float(PP))
print "sensitivity: %f" %(float(TP)/float(P))
print "FPR: %f" %(float(FP)/float(FP+TN))
print "spe: %f" %(1-float(FP)/float(FP+TN))
print "npv: %f" %(float(TN)/float(FN+TN))
print "FNR: %f" %(float(FN)/float(FN+TP))
print "Voting Accuracy: %f(%d/%d)" %(float(Right)/len(f1), Right, len(f1))
