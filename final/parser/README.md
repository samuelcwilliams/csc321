## `full-take.pcap` parser

After comparing the different files, I realized the easiest way to sort them would be by their timestamp, as they were not run at the same time. 

### Program Logic
* Read `full-take.pcap`
* Iterate over each packet
	* If timestamp is before `1681180237`, add to `weather.pcap`
		* To find that specific time, I wrote the `see_time` program that is in the captures directory.
	* Else, add to `task.pcap`
* Return `weather.pcap` and `task.pcap`

