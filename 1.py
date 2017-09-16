import sys,numpy,math,time
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

class param(object):
	def __init__(self,wi,wi0)	:
		self.wi = wi
		self.wi0 = wi0

def mag(X):
	return (math.pow(X[0,0],2) + math.pow(X[1,0],2))

def gx(wi,x,wi0):
	return wi[0,0]*x[0] + wi[1,0]*x[1] + wi0

def wi(var,mean):
	return mean / var

def wi0(var,mean,probability):
	return -0.5*(mag(mean)/var) + probability

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

def max_val(val):
	return val.index(max(val))

n = 0
files = []
n = int(input("Enter a number: \n"))
number_of_files = n
for x in range(n):
	name = input("Enter file name:\n")
	files.append (name)
mean_x = []
mean_y = []
var_x,var_y = [],[]
x_data = []
y_data = []
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

v,i = 0,0
for k in x_data:
	var = 0
	for x in range(3*len(k)//4):
		var += math.pow((k[x] - mean_x[i]),2)
	i += 1
	v += var/(3*len(k)//4)
	var_x.append(var/(3*len(k)//4))
i = 0
for k in y_data:
	var = 0
	for y in range(3*len(k)//4):
		var += math.pow((k[y] - mean_y[i]),2)
	i += 1
	v += var/(3*len(k)//4)
	var_y.append(var/(3*len(k)//4))

var_av = v/4

probability = []
t = 0
for k in x_data:
	t += len(k)

for k in x_data:
	probability.append(math.log(len(k)/t))

r = []
r = find_r(x_data,y_data,number_of_files)
mean = numpy.zeros(shape=(2,1))
conf_matrix = numpy.zeros(shape=(number_of_files,number_of_files))
parameters = []
for k in range(number_of_files):
	mean[0,0] = mean_x[k]
	mean[1,0] = mean_y[k]
	parameters.append(param(wi(var_av,mean),wi0(var_av,mean,probability[k])))

x_r = numpy.linspace(r[1],r[0],100)
y_r = numpy.linspace(r[3],r[2],100)

max_r = 0
for i in range(len(r)):
	if(abs(r[i]) > max_r):
		max_r = abs(r[i])

Z = numpy.zeros(shape=(2*max_r,2*max_r))
min_r = -1*max_r

colors = "bygcwrmk"
color = "wcym"

for i in range(min_r,max_r):
	for j in range(min_r,max_r):
		val,x = [],[]
		x.append(i)
		x.append(j)
		for k in range(number_of_files):
			mean[0,0] = mean_x[k]
			mean[1,0] = mean_y[k]
			val.append(gx(parameters[k].wi,x,parameters[k].wi0))
		Z[i+max_r][j+max_r] = max(val)

X,Y = [],[]
for i in range(min_r,max_r):
	X.append(i)
	Y.append(i)
fig1.suptitle('Filled contour plot', fontsize=20)

cp = ax1.contourf(X, Y, Z)
fig1.colorbar(cp)

for i in range(number_of_files):
	ax1.scatter(x_data[i],y_data[i],label=files[i],c=color[i])
ax1.legend()

data_x,data_y = [],[]
for i in range(number_of_files):
	x,y = [],[]
	data_x.append(x)
	data_y.append(y)
for i in x_r:
	for j in y_r:
		val,x = [],[]
		x.append(i)
		x.append(j)
		for k in range(number_of_files):
			mean[0,0] = mean_x[k]
			mean[1,0] = mean_y[k]
			val.append(gx(parameters[k].wi,x,parameters[k].wi0))
			class_ = val.index(max(val))
			data_x[class_].append(i)
			data_y[class_].append(j)

for i in range(number_of_files):
	ax2.scatter(data_x[i],data_y[i],label=files[i],c=colors[i])
plt.legend()

for j in range(number_of_files):
	val,x = [],[]
	name = files[j]
	rem(x_data[j],y_data[j])	
	ax2.scatter(x_data[j],y_data[j],label=name,marker='o',c=colors[7-j])

for i in range(number_of_files):
	for j in range(len(x_data[i])):
		x = []
		x.append(x_data[i][j])
		x.append(y_data[i][j])
		val = []
		for t in range(number_of_files):
			mean[0,0] = mean_x[t]
			mean[1,0] = mean_y[t]
			val.append(gx(parameters[t].wi,x,parameters[t].wi0))
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
fig2.savefig("Output/1/" +  str(1)  + name + ".png")
fig1.savefig("Output/1/" +  str(1) + "contour" + name + ".png")

