## Forward and Reverse DNS Lookup

### Output Format 
For this script, I originally wanted for the output `.tsv` file to have the domain and then the corresponding addresses found for it, all in one row. However, I realized this would probably make it a little more difficult to visualize, so I abandoned that idea (the original code for that can be seen in the `/old` directory). What I settled on, was having a new column for each address that was returned for a given domain. For example, that's why google.com has two entries in the `domain_to_ip.tsv` file.
