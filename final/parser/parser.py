from scapy.all import *

# read pcap file
full_take = rdpcap("full-take.pcap")

# initialize weather.pcap and task.pcap
weather = []
task = []

# loop through each packer in full_take
for packet in full_take:
    # get timestamp
    timestamp = packet.time

    # add packets to file based on time
    if timestamp < 1681180240:
        weather.append(packet)
    else:
        task.append(packet)

# write to weather.pcap and task.pcap
wrpcap("weather.pcap", weather)
wrpcap("task.pcap", task)
