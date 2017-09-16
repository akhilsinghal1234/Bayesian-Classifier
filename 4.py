import sys,numpy,math,time
import matplotlib.pyplot as plt

def mul(X,Y):
	result = numpy.zeros(shape=(2,1))

	for i in range(len(X)):
   		for j in range(len(Y[0])):
   			for k in range(len(Y)):
   				result[i][j] += X[i][k] * Y[k][j]
	return result
def determinant(X):
	return X[0,0] * X[1,1] - X[1,0] * X[0,1]

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
def inverse(X,d):
	temp = (X[0,0]/d)
	X[0,0] = (X[1,1]/d)
	X[1,1] = temp
	temp = (-1*X[0,1])/d
	X[0,1] = X[1,0] = temp
	return X

def transpose(X):
	m = numpy.zeros(shape=(1,2))
	m[0,0] = X[0,0]
	m[0,1] = X[1,0]
	return m

def gx(Wi,wi,x,wi0):
	return mul(transpose(x),mul(Wi,x))[0,0] +  wi[0,0]*x[0] + wi[1,0]*x[1] + wi0

def wi(var,mean):
	return mul(var,mean)

def wi0(var,mean,probability,det):
	return -0.5*mul(transpose(mean),(mul(var,mean)))[0,0] - 0.5*+ probability

def Wi(cov_i):
	return -0.5*cov_i

def find_r(x_data,y_data,n):
	max_x,min_x,max_y,min_y = 0,sys.maxsize,0,sys.maxsize
	range = []
	for k in x_data:
		if(max(k) > max_x):
			max_x = max(k)

		if(min(k) < min_x):
			min_x = min(k) 

	for k in y_data:
		if(max(k) > max_y):
			max_y = max(k)

		if(min(k) < min_y):
			min_y = min(k) 
	range.extend((int(max_x)+1,int(min_x)-1,int(max_y)+1,int(min_y)-1))
	return range

def rem(array1,array2):
	l1 = (int)((len(array1)*3)/4)
	for i in range(0,l1):
		array1.pop(0)
		array2.pop(0)

def cov_mat(varx,vary,co_var):
	cov_m = numpy.zeros(shape=(2,2))
	cov_m[0,0] = varx
	cov_m[1,1] = vary
	cov_m[0,1] = cov_m[1,0] = co_var
	return cov_m

