import paramiko
import os
import sys
import json
import time

def connect_tv(host='192.168.1.5', port=9922, user='prisoner', key_path=r'C:\Users\Dorp\.ssh\71b8ff2ec0', passphrase='2A3F6A'):
    print(f"Connecting to LG webOS TV at {host}:{port} as {user}...")
    key = paramiko.RSAKey.from_private_key_file(key_path, password=passphrase)
    
    sock = (host, port)
    transport = paramiko.Transport(sock)
    sec_opts = transport.get_security_options()
    sec_opts.key_types = ('ssh-rsa', 'rsa-sha2-512', 'rsa-sha2-256')
    sec_opts.pubkey_algorithms = ('ssh-rsa', 'rsa-sha2-512', 'rsa-sha2-256')
    
    transport.connect(username=user, pkey=key)
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    print("SSH connection established successfully!")
    return ssh

def test_connection():
    ssh = connect_tv()
    stdin, stdout, stderr = ssh.exec_command('uname -a; whoami; id')
    print("STDOUT:\n", stdout.read().decode())
    print("STDERR:\n", stderr.read().decode())
    ssh.close()

if __name__ == '__main__':
    test_connection()
