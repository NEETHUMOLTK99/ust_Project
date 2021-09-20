import os



# Assign ip address
def ip_cmnd():
    
    ip = input('Enter ip address to add on interface : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose interface: ")
        command = f'sudo ip address add {ip} dev {interface_choice}'
        res = os.popen(command).read()
        print('Ip address assigned successfully')


 # Delete Ip address
 
def ip_cmnd_del():
   
    ip = input('Enter ip address to delete from interface : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose interfaces: ")
        command = f'sudo ip address del {ip} dev {interface_choice}'
        res = os.popen(command).read()
        print("ip adress deleted successfully")
        
        
        
 #show ip address
        
def ip_cmnd_display():
    
    command = f'ip -c -br address'
    res = os.popen(command).read()
    print(res)

def display_all_interface():
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    command = 'ip l'
    res = os.popen(command).read()
    print(f'sudo All interfaces name  => {interfaces}  Details => {res}')


def configure_routing():
    network_addr = input('Enter network Address with /mask : ')
    getway_ip = input('Enter Gateway ip address : ')
    if len(network_addr.split('.')) == 4 and len(getway_ip.split('.')) == 4:
        cmd = f'sudo ip r add {network_addr} via {getway_ip}'
        res = os.popen(cmd).read()
        print(res)
        print('Roting configuration completed !')



def on_off_interface():
    print('1.Turned off interface ')
    print('2.Turned on interface')
    choice = int(input("enter your choice: "))
    
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    print(interfaces)
    interface_choice = input("Enter your choice: ")
    
    if choice == 1:

        cmd = f'ip link set dev {interface_choice}  down'
        res = os.popen(cmd).read()
        print(f'{interface_choice} turned off  | Details => {res}')

    elif choice == 2:
        cmd = f'ip link set dev {interface_choice}  up'
        res = os.popen(cmd).read()
        print(f'{interface_choice} turned on | Details => {res} ')

    else:
        print('Wrong option choosed')


def add_ARP_entry():
    ip = input('Enter ip address  : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose interfaces: ") 
        arp_cache = os.popen('ip n show | cut -d " " -f5').read()
        cmd = f'sudo ip n add {ip} lladdr {arp_cache} dev {interface_choice} nud permanent'
        res = os.popen(cmd).read()
        print('ARP Entry added successfully ')


def del_arp_entry():
    ip = input('Enter ip address : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        print(interfaces)
        interface_choice = input("choose interfaces: ")
        cmd = f'sudo ip n del {ip} dev {interface_choice}'
        res = os.popen(cmd).read()
        print('ARP Entry deleted successfully ')


def restart_network():
    cmd = 'sudo systemctl restart networking'
    cmd2 = 'sudo systemctl status networking'
    os.popen(cmd).read()
    print('Network services restarted ')
    print(os.popen(cmd2).read())


def change_host_name():
    host_name = input("Enter new host name :")
    cmd = f'hostnamectl set-hostname {host_name}'
    os.popen(cmd).read()
    print(f'sudo new host name {host_name} set successfully ')


def add_dns_server():

    print('adding dns server')
    print('first : nameserver 8.8.8.8 write in this format')
    print('second : ctrl + d  to exit ')
    cmd = 'sudo cat  >> /etc/resolv.conf'
    print(os.popen(cmd).read())
    print('Nameserver added successfully  ')
