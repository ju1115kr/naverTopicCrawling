#!/usr/bin/expect

set date [exec date]
set today [exec date +%y%m%d]
cd /home/ubuntu/topic
exec python3 /home/ubuntu/topic\ crowing.py >> /home/ubuntu/topic/$today
exec git add .
exec git commit -m $date
spawn git push origin
sleep 3
expect "password: "
send "dlwndud001!\n"
#interact
expect eof
exit
