import sys,math,time,numpy
import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor'] = 'wheat'

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

def mul(X,Y):
	result = numpy.zeros(shape=(len(X),len(Y[0])))
	for i in range(len(X)):
   		for j in range(len(Y[0])):
   			for k in range(len(Y)):
   				result[i][j] += X[i][k] * Y[k][j]
	return result

def determinant(X):
	return (X[0,0] * X[1,1] - X[1,0] * X[0,1])

def cov_m(var_x,var_y):
	cov_mat = numpy.zeros(shape=(2,2))
	cov_mat[0,0] = var_x
	cov_mat[1,1] = var_y
	return cov_mat

def inverse(X,d):
	temp = (X[0,0]/d)
	X[0,0] = (X[1,1]/d)
	X[1,1] = temp
	return X

def subtract(X,Y):
	a = numpy.zeros(shape=(len(X),len(Y[0])))
	for i in range(len(X)):
		for j in range(len(X[0])):
			a[i][j] = X[i][j] - Y[i][j]
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

mean1 = mean(mean_x1,mean_y1)
mean2 = mean(mean_x2,mean_y2)

cov_m1 = cov_m(var_x1,var_y1)
cov_m2 = cov_m(var_x2,var_y2)

det1 = determinant(cov_m1)						#determinant of cov_matrix
det2 = determinant(cov_m2)

cov_1 = inverse(cov_m1,det1)						#inverse of 2X2 matrix
cov_2 = inverse(cov_m2,det2)

a_t = subtract(cov_1,cov_2)						#subtract two matrices

b_t = subtract(mul(cov_1,mean1),mul(cov_2,mean2))
b = transpose(b_t)

c1_t = mul(cov_1,mean1)
c1 = mul(transpose(mean1),c1_t)
c1 = -0.5*c1

c2_t = mul(cov_2,mean2)
c2 = mul(transpose(mean2),c2_t)
c2 = 0.5*c2

ln = math.log(abs(det1)/abs(det2))
ln = -0.5*ln + math.log(len(array_x1)/len(array_x2))
c = c1[0,0] + c2[0,0] + ln

a1 = (-0.5)*a_t[0,0]
a2 = (-0.5)*a_t[1,1]

r = find_r(array_x1,array_x2,array_y1,array_y2)

x = numpy.linspace(r[2], r[0], 400)
y = numpy.linspace(r[3], r[1], 400)
x, y = numpy.meshgrid(x, y)
plt.contour(x, y,(a1*x**2 + a2*y**2 + b[0,0]*x + b[0,1]*y + c), [0], colors='r')

plt.xlabel('-----------------------X-----------------------')
plt.ylabel('-----------------------Y-----------------------')

rem(array_x1,array_y1)
rem(array_x2,array_y2)

plt.scatter(array_x1,array_y1,c = 'g')
plt.scatter(array_x2,array_y2,c = 'm')

plt.savefig('res3.png')
fp1.close()
fp2.close()
