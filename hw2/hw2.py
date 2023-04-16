import netifaces, ipaddress


def get_interfaces():
    """
    Return a list of all the interfaces on this host
    Home Network: ['lo', 'wlp0s20f3']
    Belhaven Network: 
    """

    interfaces = netifaces.interfaces()
    return interfaces

def get_mac(interface: str):
    """
    For the given interface string, return the MAC address as a 
    string
    Home Network:
    Belhaven Network: 00:00:00:00:00:00, 20:1e:88:d2:d8:4f
    """

    address = netifaces.ifaddresses(interface)
    return address[netifaces.AF_LINK][0]['addr']

def get_ips(interface: str):
    """
    For the given interface string, return a dict with the IPv4/6
    address objects for that interface.
    Home Network:
    Belhaven Network:
    """

    

def get_netmask(interface: str):
    """
    For the given interface string, return a dict with the IPv4/6 netmask
    objects (as IPv4/6 address objects) for that interface
    Home Network:
    Belhaven Network:
    """

    pass

def get_network(interface: str):
    """
    For the given interface string, return a dict with the IPv4/6 network
    objects for that interface.
    Home Network:
    Belhaven Network:
    """

    pass

if __name__ == "__main__":
    interfaces = get_interfaces()
    for interface in interfaces:
        get_mac(interface)
