import subprocess

# Open the input and output files
with open('domains.tsv', 'r') as input_file, open('domains_to_ips.txt', 'w') as output_file:

    # skip header line
    next(input_file)

    # iterate over each line
    for line in input_file:

        # split each line by tabs to seperate each column
        columns = line.strip().split('\t')

        # since the domain is in the second column, we use an index of 1
        domain = columns[1]

        # use the subprocess module to perform a IPv4 and IPv6 dns lookup using the host command
        output = subprocess.check_output(['host','-t', 'A', domain], universal_newlines=True)
        v4 = output.split()[-1]

        output = subprocess.check_output(['host', '-t', 'A', domain], universal_newlines=True)
        v6 = output.split()[-1]
        
        output_file.write(f"{domain}, {v4}, {v6}\n")

