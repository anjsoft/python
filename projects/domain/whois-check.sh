echo 'start'
for name in $(cat 4-nums-dict.txt)
do
echo $name.com
sleep 1
whois $name.com|cat|grep 'No match'>>ok-domain.txt
sed -i -e "1d" 4-nums-dict.txt
done 
