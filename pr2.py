import sys,math,time,numpy
import matplotlib.pyplot as plt

def calc_slope(mean_y2,mean_y1,mean_x1,mean_x2):
	m = (mean_y2 - mean_y1)/(mean_x2 - mean_x1)
	return -1*(1/m)

def cal_mean(array):
	mean = 0
	for x in range((3*len(array))//4):					#calculating mean
		mean += array[x];
	return mean/((3*len(array))//4)

def cal_var(array,mean):
	var = 0
	for x in range((3*len(array))//4):					#calculating variance
		var += math.pow((array[x]-mean),2)
	return (var/((3*len(array))//4))

def rem(array1,array2):
	l1 = (int)((len(array1)*3)/4)
	for i in range(0,l1):
		array1.pop(0)
		array2.pop(0)

def cov(array1,array2,mean1,mean2):
	co = 0
	for i in range((3*len(array1))//4):					#calculating co-var for files 1 & 2
		co += ((array1[i]-mean1)*(array2[i] - mean2))
	return co/((3*len(array1)//4 ) - 1)

def mul(X,Y):
	result = numpy.zeros(shape=(2,1))

	for i in range(len(X)):
   		for j in range(len(Y[0])):
   			for k in range(len(Y)):
   				result[i][j] += X[i][k] * Y[k][j]
	return result
def determinant(X):
	return X[0,0] * X[1,1] - X[1,0] * X[0,1]

def find_r(x1,x2,y1,y2):
	m = []
	if max(array_x1) > max(array_x2):
		m.append(max(array_x1))
	else:	
		m.append(max(array_x2))
	if max(array_y1) > max(array_y2):
		m.append(max(array_y1))
	else:
		m.append(max(array_y2))
	if min(array_x1) < min(array_x2):
		m.append(min(array_x1))
	else:	
		m.append(min(array_x2))
	if min(array_y1) < min(array_y2):
		m.append(min(array_y1))
	else:
		m.append(min(array_y2))	
	return m

def subtract(X,Y):
	a = numpy.zeros(shape=(len(X),len(Y[0])))
	for i in range(len(X)):
		for j in range(len(X[0])):
			a[i][j] = X[i][j] - Y[i][j]
	return a

def add(X,Y):
	a = numpy.zeros(shape=(len(X),len(Y[0])))
	for i in range(len(X)):
		for j in range(len(X[0])):
			a[i][j] = X[i][j] + Y[i][j]
	return a

def mean(x,y):
	m = numpy.zeros(shape=(2,1))
	m[0,0] = x
	m[1,0] = y
	return m

def transpose(X):
	m = numpy.zeros(shape=(1,2))
	m[0,0] = X[0,0]
	m[0,1] = X[1,0]
	return m


def inverse(X,d):
	temp = (X[0,0]/d)
	X[0,0] = (X[1,1]/d)
	X[1,1] = temp
	temp = (-1*X[0,1])/d
	X[0,1] = X[1,0] = temp
	return X

file1 = input("Enter file name(1): \n")
fp1 = open(file1,"r")
file2 = input("Enter file name(2): \n")
fp2 = open(file2,"r")

array_x1,array_y1,array_x2,array_y2 = [],[],[],[]


for line in fp1:
	m,n = line.split()
	array_x1.append(float(m))
	array_y1.append(float(n))
for line in fp2:
	m,n = line.split()
	array_x2.append(float(m))
	array_y2.append(float(n))

mean_x1,mean_y1,mean_x2,mean_y2 = cal_mean(array_x1),cal_mean(array_y1),cal_mean(array_x2),cal_mean(array_y2)
var_x1,var_x2,var_y1,var_y2 = cal_var(array_x1,mean_x1),cal_var(array_x2,mean_x2),cal_var(array_y1,mean_y1) ,cal_var(array_y2,mean_y2)
	
co_1 = cov(array_x1,array_y1,mean_x1,mean_y1)
co_2 = cov(array_x2,array_y2,mean_x2,mean_y2)

cov_m = numpy.zeros(shape=(2,2))
cov_m[0,0] = (var_x1 + var_x2)/2
cov_m[1,1] = (var_y1 + var_y2)/2
cov_m[0,1] = (co_1 + co_2)/2
cov_m[1,0] =cov_m[0,1]

det = determinant(cov_m)						#determinant of cov-matrix

cov_1 = inverse(cov_m,det)						#inverse of cov-matrix

mean1 = mean(mean_x1,mean_y1)
mean2 = mean(mean_x2,mean_y2)
	
slope = mul(cov_1,subtract(mean1,mean2))				#multiply cov_matrix and mean
m = slope[1,0]/slope[0,0]
slope = -1*(1/m)

c0 = mul(transpose(subtract(mean1,mean2)),mul(cov_1,subtract(mean1,mean2)))[0,0]

x_0 = subtract((0.5*add(mean1,mean2)), ((-1*math.log(len(array_x1)/len(array_x2)) / c0) * subtract(mean1,mean2)))

x0_1 = x_0[0,0]
x0_2 = x_0[1,0]

c = x0_2 - slope*x0_1
r = find_r(array_x1,array_x2,array_y1,array_y2)

plot1,plot2 = [],[]
for x in range (int(r[2])-1,int(r[0])+1):
	plot1.append(x)
	plot2.append(slope*x + c)

plt.plot(plot1, plot2, c = "m")

plt.title('Data from')
plt.xlabel('-----------------------X-----------------------')
plt.ylabel('-----------------------Y-----------------------')

rem(array_x1,array_y1)
rem(array_x2,array_y2)

TP,TN,FP,FN = 0,0,0,0
# conf_m = numpy.zeros(shape=(2,2))
for i in range(len(array_x1)):
	if(array_y1[int(mean_x1)] - slope*array_x1[int(mean_y1)] - c > 0):			
		if(array_y1[i] - slope*array_x1[i] - c > 0):
			TP += 1
		else:
			FN += 1
	else:
		if(array_y1[i] - slope*array_x1[i] - c < 0):
			TP += 1
		else:
			FN += 1

for i in range(len(array_x2)):
	if(array_y2[int(mean_x2)] - slope*array_x2[int(mean_y2)] - c > 0):
		if(array_y2[i] - slope*array_x2[i] - c > 0):
			TN += 1
		else:
			FP += 1
	else:
		if(array_y2[i] - slope*array_x2[i] - c < 0):
			TN += 1
		else:
			FP += 1

l1 = ("TN="+str(TN)).ljust(10) + ("FP="+str(FP)).ljust(10)
l2 = ( "FN="+str(FN)).ljust(10) + ("TP="+str(TP)).ljust(10)
print("\nConfusion Matrix for ",file1," ",file2,"\n")
print(l1)
print("\n")
print(l2)

plt.scatter(array_x1,array_y1,c = 'r')
plt.scatter(array_x2,array_y2,c = 'b')
# plt.show()
plt.savefig("res2.png")
fp1.close()
fp2.close()
