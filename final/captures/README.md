## `full-take.pcap` parser

After looking at captures from each of the individual assignments, I think I've figured out a really simple way to parse them into individual `weather.pcap` and `task.pcap` files: their timestamps. Since they weren't run at the same time, it's very easy to distinguish between the two just by looking at the times. So, I'm going to write a script using Python's `scapy` library to work with the data in`full-take.pcap`. 

### Program Logic
* Read `full-take.pcap`
* Iterate over each packet
	* If timestamp is before 21:35, add to `weather.pcap`
	* Else, add to `task.pcap`
* Return `weather.pcap` and `task.pcap`