def cov(array1,array2,mean1,mean2):
	co = 0
	for i in range((3*len(array1))//4):					#calculating co-var for files 1 & 2
		co += ((array1[i]-mean1)*(array2[i] - mean2))
	return co/((3*len(array1)//4 ) - 1)

n = 0
files = []
n = int(input("Enter a number: \n"))
number_of_files = n
for x in range(n):
	name = input("Enter file name:\n")
	files.append (name)
mean_x,mean_y,var_x,var_y,x_data,y_data,cov_ = [],[],[],[],[],[],[]

for file in files:
	fp = open(file,"r")
	x,y = [],[]
	for line in fp:
		m,n = line.split()
		x.append((float(m)))
		y.append((float(n)))
	fp.close()
	x_data.append(x)
	y_data.append(y)

for k in x_data:
	mean = 0
	for x in range(3*len(k)//4):
		mean += k[x]
	mean_x.append(mean/(3*len(k)//4))

for k in y_data:
	mean = 0
	for y in range(3*len(k)//4):
		mean += k[y]
	mean_y.append(mean/(3*len(k)//4))
i = 0
for k in x_data:
	var = 0
	for x in range(3*len(k)//4):
		var += math.pow((k[x] - mean_x[i]),2)
	i += 1
	var_x.append(var/(3*len(k)//4))
i = 0
for k in y_data:
	var = 0
	for y in range(3*len(k)//4):
		var += math.pow((k[y] - mean_y[i]),2)
	i += 1
	var_y.append(var/(3*len(k)//4))

for i in range(len(x_data)):
	co = cov(x_data[i],y_data[i],mean_x[i],mean_y[i])
	cov_.append(co)

probability = []
t = 0
for k in x_data:
	t += len(k)

for k in x_data:
	probability.append(math.log(len(k)/t))

r = []
r = find_r(x_data,y_data,number_of_files)

i = 0
x_r,y_r = [],[]
x_r = numpy.linspace(r[1],r[0],100)
y_r = numpy.linspace(r[3],r[2],100)

colors = "gcbwrymk"
conf_matrix = numpy.zeros(shape=(number_of_files,number_of_files))
mean = numpy.zeros(shape=(2,1))

data_x,data_y = [],[]
for i in range(number_of_files):
	x,y = [],[]
	data_x.append(x)
	data_y.append(y)

for i in x_r:
	for j in y_r:
		val = []
		x = numpy.zeros(shape=(2,1))
		x[0,0] = i
		x[1,0] = j
		for k in range(number_of_files):
			mean[0,0] = mean_x[k]
			mean[1,0] = mean_y[k]

			cov = cov_mat(var_x[k],var_y[k],cov_[k])
			cov_i = inverse(cov,determinant(cov))
			val.append(gx(Wi(cov_i),wi(cov_i,mean),x,wi0(cov_i,mean,probability[k],determinant(cov))))
			class_ = val.index(max(val))
			data_x[class_].append(i)
			data_y[class_].append(j)

for i in range(number_of_files):
	plt.scatter(data_x[i],data_y[i],label=files[i],c=colors[i])
plt.legend()
	
for j in range(number_of_files):
	rem(x_data[j],y_data[j])
	plt.scatter(x_data[j],y_data[j],marker='o',c=colors[7-j])

x = numpy.zeros(shape=(2,1))
for i in range(number_of_files):
	for j in range(len(x_data[i])):
		x[0,0] = x_data[i][j]
		x[1,0] = y_data[i][j]
		val = []
		for k in range(number_of_files):
			mean[0,0] = mean_x[k]
			mean[1,0] = mean_y[k]
			cov = cov_mat(var_x[k],var_y[k],cov_[k])
			cov_i = inverse(cov,determinant(cov))
			val.append(gx(Wi(cov_i),wi(cov_i,mean),x,wi0(cov_i,mean,probability[k],determinant(cov))))
		class_ = val.index(max(val))
		conf_matrix[i,class_] += 1

print("Confusion Matrix for all classes:\n",conf_matrix)
recall,precision= [],[]
mean_re,mean_pre,accuracy = 0,0,0
for i in range(number_of_files):				#recall
	temp = 0
	print("Recall for class:",files[i])
	for j in range(number_of_files):
		temp += conf_matrix[j][i]
	print(round (conf_matrix[i][i]/temp,3))
	recall.append(conf_matrix[i][i] / temp)
	mean_re += conf_matrix[i][i] / temp

mean_re = mean_re/number_of_files
for i in range(number_of_files):				#precision
	temp = 0
	print("Precision for class:",files[i])
	for j in range(number_of_files):
		temp += conf_matrix[i][j]
	print(round (conf_matrix[i][i]/temp,3))
	precision.append(conf_matrix[i][i] / temp)
	mean_pre += conf_matrix[i][i] / temp
mean_pre = mean_pre/number_of_files

f_measure = 0
for i in range(number_of_files):
	if(precision[i] and recall[i] != 0):
		f_measure += round(2*precision[i]*recall[i]/(precision[i]+recall[i]),3)
		print("F-measure for:",files[i],"\n",round(2*precision[i]*recall[i]/(precision[i]+recall[i]),3))
total = 0
for i in range(number_of_files):				#accuracy
	accuracy += conf_matrix[i][i]
	total += len(x_data[i])
accuracy = accuracy/(total)
print("Accuracy of classification:",round(accuracy,3))
print("Mean recall:",round(mean_re,3))
print("Mean precision:",round(mean_pre,3))
print("Mean F-measure:",round((f_measure/number_of_files),3))
name = ""
for file in files:
	name_i = file
	name_i = name_i[:-4]
	name += name_i
# print(name)
plt.savefig("Output/4/"+ str(4) + name + ".png")
# plt.show()
