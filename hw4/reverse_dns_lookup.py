import subprocess

# open input and output files
with open('domains_to_ips.csv', 'r') as input_file, open('ips_to_domains.csv', 'w') as output_file:

    # iterate over each line
    for line in input_file:

        # split each line using tabs as a separator
        columns = line.strip().split(',')

        # split the values in the second column 
        addresses = columns[0].split()

        # use the subprocess module to perform reverse DNS lookup using the hosts module
        domain = ""
        try:
            for ip in addresses:
                output = subprocess.check_output(['host','-t', 'PTR', ip], universal_newlines=True)
                domain += output.split()[-1]
        except:
            pass

        # write the output domain/addresses to the output file
        output_file.write(f"{ip},{domain}\n")
