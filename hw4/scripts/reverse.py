import subprocess, tldextract

# open input/output file
with open('../tsv_files/domain_to_ip.tsv', 'r') as input_file, open('../tsv_files/ip_to_domain.tsv', 'w') as output_file:
    output_file.write(f'original_domain\taddresses\tnew_domains\n')

    # iterate over file
    for line in input_file:

        # split into columns and pull out IP addresses
        columns = line.strip().split('\t')
        address = columns[1]

        # run lookup and capture output 
        raw = subprocess.run(['host', '-t', 'PTR', address], capture_output=True, text=True)
        domain = raw.stdout.strip().split()[-1]

        # verify that domain is valid using tldextract's registered_domain functon
        domain = tldextract.extract(domain).registered_domain
        if domain:
            # write to output file
            output_file.write(f'{columns[0]}\t{address}\t{domain}\n')
        
