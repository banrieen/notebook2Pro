period=100000
n=$((6*1000000/$period))
i=0
{
while [ $i -lt $n ]
do
d=$(date)
echo $d 1>&2 
top -n 1 |awk -v date="$d" '/Xorg/{print $10";"$13" "date}'
i=$(($i+1))
usleep $period
done 
} | tee >(awk -F\; '{if($1>=max){max=$1;proname=$2}}END{print max";"proname}')
