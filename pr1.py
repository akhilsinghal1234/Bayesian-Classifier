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

for x in array_x1:
	mean_x1 += x
for y in array_y1:
	mean_y1 += y
for x in array_x2:
	mean_x2 += x
for y in array_y2:
	mean_y2 += y
mean_x1 = float(mean_x1/len(array_x1))
mean_y1 = (float)(mean_y1/len(array_y1))
mean_x2 = float(mean_x2/len(array_x2))
mean_y2 = (float)(mean_y2/len(array_y2))
print("Mean x for 1: ",round(mean_x1,3))
print("Mean y for 1:",round(mean_y1,3))
print("Mean x for 2: ",round(mean_x2,3))
print("Mean y for 2:",round(mean_y2,3),"\n")
time.sleep(2)

# variance = 0
# for x in array:
# 	variance += math.pow((x-mean),2)
# variance = variance/(len(array)-1)
# print("Variance of elements in array: ",round(variance,5))
# std_dev = math.pow(variance,0.5)
# print("Standard Deviation of elements in array: ",round(std_dev,5))
plt.show()
fp1.close()
fp2.close()