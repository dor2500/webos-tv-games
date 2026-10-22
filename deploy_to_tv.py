import subprocess
import os
import sys
import json
import time

KEY_PATH = os.path.expandvars(r'%TEMP%\tv_key_nopass')
TV_IP = "192.168.1.5"
PORT = "9922"
USER = "prisoner"

SSH_BASE = [
    "ssh",
    "-o", "StrictHostKeyChecking=no",
    "-o", "HostKeyAlgorithms=+ssh-rsa",
    "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa",
    "-i", KEY_PATH,
    "-p", PORT,
    f"{USER}@{TV_IP}"
]

SCP_BASE = [
    "scp",
    "-o", "StrictHostKeyChecking=no",
    "-o", "HostKeyAlgorithms=+ssh-rsa",
    "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa",
    "-i", KEY_PATH,
    "-P", PORT
]

def deploy_package(local_ipk_path, app_id):
    ipk_name = os.path.basename(local_ipk_path)
    remote_temp = f"/media/developer/temp/{ipk_name}"
    
    print(f"\n==========================================")
    print(f"Deploying {ipk_name} ({app_id}) to LG TV...")
    print(f"==========================================")
    
    # 1. SCP file to TV
    print(f"1. Uploading {ipk_name} to {remote_temp}...")
    scp_cmd = SCP_BASE + [local_ipk_path, f"{USER}@{TV_IP}:{remote_temp}"]
    res_scp = subprocess.run(scp_cmd, capture_output=True, text=True)
    if res_scp.returncode != 0:
        print(f"SCP Error:\n{res_scp.stderr}")
        return False
    print("Upload complete!")

    # 2. Trigger installation via luna-send-pub
    print("2. Calling webOS appInstallService...")
    payload = json.dumps({
        "id": app_id,
        "ipkUrl": remote_temp,
        "subscribe": True
    })
    remote_install_cmd = f"luna-send-pub -i -n 1 luna://com.webos.appInstallService/dev/install '{payload}'"
    res_install = subprocess.run(SSH_BASE + [remote_install_cmd], capture_output=True, text=True)
    print("Install output:\n", res_install.stdout)
    if res_install.stderr:
        print("Install stderr:\n", res_install.stderr)
        
    # 3. Clean up temp file
    print("3. Cleaning up temporary remote IPK...")
    subprocess.run(SSH_BASE + [f"rm -f {remote_temp}"], capture_output=True)
    
    print(f"Successfully deployed {app_id} to LG TV!\n")
    return True

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        deploy_package(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python deploy_to_tv.py <local_ipk_path> <app_id>")
