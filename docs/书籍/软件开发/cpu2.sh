period=100000
n=$((1000000/$period))
i=0
max=0
while [ $i -lt $n ]
do
echo 1
eval $(top -n 1 |awk '/Xorg/{print "if (($max<="$10*10"));then max="$10*10";pro="$13";d=$(date);fi"}')
i=$(($i+1))
usleep $period
done 
echo "$(echo "scale=1;$max"'/10' |bc );$pro;$d"
