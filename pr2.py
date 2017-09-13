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


mean_x1,mean_y1,mean_x2,mean_y2 = 0,0,0,0

mean_x1 = cal_mean(array_x1)
mean_y1 = cal_mean(array_y1)
mean_x2 = cal_mean(array_x2)
mean_y2 = cal_mean(array_y2)

var_x1,var_x2,var_y1,var_y2 = 0, 0 , 0 , 0

var_x1 = cal_var(array_x1,mean_x1)
var_y1 = cal_var(array_y1,mean_y1)
var_x2 = cal_var(array_x2,mean_x2)
var_y2 = cal_var(array_y2,mean_y2)

co_1 = cov(array_x1,array_y1,mean_x1,mean_y1)
co_2 = cov(array_x2,array_y2,mean_x2,mean_y2)

cov_m = numpy.zeros(shape=(2,2))
cov_m[0,0] = (var_x1 + var_x2)/2
cov_m[1,1] = (var_y1 + var_y2)/2
cov_m[0,1] = (co_1 + co_2)/2
cov_m[1,0] =cov_m[0,1]

det = cov_m[0,0] * cov_m[1,1] - cov_m[1,0] * cov_m[0,1]		#determinant of cov_matrix

temp = (cov_m[0,0]/det)							#inverse of cov_matrix
cov_m[0,0] = (cov_m[1,1]/det)
cov_m[1,1] = temp
temp = cov_m[0,1]
cov_m[0,1] = cov_m[1,0] = -1*(temp/det)

mean = numpy.zeros(shape=(2,1))
mean[0,0] = mean_x1 - mean_x2
mean[1,0] = mean_y1 - mean_y2

slope = numpy.zeros(shape=(2,1))
slope[0,0] = cov_m[0,0]*mean[0,0] + cov_m[0,1]*mean[1,0]
slope[1,0] = cov_m[1,0]*mean[0,0] + cov_m[1,1]*mean[1,0]
m = slope[1,0]/slope[0,0]
slope = -1*(1/m)

x0_1 = (mean_x1 + mean_x2)/2
x0_2 = (mean_y1 + mean_y2)/2

c = x0_2 - slope*x0_1

plot1,plot2 = [],[]
for x in range (-10,20):
	plot1.append(x)
	plot2.append(slope*x + c)

plt.plot(plot1, plot2, c = "g")

# var_1 = (var_x1 + var_y1)/2
# var_2 = (var_x2 + var_y2)/2
# var_avg = (var_1 + var_2)/2
# print( "Average var: ",round(var_avg,3))

plt.title('Data from')
plt.xlabel('-----------------------X-----------------------')
plt.ylabel('-----------------------Y-----------------------')

rem(array_x1,array_y1)
rem(array_x2,array_y2)

plt.scatter(array_x1,array_y1,c = 'r')
plt.scatter(array_x2,array_y2,c = 'b')

print("Variance x1: ",round(var_x1,2))
print("Variance y1: ",round(var_y1,2))
print("Variance x2: ",round(var_x2,2))
print("Variance y2: ",round(var_y2,2))

plt.show()
fp1.close()
fp2.close()
