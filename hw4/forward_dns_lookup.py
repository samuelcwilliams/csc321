import subprocess

# open input and output files
with open('domains.tsv', 'r') as input_file, open('domains_to_ips.tsv', 'w') as output_file:

    # skip header line
    next(input_file)

    # iterate over each line
    for line in input_file:

        # split each line by tabs to seperate each column
        columns = line.strip().split('\t')

        # since the domain is in the second column, we use an index of 1
        domain = columns[1]

        # use the subprocess module to perform a IPv4 and IPv6 DNS lookup using the host command
        try:
            output = subprocess.check_output(['host','-t', 'A', domain], universal_newlines=True)
            v4 = output.split()[-1]
        except:
            pass

        try:
            output = subprocess.check_output(['host', '-t', 'AAAA', domain], universal_newlines=True)
            v6 = output.split()[-1]
        except:
            pass
        
        output_file.write(f"{domain}    {v4}  {v6}\n")

