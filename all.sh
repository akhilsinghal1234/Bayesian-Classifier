#! /bin/sh
dirname="Output"
rm -f -r ${dirname}
mkdir -p -- ${dirname}
dirname="input"
rm -f -r ${dirname}
mkdir -p -- ${dirname}
# input_name
prefix="$dirname/in_"
postfix=".in"
for number in 1 2 3;do
if [ $number = 1 ]; then
	echo "$number\nClass1.txt" > $prefix$number'_1'$postfix
	echo "$number\nClass2.txt" > $prefix$number'_2'$postfix
	echo "$number\nClass3.txt" > $prefix$number'_3'$postfix
elif [ $number = 2 ]; then 
	echo "$number\nClass1.txt\nClass2.txt" > $prefix$number'_12'$postfix
	echo "$number\nClass1.txt\nClass3.txt" > $prefix$number'_13'$postfix
	echo "$number\nClass2.txt\nClass3.txt" > $prefix$number'_23'$postfix
elif [ $number = 3 ]; then 
	echo "$number\nClass1.txt\nClass2.txt\nClass3.txt" > $prefix$number'_123'$postfix
 fi;done

postfix1=".py"
for number in 1 2 3 4;do
python "$number$postfix1" < $prefix'1_1'$postfix
python "$number$postfix1" < $prefix'1_2'$postfix
python "$number$postfix1" < $prefix'1_3'$postfix
python "$number$postfix1" < $prefix'2_12'$postfix
python "$number$postfix1" < $prefix'2_13'$postfix
python "$number$postfix1" < $prefix'2_23'$postfix
python "$number$postfix1" < $prefix'3_123'$postfix
done