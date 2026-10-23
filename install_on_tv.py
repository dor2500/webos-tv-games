import subprocess
import os
import sys
import json

def install_ipk_on_tv(ipk_name, app_id, tv_ip=None):
    target_ip = tv_ip or os.environ.get("TV_IP")
    if not target_ip or target_ip.strip() in ("", "192.168.1.XX", "YOUR_TV_IP"):
        print("[-] Error: LG TV IP address is required.")
        print("    Usage: python install_on_tv.py <ipk_name> <app_id> [tv_ip]")
        print("    Or set environment variable: set TV_IP=192.168.1.XX")
        return None

    key_path = os.environ.get("TV_KEY_PATH", os.path.expandvars(r'%TEMP%\tv_key_nopass'))
    port = os.environ.get("TV_PORT", "9922")
    user = os.environ.get("TV_USER", "prisoner")
    
    payload = json.dumps({
        "id": app_id,
        "ipkUrl": f"/media/developer/temp/{ipk_name}",
        "subscribe": True
    })
    
    # Run luna-send-pub via OpenSSH CLI
    remote_cmd = f"luna-send-pub -i -n 1 luna://com.webos.appInstallService/dev/install '{payload}'"
    print(f"Installing {app_id} on LG TV ({target_ip})...")
    
    cmd = [
        "ssh",
        "-o", "StrictHostKeyChecking=no",
        "-o", "HostKeyAlgorithms=+ssh-rsa",
        "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa",
        "-i", key_path,
        "-p", str(port),
        f"{user}@{target_ip}",
        remote_cmd
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Response STDOUT:\n", res.stdout)
    if res.stderr:
        print("Response STDERR:\n", res.stderr)
        
    return res.stdout

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        target_ip = sys.argv[3] if len(sys.argv) > 3 else None
        install_ipk_on_tv(sys.argv[1], sys.argv[2], target_ip)
    else:
        print("Usage: python install_on_tv.py <ipk_name> <app_id> [tv_ip]")
