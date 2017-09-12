import sys
import math,time
import matplotlib.pyplot as plt

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

plt.title('Data from')
plt.xlabel('-----------------------X-----------------------')
plt.ylabel('-----------------------Y-----------------------')
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.scatter(array_x1,array_y1,c = 'r')
plt.scatter(array_x2,array_y2,c = 'b')


mean_x1,mean_y1,mean_x2,mean_y2 = 0,0,0,0


for x in range((3*len(array_x1))//4):					#calculating mean for x & y
	mean_x1 += array_x1[x];
for y in range((3*len(array_y1))//4):
	mean_y1 += array_y1[y]
for x in range((3*len(array_x2))//4):
	mean_x2 += array_x2[x]
for y in range((3*len(array_y2))//4):
	mean_y2 += array_y2[y]

mean_x1 = float(mean_x1/((3*len(array_x1))//4))
mean_y1 = float(mean_y1/((3*len(array_y1))//4))
mean_x2 = float(mean_x2/((3*len(array_x2))//4))
mean_y2 = float(mean_y2/((3*len(array_y2))//4))
print("Mean x for 1: ",round(mean_x1,3))
print("Mean y for 1:",round(mean_y1,3))
print("Mean x for 2: ",round(mean_x2,3))
print("Mean y for 2:",round(mean_y2,3),"\n")

var_x1,var_x2,var_y1,var_y2 = 0, 0 , 0 , 0

for x in range((3*len(array_x1))//4):					#calculating variance for x and y
	var_x1 += math.pow((array_x1[x]-mean_x1),2)
for y in range((3*len(array_y1))//4):
	var_y1 += math.pow((array_y1[x]-mean_y1),2)
for x in range((3*len(array_x2))//4):
	var_x2 += math.pow((array_x2[x]-mean_x2),2)
for y in range((3*len(array_y2))//4):
	var_y2 += math.pow((array_y2[x]-mean_y2),2)

co_1,co_2 = 0,0

for i in range((3*len(array_x1))//4):					#calculating co-var for files 1 & 2
	co_1 += ((array_x1[i]-mean_x1)*(array_y1[i] - mean_y1))

co_1 = co_1/((3*len(array_x1)//4 ) - 1)

for i in range((3*len(array_x2))//4):
	co_2 += ((array_x2[i]-mean_x2)*(array_y2[i] - mean_y2))

co_2 = co_2/((3*len(array_x2)//4 ) - 1)

var_x1 = float(var_x1/((3*len(array_x1))//4))
var_y1 = float(var_y1/((3*len(array_y1))//4))
var_x2 = float(var_x2/((3*len(array_x2))//4))
var_y2 = float(var_y2/((3*len(array_y2))//4))

print("Variance x1: ",round(var_x1,2))
print("Variance y1: ",round(var_y1,2))
print("Variance x2: ",round(var_x2,2))
print("Variance y2: ",round(var_y2,2))
print("Co-Var(1): ",round(co_1,2))
print("Co-Var(2): ",round(co_2,2))
plt.show()
fp1.close()
fp2.close()
