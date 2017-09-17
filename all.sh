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
mkdir -p -- "linear"
cd "linear"
for number in 1 2 3 4;do
mkdir -p -- "$number"
done 
cd ..
mkdir -p -- "non_linear"
cd "non_linear"
for number in 1 2 3 4;do
mkdir -p -- "$number"
done 
cd ..
cd ..

echo "Generating All Posible Input cases .\n"
dirname="input"
rm -f -r ${dirname}
mkdir -p -- ${dirname}
cd ${dirname}
mkdir -p -- "linear"
mkdir -p -- "non_linear"
cd ..

# input_name for linear !
prefix="$dirname/linear/in_"
postfix=".in"
for number in 1 2 3;do
if [ $number = 2 ]; then 
	echo "$number\nClass1_l.txt\nClass2_l.txt\nOutput/linear" > $prefix$number'_12'$postfix
	echo "$number\nClass1_l.txt\nClass3_l.txt\nOutput/linear" > $prefix$number'_13'$postfix
	echo "$number\nClass2_l.txt\nClass3_l.txt\nOutput/linear" > $prefix$number'_23'$postfix
elif [ $number = 3 ]; then 
	echo "$number\nClass1_l.txt\nClass2_l.txt\nClass3_l.txt\nOutput/linear" > $prefix$number'_123'$postfix
 fi;done

# input_name for Non - linear !
 prefix="$dirname/non_linear/in_"
postfix=".in"
for number in 1 2 3;do
if [ $number = 2 ]; then 
	echo "$number\nClass1_nl.txt\nClass2_nl.txt\nOutput/non_linear" > $prefix$number'_12'$postfix
	echo "$number\nClass1_nl.txt\nClass3_nl.txt\nOutput/non_linear" > $prefix$number'_13'$postfix
	echo "$number\nClass2_nl.txt\nClass3_nl.txt\nOutput/non_linear" > $prefix$number'_23'$postfix
elif [ $number = 3 ]; then 
	echo "$number\nClass1_nl.txt\nClass2_nl.txt\nClass3_nl.txt\nOutput/non_linear" > $prefix$number'_123'$postfix
 fi;done

echo "                                            ---------------LINEAR CASE ------------"
postfix1=".py"
prefix="$dirname/linear/in_"
for number in 1 2 3 4;do
echo "Running Program For Case $number.\n"
python "$number$postfix1" < $prefix'2_12'$postfix >"Output/linear/$number/Linear_$number.dat"
python "$number$postfix1" < $prefix'2_13'$postfix >"Output/linear/$number/Linear_$number.dat"
python "$number$postfix1" < $prefix'2_23'$postfix >"Output/linear/$number/Linear_$number.dat"
python "$number$postfix1" < $prefix'3_123'$postfix >"Output/linear/$number/Linear_$number.dat"
echo "Completed Program For Case $number.\n"
done
echo "Program Completed For Linear Case"

echo "                                            ------------ NON-LINEAR CASE -----------"
prefix="$dirname/non_linear/in_"
for number in 1 2 3 4;do
echo "Running Program For Case $number.\n"
python "$number$postfix1" < $prefix'2_12'$postfix >"Output/non_linear/$number/Non_Linear_$number.dat"
python "$number$postfix1" < $prefix'2_13'$postfix >"Output/non_linear/$number/Non_Linear_$number.dat"
python "$number$postfix1" < $prefix'2_23'$postfix >"Output/non_linear/$number/Non_Linear_$number.dat"
python "$number$postfix1" < $prefix'3_123'$postfix >"Output/non_linear/$number/Non_Linear_$number.dat"
echo "Completed Program For Case $number.\n"
done
echo "Program Completed For Non Linear Case"

echo "Program Completed !\n\nPlease check the Output Directory!\n"