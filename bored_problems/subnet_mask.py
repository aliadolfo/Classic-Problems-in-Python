from netaddr import *

# IPv4 Address to Binary
# IPv4 uses 32 binary bits to create a single unique address on the network

ip_address = '192.168.1.10'
ipBynary_address = '11000000101010000000000100001010'

# format '08b'
# 'b' Binary format. Outputs the number in base 2.
# '0' It is the character that is placed in place of the empty spaces
def ip4_to_binary(ip):
    octet_list = ip.split(".")
    octet_bin = [format(int(item), '08b') for item in octet_list]
    binary_ip_address = ("").join(octet_bin)
    return binary_ip_address

def ipv4_binary_to_int(ip_array):
    
    binary_ip = []

    split_in = 8
    for index in range(0, len(ip_array), split_in):
        binary_ip.append(ip_array[index : index + split_in ])

    return binary_ip

m_netmask = "11000000.10101000.00000001.00001010"
def netmask_to_cidr(m_netmask):
  return(sum([ bin(int(bits)).count("1") for bits in m_netmask.split(".") ]))
   
    


if '__main__'==__name__:
    print(">>>>>>>>>>>>>>>>> ", ip4_to_binary(ip_address))
    print("# size of binary ip : $ ", len(ip4_to_binary(ip_address)))
    print("Binary to int > : ", ipv4_binary_to_int(ipBynary_address))
    print("Binary len : ", len(ipv4_binary_to_int(ipBynary_address)))
    print("netmask >>> : ", netmask_to_cidr(m_netmask))
    
