#!/bin/python3
import time
from colorama import Fore,Style
import os
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
def banner():
    print(Fore.MAGENTA+Style.BRIGHT+"""
███████╗ ██████╗ █████╗ ███╗   ██╗███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
███████╗██║     ███████║██╔██╗ ██║███████╗██████╔╝██║     ██║   ██║██║   ██║   
╚════██║██║     ██╔══██║██║╚██╗██║╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
███████║╚██████╗██║  ██║██║ ╚████║███████║██║     ███████╗╚██████╔╝██║   ██║   
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   

AUTHOR : GHOST
GITHUB : github.com/mdk4if
""")
def help():
    usage = Fore.CYAN+Style.BRIGHT+"""
    help                                        show this help menu
    add host,ah <ip/domain>                     add host(s) to perform scans
    list hosts,lh                               list added hosts 
    set host,sh <id>                            set host to scan 
    portscan,ps <start-end> | all | fast        perform port scan                               
    list scans,ls                               list scans
    set scan,ss <id>                            set type of scan to perform
    scan                                        start scanning 
    list outputs,lo                             list outputs
    show output,so <id>                         show output of a scan 
    q | quit | exit                             exit scansploit
    cl | clear | cls                            clear the screen
    """
    print(usage)

try:
    os.system("mkdir /home/ghost/.scansploit > /dev/null 2>&1")
except:
    pass
host_list = []
path = "/home/ghost/.scansploit/"
scanList = {
            "TCP SYN port scan": "nmap -sS ",
            "TCP connect port scan": "nmap -sT ",
            "UDP port scan": "nmap -sU ",
            "TCP ACK port scan": "nmap -sA ",
            "Only port scan": "nmap -Pn ",
            "Only host discovery": "nmap -sn",
            "ARP discovery on local networks": "nmap -PR ",
            "Disable DNS resolution": "nmap -n ",
            "Detect the version of services": "nmap -sV ",
            "OS Detection, Version Detection, script scanning and traceroute": "nmap -A ",
            "OS Detection": "nmap -O ",
            "Panaroid IDS evasion": "nmap -T0 ",
            "Sneaky IDS evasion": "nmap -T1 ",
            "Polite IDS evasion": "nmap -T2 ",
            "Normal IDS evasion": "nmap -T3 ",
            "Aggressive speed scan": "nmap -T4 ",
            "Insane speed scan": "nmap -T5 ",
            }
def portscan(scansploit,target):
    if "all" in scansploit:
        os.system(f"nmap -p- " + target + " -oN /home/ghost/.scansploit/" + time.strftime(f"{target}-%Y%m%d-%H%M%S"))
    elif "fast" in scansploit:
        os.system(f"nmap -F " + target + " -oN /home/ghost/.scansploit/" + time.strftime(f"{target}-%Y%m%d-%H%M%S"))
    else:
        os.system("nmap -p " + scansploit.split()[-1] + " " + target + " -oN /home/ghost/.scansploit/" + time.strftime(f"{target}-%Y%m%d-%H%M%S"))
    
def scansploit():
    banner()
    while True:
        scansploit = input(Fore.MAGENTA+Style.BRIGHT+"scansploit> "+Fore.GREEN)
        if scansploit == "help" or scansploit == "-h" or scansploit == "--help" or scansploit == "?":
            help()
        elif scansploit == "q" or scansploit == "quit" or scansploit == "exit":
            break
        elif scansploit == "":
            continue
        elif scansploit == "cl" or scansploit == "clear" or scansploit == "cls":
            os.system("clear")
        elif scansploit == "banner":
            banner()
        elif "add host" in scansploit or "ah" in scansploit:
            host_list.append(scansploit.split()[-1])
        elif scansploit == "list hosts" or scansploit == "lh":
            print("ID ---> HOST")
            for id,host in enumerate(host_list):
                print(f"{id} ---> {host}")
        elif "set host" in scansploit or "sh" in scansploit:
            host2scan = host_list[int(scansploit.split()[-1])]
            print(f"HOST ---> {host2scan}")
        elif "portscan" in scansploit or "ps" in scansploit:
            try:
                portscan(scansploit,host2scan)
            except:
                print("[!] You need to set the host first")
        elif scansploit == "list scans" or scansploit == "ls":
            print("ID ---> SCANS")
            for id,scan in enumerate(list(scanList.keys())):
                print(f"{id} ---> {scan}")
        elif "set scan" in scansploit or "ss" in scansploit:
            scan_index = list(scanList.keys())[int(scansploit.split()[-1])]
            print(f"SCAN ---> {scan_index}")
        elif scansploit == "scan":
            os.system(scanList[scan_index] + host2scan + " " + "-oN /home/ghost/.scansploit/" + time.strftime(f"{host2scan}-%Y%m%d-%H%M$S"))
        elif scansploit == "list outputs" or scansploit == "lo":
            print("ID ---> OUTPUT")
            for id,i in enumerate(os.listdir(path)):
                print(f"{id} ---> {i}")
        elif "show output" in scansploit or "so" in scansploit:
            os.system("cat " + path + os.listdir(path)[int(scansploit.split()[-1])])
        else:
            print(Fore.RED+Style.BRIGHT+"[!] Invalid command type help for more information")

            

scansploit()

