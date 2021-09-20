#!/usr/bin/python3

import os

CONF ={}



def print(string):
	print(Text(string))

def print(string): 
	print(Text(string))

def fw_reload():
	print(os.popen("sudo firewall-cmd --reload").read())

def fw_get_active_zones():
	zone = os.popen("sudo firewall-cmd --get-active-zones").read()
	CONF["ZONE"] = zone.split("\n")[0]
	print(zone)

def fw_activate():
	gprint("Activating the firewall")
	os.popen("sudo systemctl start firewalld").read()

def fw_get_status():
	state = os.popen("sudo firewall-cmd --state").read()
	if state == "running\n":
		gprint("Firewall is active")
	else:
		rprint("Firewall is not active")
		fw_activate()
	fw_get_active_zones()

def get_zone_list():
	zone_lst = os.popen("sudo firewall-cmd --get-zones").read().split(" ")
	zone_lst[-1] = zone_lst[-1][:-1] 
	return zone_lst

def fw_add_port():
	port = Prompt.ask("Enter port number : ")
	proto = Prompt.ask("Enter protocol :", choices=["tcp","udp"],default="tcp")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-port="+port+"/"+proto+" --zone="+zone+" --permanent "
	print(os.popen(cmd).read())

def fw_get_services():
	gprint("_________________________________________________________")
	gprint("Service List:")
	cmd = "sudo firewall-cmd --get-services"
	print(os.popen(cmd).read())
	gprint("_________________________________________________________")

def fw_add_services():
	fw_get_services()
	service = Prompt.ask("Enter service name from above list : ")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-service="+service+" --zone="+zone+" --permanent" 
	print(os.popen(cmd).read())

def fw_add_rule_menu():
	gprint("\t[1]Add Port")
	gprint("\t[2]Add services")
	gprint("\t[3]Add sources")
	gprint("\t[4]Back to Main menu")

def fw_add_rule():
	fw_add_rule_menu()
	ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3","4"])
	if ch == "1":
		#add port
		fw_add_port()
		pass
	elif ch == "2":
		fw_add_services()
		#add services
		pass
	elif ch == "3":
		#add sources
		pass
	elif ch == "4":
		pass
	else:
		pass
		

def main_menu():
	print("[1] Add rules")
	print("[2] Delete rules")
	print("[3] Get Active Zones")
	print("[4] Get Details of Active Zones")
	print("[5] Reload firewall")
	print("[6] Exit")



if __name__ == "__main__":
	fw_get_status()
	while True:
		main_menu()
		ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3","4","5","6"])
		if ch == "1":
			#Add rule
			fw_add_rule()
			pass
		elif ch == "2":
			#delete rules
			pass
		elif ch == "3":
			fw_get_active_zones()
			pass
		elif ch == "4":
			#get active zone details
			pass
		elif ch == "5":
			fw_reload()
			pass
		elif ch == "6":
			#exit
			break;
		else:
			print(Text("Wrong option! Type option again "))
