import subprocess, tldextract

# open input/output file
with open('domain_to_ip.tsv', 'r') as input_file, open('ip_to_domain.tsv', 'w') as output_file:

    # iterate over file
    for line in input_file:

        # split into columns and pull out IP addresses
        columns = line.strip().split('\t')
        addresses = columns[1]
        address_list = addresses.split()

        unvalidated = ""
        test = []

        # iterate over addresses returned for each specific domain given initally in domains.tsv
        for address in address_list:
            raw = subprocess.run(['host', '-t', 'PTR', address], capture_output=True, text=True)
            test.append(raw.stdout.strip().split()[-1])

        # split into list and iterate over list to make sure there are only valid domains present
        print(test)
        validated = ''
        for string in test:
            # using tldextracts registered_domain function to make sure what was returned is a valid domain
            valid = tldextract.extract(string).registered_domain
            print(valid)
            if valid:
                validated = validated + valid + ' '

        # write to output file
        output_file.write(f'{columns[0]}\t{addresses}\t{validated}\n')
