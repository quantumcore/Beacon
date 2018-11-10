# Date Completed - Sept - 11 - 2018
# Date Modified : 2 nov 2018
# Changelogs : 
# Added Registration feature.
# Fixed some bugs

import socket
import os
from threading import Thread
try:
        import colorama
except ImportError:
        os.system("py -m pip install colorama")
        
from colorama import Fore, Style
import platform
import datetime, smtplib
import core

def __main__():
        """Registration"""

        def clear_screen(): 
            """Clear the screen only"""
            if os.name == 'nt': 
                    os.system('cls') 
            else: 
                    os.system('clear')

        print(Fore.YELLOW+"Starting Script ... "+Style.RESET_ALL)
        def registration_process():   

                def send_mail(message):
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.ehlo()

                        try:
                                server.login(user_email, user_password)
                        except smtplib.SMTPAuthenticationError as login_incorrect:
                                print("[ - ] Login Information Incorrect. Re-run.", login_incorrect)
                                exit(1)

                        try:
                                server.sendmail(user_email, __author_email__, message)
                        except Exception as email_error:
                                print("[ - ] Email Sending Error, Re - run : ", email_error)
                                exit(1)

                        print("[ + ] Email Sent!")

                print("------------------------------------------------------------------------")
                print("| User Registration Process, Do not quit please.")
                print("| Registeration Process will ask you for your GMAIL Credentials.")
                print("| No Malacious intentions (See Code). Email will be sent with your Account to Author as part of Registration")
                print("| Email message will be sent to developer just notifiyng that a new Person has Registered.")
                print("| Information Taken is : Platform Name, Date & Time & Email. (Any doubts, See Code.)")
                print("| " + platform.platform() + "| | ", datetime.datetime.now(), " | | ", "Your Gmail. |")
                print("------------------------------------------------------------------------")
                print("[ ------------- Process may take time. Please be patient ------------- ]")
                user_name = input("[ ! ] Enter your USERNAME : ")
                user_email = input("[ ! ] Enter GMAIL : ")
                user_password = input("[ ! ] Enter Password : ")
                __author_email__ = "fahad.mustafa0012@gmail.com"
                ostime = datetime.datetime.now()
                ostime = str(ostime)

                msg = "Hey, My EMAIL is " + user_email + " & I just Registered in Beacon with " + platform.platform() + " !\n Time is " + ostime

                info = open("user-info", "w+")
                info.write("--] Email : " + user_email)
                info.write("\n--] USERNAME : " + user_name)
                info.close()

                extra_msg = input("[ ? ] Would you like to send any Message to Developer? (Y/n): ")
                if(extra_msg == "Y".lower().strip()):
                        extra = input("[ ! ] Enter Message : ")
                        send_mail(msg)
                        send_mail(extra)
                else:
                        print("Okay, Skip.")
                        send_mail(msg)

                print("[ + ] You are Registered!")
                input("[ + ] Press Any key to Exit. Restart the Program to use Beacon.")
        
        try:
                clear_screen()
                user_file = open("user-info", "r")
                print(Fore.LIGHTCYAN_EX+"All things [OK]"+Style.RESET_ALL)
                core.__main__()
        except FileNotFoundError:
                clear_screen()
                print(Fore.YELLOW+"Starting Script ... "+Style.RESET_ALL)
                print("[ * ] Starting Registration..")
                registration_process()


if __name__ == "__main__":
    __main__()
