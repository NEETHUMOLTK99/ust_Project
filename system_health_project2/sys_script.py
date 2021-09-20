#system health project

import os

from sys_script import *




def display_aval_RAM():
    mem = os.popen(
        'free -m | tr -s " " | cut -d " " -f4 | head -n 2 | tail -n 1').read()
    print(f'Available memory on device => {mem} mb')


def display_load_avg():
    cmds = 'cat /proc/loadavg'
    cmd = input('Enter any of commands:- [cat /proc/loadavg,uptime,w] ')
    res = os.popen(cmd).read()
    print(res)


def hostname_details():
    cmd = 'hostnamectl status'
    res = os.popen(cmd).read()
    print(res)


def process_count():
    cmd = 'ps -a | wc -l'
    res = os.popen(cmd).read()
    print(f' {res} processes running on system ')


def display_uptime():
    cmd = 'uptime | cut -d " " -f2,3'
    res = os.popen(cmd).read()
    print(f'Uptime ==>  {res}')
