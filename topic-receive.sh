#!/usr/bin/expect

if {[file exist "/tmp/topic"]} {
    cd /tmp/topic
    spawn git pull
    sleep 3
    expect "password: "
    send "dlwndud001!\n"
    expect eof
    exit
} else {
    spawn git clone git@10.30.10.8:/home/ubuntu/topic.git
    sleep 3
    expect "(yes/no)? "
    send "yes\n"
    expect "password: "
    send "dlwndud001!\n"
    expect eof
    exit
}
