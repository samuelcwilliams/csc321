import subprocess

# open input and output files
with open('domains_to_ips.csv', 'r') as input_file, open('ips_to_domains.csv', 'w') as output_file:

    # iterate over each line
    for line in input_file:
        # split each line using commas as a separator
        columns = line.split(',')

        # split the values in the second column 
        addresses = columns[1].split()

        domain = ""
        try:
            # iterate over each ip in our addresses list
            for ip in addresses:
                # use the subprocess module to perform reverse DNS lookup using the hosts module
                output = subprocess.check_output(['host','-t', 'PTR', ip], universal_newlines=True)

                # string formatting
                domain += " " + output.split()[-1]
                domain = domain.rstrip(".")

                # write the output domain/addresses to the output file
                output_file.write(f"{ip},{domain}\n")
        except:
            pass
