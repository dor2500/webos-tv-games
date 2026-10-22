import subprocess
import os
import sys
import json

def install_ipk_on_tv(ipk_name, app_id):
    key_path = os.path.expandvars(r'%TEMP%\tv_key_nopass')
    payload = json.dumps({
        "id": app_id,
        "ipkUrl": f"/media/developer/temp/{ipk_name}",
        "subscribe": True
    })
    
    # Run luna-send-pub via OpenSSH CLI
    remote_cmd = f"luna-send-pub -i -n 1 luna://com.webos.appInstallService/dev/install '{payload}'"
    print(f"Installing {app_id} on LG TV...")
    
    cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "HostKeyAlgorithms=+ssh-rsa",
        "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa",
        "-i", key_path,
        "-p", "9922",
        "prisoner@192.168.1.5",
        remote_cmd
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Response STDOUT:\n", res.stdout)
    if res.stderr:
        print("Response STDERR:\n", res.stderr)
        
    return res.stdout

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        install_ipk_on_tv(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python install_on_tv.py <ipk_name> <app_id>")
