import subprocess, ipaddress

# open input/output file
with open('../tsv_files/domains.tsv', 'r') as input_file, open('../tsv_files/domain_to_ip.tsv', 'w') as output_file:

    # skip header
    next(input_file)

    # iterate over file
    for line in input_file:

        # split into columns and pull out domain name
        columns = line.strip().split('\t')
        domain = columns[1]

        # perform dns lookup using host
        v4 = subprocess.run(['host', '-t', 'A', domain], capture_output=True, text=True)
        v6 = subprocess.run(['host', '-t', 'AAAA', domain], capture_output=True, text=True)

        # extract addresses and split into list for address validation
        unvalidated = v4.stdout.strip().split()[-1] + ' ' + v6.stdout.strip().split()[-1]
        unvalidated = unvalidated.split()

        addresses = ""

        # validation to confirm they are addresses. (created to deal with the "record" issue)
        for string in unvalidated:
            try:
                ip_address = ipaddress.ip_address(string)
            except ValueError:
                continue

            # add the validated address
            addresses =  str(ip_address)

            # write to output file
            output_file.write(f'{domain}\t{addresses}\n')

        
