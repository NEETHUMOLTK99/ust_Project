#!/usr/bin/python3

#Network Management Tool


import os

from net_script import *

def main_menu():
	print("1. Assign IP Address")
	print("2. Delete IP Address")
	print("3. Display IP Address")
	print("4. Display all Interfaces")
	print("5. configure Routing ")
	print("6. Turn on/off Interfaces")
	print("7. Add ARP entry")
	print("8. Delete ARP Entry")
	print("9. Restart Network")
	print("10.Change Hostname")
	print("11.Add DNS server entry")
	print("12.Exit")

while True:
	main_menu()
	ch = int(input('Enter Choice : '))
	if ch == 1:
		ip_cmnd()

	elif ch == 2:
		ip_cmnd_del()
	elif ch == 3:
		ip_cmnd_display()
	elif ch == 4:
		display_all_interface()
	elif ch == 5:
		configure_routing()
	elif ch == 6:
		on_off_interface()
	elif ch == 7:
		add_ARP_entry()
	elif ch == 8:
		del_ARP_entry()
	elif ch == 9:
		restart_network()
	elif ch == 10:
		change_hostname()
	elif ch == 11:
		add_dns_server()
	elif ch == 12:
		break;
	else:
		print("Wrong Choice")
