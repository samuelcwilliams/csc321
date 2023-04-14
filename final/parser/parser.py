from scapy.all import *

# read pcap file
full_take = rdpcap("full-take.pcap")

# initialize weather.pcap and task.pcap
weather = PcapWriter("weather.pcap", append=True)
task = PcapWriter("task.pcap", append=True)

# loop through each packer in full_take
for packet in full_take:
    # get timestamp
    timestamp = packet.time

    # add packets to file based on time
    if timestamp < 1681180240:
        weather.write(packet)
    else:
        task.write(packet)

# close the weather and task files
weather.close()
task.close()
