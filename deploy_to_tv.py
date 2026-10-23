import subprocess
import os
import sys
import json
import time

# Dynamic configuration - no private IP addresses or hardcoded personal credentials
TV_IP = os.environ.get("TV_IP")
PORT = os.environ.get("TV_PORT", "9922")
USER = os.environ.get("TV_USER", "prisoner")
KEY_PATH = os.environ.get("TV_KEY_PATH", os.path.expandvars(r'%TEMP%\tv_key_nopass'))

def get_ssh_cmd(tv_ip, port=PORT, user=USER, key_path=KEY_PATH):
    return [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "HostKeyAlgorithms=+ssh-rsa",
        "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa",
        "-i", key_path,
        "-p", str(port),
        f"{user}@{tv_ip}"
    ]

def get_scp_cmd(port=PORT, key_path=KEY_PATH):
    return [
        "scp",
        "-o", "StrictHostKeyChecking=no",
        "-o", "HostKeyAlgorithms=+ssh-rsa",
        "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa",
        "-i", key_path,
        "-P", str(port)
    ]

def deploy_package(local_ipk_path, app_id, tv_ip=None):
    target_ip = tv_ip or TV_IP
    if not target_ip or target_ip.strip() in ("", "192.168.1.XX", "YOUR_TV_IP"):
        print("[-] Error: LG TV IP address is required.")
        print("    Usage: python deploy_to_tv.py <local_ipk_path> <app_id> [tv_ip]")
        print("    Or set the environment variable: set TV_IP=192.168.1.XX (PowerShell: $env:TV_IP='192.168.1.XX')")
        return False

    ipk_name = os.path.basename(local_ipk_path)
    remote_temp = f"/media/developer/temp/{ipk_name}"
    
    print(f"\n==========================================")
    print(f"Deploying {ipk_name} ({app_id}) to LG TV at {target_ip}:{PORT}...")
    print(f"==========================================")
    
    # 1. SCP file to TV
    print(f"1. Uploading {ipk_name} to {remote_temp}...")
    scp_base = get_scp_cmd()
    scp_cmd = scp_base + [local_ipk_path, f"{USER}@{target_ip}:{remote_temp}"]
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
    ssh_base = get_ssh_cmd(target_ip)
    remote_install_cmd = f"luna-send-pub -i -n 1 luna://com.webos.appInstallService/dev/install '{payload}'"
    res_install = subprocess.run(ssh_base + [remote_install_cmd], capture_output=True, text=True)
    print("Install output:\n", res_install.stdout)
    if res_install.stderr:
        print("Install stderr:\n", res_install.stderr)
        
    # 3. Clean up temp file
    print("3. Cleaning up temporary remote IPK...")
    subprocess.run(ssh_base + [f"rm -f {remote_temp}"], capture_output=True)
    
    print(f"Successfully deployed {app_id} to LG TV!\n")
    return True

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        target_ip = sys.argv[3] if len(sys.argv) > 3 else None
        deploy_package(sys.argv[1], sys.argv[2], target_ip)
    else:
        print("Usage: python deploy_to_tv.py <local_ipk_path> <app_id> [tv_ip]")
        print("Example: python deploy_to_tv.py packages/com.retrohub.nostalgia_5.1.0_all.ipk com.retrohub.nostalgia 192.168.X.X")
