#! /bin/sh
clear
echo "                                                ##########################################
                                                # Version :: 1.01                        #
                                                # Scripts all the possible input and     #
                                                # redirects to output folder 1 2 3 4	 #
                                                # Group :: 1                             #
                                                ##########################################"

dirname="Output"
echo "\nMaking Output Directory.\n"
rm -f -r ${dirname}
mkdir -p -- ${dirname}
cd ${dirname}
for number in 1 2 3 4;do
mkdir -p -- "$number"
done 
cd ..
echo "Generating All Posible Input cases .\n"
dirname="input"
rm -f -r ${dirname}
mkdir -p -- ${dirname}
# input_name
prefix="$dirname/in_"
postfix=".in"
for number in 1 2 3;do
# if [ $number = 1 ]; then
# 	echo "$number\nClass1.txt" > $prefix$number'_1'$postfix
# 	echo "$number\nClass2.txt" > $prefix$number'_2'$postfix
# 	echo "$number\nClass3.txt" > $prefix$number'_3'$postfix
if [ $number = 2 ]; then 
	echo "$number\nClass1.txt\nClass2.txt" > $prefix$number'_12'$postfix
	echo "$number\nClass1.txt\nClass3.txt" > $prefix$number'_13'$postfix
	echo "$number\nClass2.txt\nClass3.txt" > $prefix$number'_23'$postfix
elif [ $number = 3 ]; then 
	echo "$number\nClass1.txt\nClass2.txt\nClass3.txt" > $prefix$number'_123'$postfix
 fi;done

postfix1=".py"
for number in 1 2 3 4;do
echo "Running Program For Case $number.\n"
python "$number$postfix1" < $prefix'2_12'$postfix > temp.txt
python "$number$postfix1" < $prefix'2_13'$postfix > temp.txt
python "$number$postfix1" < $prefix'2_23'$postfix > temp.txt
python "$number$postfix1" < $prefix'3_123'$postfix > temp.txt
echo "Completed Program For Case $number.\n"
done
echo "Program Completed !\n\nPlease check the Output Directory!\n"