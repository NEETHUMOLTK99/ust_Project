#!/usr/bin/python3
import os
from sys_script import *




def main_menu():
    
    print('1.Display available RAM')
    print('2.Display load average')
    print('3.Display Hostname details')
    print('4.Display All process count')
    print('5.Display uptime')
    print('6.Exit')
    


while True:
    main_menu()
    ch = int(input('Enter choice : '))
    if ch == 1:
        display_aval_RAM()
    elif ch == 2:
        display_load_avg()
    elif ch == 3:
        hostname_details()
    elif ch == 4:
        process_count()
    elif ch == 5:
        display_uptime()
    elif ch == 6:
        break
    else:
        console.print('oops ! wrong option  ')
