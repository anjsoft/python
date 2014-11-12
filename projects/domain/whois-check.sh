echo 'start'
for name in $(cat 2-nums-dict.txt)
do
echo $name.com
sleep 5
whois $name.com|cat|grep 'No match'>>ok-domain.txt
done 
