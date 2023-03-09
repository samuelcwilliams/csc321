import netifaces as nf
import ipaddress as ip

def get_interfaces():
    """Return a list of all the interfaces on this host

    Args: None

    Returns: (list) List of interfaces for this host
    
    Home:     ['lo', 'wlp0s20f3']
    Belhaven: ['lo', 'wlp0s20f3']
    """
    return print(nf.interfaces(), '\n')

def get_mac():

    """For the given interface string, return the MAC address as a string

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (str) MAC address

    Home:     00:00:00:00:00:00, 20:1e:88:d2:d8:4f
    Belhaven: 00:00:00:00:00:00, 20:1e:88:d2:d8:4f
    """

    ifs = nf.interfaces()
    macs = ''

    for i in ifs:
        address = nf.ifaddresses(i)
        print(address[nf.AF_LINK][0]['addr'])
    print('\n')

def get_ips():
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 address objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('192.168.65.48'),
       'v6': ipaddress.IPv6Address('fe80::14e1:8686:e720:57a')}

    Home:     {'v4-0': IPv4Address('127.0.0.1'), 'v4-1': IPv4Address('192.168.40.144')}
    Belhaven: {'v4-0': IPv4Address('127.0.0.1'), 'v4-1': IPv4Address('192.168.181.0')}
    """

    ifs = nf.interfaces()
    dict = {}
    v4_counter = 0
    v6_counter = 0

    for i in ifs:
        address = nf.ifaddresses(i)
        for i in address[nf.AF_INET]:
            ip_add = ip.ip_address(i['addr'])
            if ip_add.version == 4:
                dict[f'v4-{v4_counter}'] = ip.ip_address(i['addr'])
                v4_counter += 1
            else:
                dict[f'v6-{v6_counter}'] = ip.ip_address(i['addr'])
                v6_counter += 1
    return print(dict)

def get_netmask():
    """For the given interface string, return a dictionary with the
    IPv4 and IPv6 netmask objects (as IPv4/v6Address objects) for that
    interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('255.255.255.0'),
       'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')}

    Home:     {'v4-0': IPv4Address('255.0.0.0'), 'v4-1': IPv4Address('255.255.255.0')}
    Belhaven: {'v4-0': IPv4Address('255.0.0.0'), 'v4-1': IPv4Address('255.255.240.0')}
    """

    ifs = nf.interfaces()
    dict = {}
    v4_counter = 0
    v6_counter = 0

    for i in ifs:
        address = nf.ifaddresses(i)
        for i in address[nf.AF_INET]:
            nm_add = ip.ip_address(i['netmask'])
            if nm_add.version == 4:
                dict[f'v4-{v4_counter}'] = nm_add
                v4_counter += 1
            else:
                dict[f'v6-{v6_counter}'] = nm_add
                v6_counter += 1

    return print(dict)

def get_network():
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 network objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Network('192.168.65.0/24'),
       'v6': ipaddress.IPv6Network('fe80::/64')}

    Home:     {'v4-0': IPv4Network('127.0.0.1/32'), 'v4-1': IPv4Network('192.168.40.144/32')}
    Belhaven: {'v4-0': IPv4Network('127.0.0.1/32'), 'v4-1': IPv4Network('192.168.181.0/32')}
    """

    ifs = nf.interfaces()
    dict = {}
    v4_counter = 0
    v6_counter = 0

    for i in ifs:
        address = nf.ifaddresses(i)
        for i in address[nf.AF_INET]:
            nw = ip.ip_network(i['addr'], strict=False)
            if nw.version == 4:
                dict[f'v4-{v4_counter}'] = nw
                v4_counter += 1
            else:
                dict[f'v6-{v6_counter}'] = nw
                v6_counter += 1
    
    return print(dict)

if __name__ == "__main__":
    get_interfaces()
    get_mac()
    get_ips()
    get_netmask()
    get_network()