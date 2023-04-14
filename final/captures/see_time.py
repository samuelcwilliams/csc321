from scapy.all import *

"""
I wrote this program as an easy way to get the highest packet timestamp (aka the
newest) in a given file. Use it by specifying a filename and it will print the 
highest timestamp in UNIX time. 
"""

# read pcap file
toread = input("File name: ")
packets = rdpcap(toread)

# find the newest packet
newest_packet = max(packets, key=lambda p: p.time)

# print the timestamp of the newest packet in Unix time format
print(int(newest_packet.time))
