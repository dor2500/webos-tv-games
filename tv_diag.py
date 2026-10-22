import subprocess
import os
import json

key_path = os.path.expandvars(r'%TEMP%\tv_key_nopass')

def run_ssh(remote_cmd):
    cmd = [
        'ssh',
        '-o', 'StrictHostKeyChecking=no',
        '-o', 'HostKeyAlgorithms=+ssh-rsa',
        '-o', 'PubkeyAcceptedKeyTypes=+ssh-rsa',
        '-i', key_path,
        '-p', '9922',
        'prisoner@192.168.1.5',
        remote_cmd
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout, res.stderr

if __name__ == '__main__':
    # 1. Block Updates via HBChannel
    print("Setting blockUpdates to true...")
    out, err = run_ssh('luna-send-pub -n 1 -f luna://org.webosbrew.hbchannel.service/setConfiguration \'{"blockUpdates":true}\'')
    print("Response:", out)

    # 2. Verify Config
    out, err = run_ssh('luna-send-pub -n 1 -f luna://org.webosbrew.hbchannel.service/getConfiguration \'{}\'')
    print("New Config:\n", out)
