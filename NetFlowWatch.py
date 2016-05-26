#!/usr/bin/python
# Filename: NetFlowWatch.py
# Version: 0.0.1
# Author: shinukami
# Date: 2016-4-7

from os import listdir
from os import system
from time import sleep

Path = "/sys/class/net/"
Devs = listdir(Path)

def Watch(Dev,timeout):
    Dev_files = ["rx_packets","tx_packets","rx_bytes","tx_bytes"]

    Files = [ open(Path+Dev+"/statistics/"+i) for i in Dev_files ]
    Data1 = [ int(i.read()) for i in Files ]

    for i in Files: i.close()

    sleep(timeout)

    # System platform Change Here
    system("clear")
    # System platform Change Here

    Files = [ open(Path+Dev+"/statistics/"+i) for i in Dev_files ]
    Data2 = [ int(i.read()) for i in Files ]

    for i in Files: i.close()

    print "Device :",Dev
    print "Recive Pkts : ",(Data2[0]-Data1[0])/timeout,"p/s"
    print "Recive Byts : ",(Data2[2]-Data1[2])/timeout,"b/s"
    print "Transp Pkts : ",(Data2[1]-Data1[1])/timeout,"p/s"
    print "Transp Byts : ",(Data2[3]-Data1[3])/timeout,"b/s"


while True:
    Watch("wlp2s0",3)

