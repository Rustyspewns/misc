#!/usr/bin/env python

import paramiko

with paramiko.SSHClient() as ssh:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect('192.168.1.102', username='kali', password='P@ssw0rd')

    stdin, stdout, stderr = ssh.exec_command('whoami')
    print(stdout.read().decode())
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l')
    print(stdout.read().decode())
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('ls -l /etc/passwd /etc/horecrux')
    print("STDOUT:")
    print(stdout.read().decode())
    print("STDERR:")
    print(stderr.read().decode())
    print('-' * 60)
