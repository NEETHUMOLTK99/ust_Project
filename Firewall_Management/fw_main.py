#Program for firewall management

import os
from rich.prompt import Prompt

CONF ={}

def main_menu():
    print("___Firewall Management___")
    print("1. Display Status of firewall")
    print("2. Add Rules")
    print("3. Delete Rules")
    print("4. Reload Rule")
    print("5. Quit")

def add_rule_menu():
	print("\t[1]Add Port")
	print("\t[2]Add services")
	print("\t[3]Add sources")
	print("\t[4]Back to Main menu")    

def dlt_rule_menu():
	print("\t[1]Remove Port")
	print("\t[2]Remove services")
	print("\t[3]Remove sources")
	print("\t[4]Back to Main menu") 

def fw_get_active_zones():
	zone = os.popen("sudo firewall-cmd --get-active-zones").read()
	CONF["ZONE"] = zone.split("\n")[0]
	print(zone)  

def fw_activate():
	print("Activating the firewall")
	os.popen("sudo systemctl start firewalld").read()         

def firewall_status():
    state = os.popen("sudo firewall-cmd --state").read()
    if state == "running\n":
        print("Firewall is active")
    else:
        print("Firewall is not active")
        fw_activate()
    fw_get_active_zones()

#Functions for add_rules()

def get_zone_list():
    zone_lst = os.popen("sudo firewall-cmd --get-zones").read().split(" ")
    zone_lst[-1] = zone_lst[-1][:-1] 
    return zone_lst


def get_services():
	print("___________________")
	print("Service List:")
	cmd = "sudo firewall-cmd --get-services"
	print(os.popen(cmd).read())
	print("___________________")

def add_port():
    port = Prompt.ask("Enter port number : ")
    proto = Prompt.ask("Enter protocol :", choices=["tcp","udp"],default="tcp")
    zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = "sudo firewall-cmd --add-port="+port+"/"+proto+" --zone="+zone+" --permanent "
    print(os.popen(cmd).read())    

def add_services():
	get_services()
	service = Prompt.ask("Enter service name from above list : ")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-service="+service+" --zone="+zone+" --permanent" 
	print(os.popen(cmd).read())

def add_sources():
    ip = input('Enter source ip address : ')
    cmd = f'sudo firewall-cmd --add-source ={ip}'
    print(os.popen(cmd).read)    


def add_rules():
    while True:
        add_rule_menu()
        ch = int(input("Enter your option : "))
        if ch == 1:
            #add port
            add_port()
        elif ch == 2:
            add_services()
            #add services
        elif ch == 3:
            #add sources
            add_sources()
        elif ch == 4:
            break
        else:
            print("Invalid option")


def dlt_port():
    port = Prompt.ask("Enter port number : ")
    proto = Prompt.ask("Enter protocol :", choices=["tcp","udp"],default="tcp")
    zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
    cmd = "sudo firewall-cmd --remove-port="+port+"/"+proto+" --zone="+zone+" --permanent "
    print(os.popen(cmd).read())    

def dlt_services():
	get_services()
	service = Prompt.ask("Enter service name from above list : ")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --remove-service="+service+" --zone="+zone+" --permanent" 
	print(os.popen(cmd).read())

def dlt_sources():
    ip = input('Enter source ip address : ')
    cmd = f'sudo firewall-cmd --remove-source ={ip}'
    print(os.popen(cmd).read)        


def delete_rules():
    while True:
        dlt_rule_menu()
        ch = int(input("Enter your option : "))
        if ch == 1:
            #add port
            dlt_port()
        elif ch == 2:
            dlt_services()
            #add services
        elif ch == 3:
            #add sources
            dlt_sources()
        elif ch == 4:
            break
        else:
            print("Invalid option")

def reload_rule():
    print(os.popen("sudo firewall-cmd --reload").read())
    
    
    
while True:
    main_menu()
    ch = int(input("Enter your choice : "))

    if ch == 1:
        firewall_status()

    elif ch == 2:
        add_rules()

    elif ch == 3:
        delete_rules()    

    elif ch == 4:
        reload_rule()    

    elif ch == 5:
        break

    else:
        print("Enter a valid choice !")
