#!/usr/bin/env python3
import os
import sys
import tarfile
import io
import time

def build_ar_header(name, size, timestamp=None, mode=0o100644, uid=0, gid=0):
    if timestamp is None:
        timestamp = int(time.time())
    name_field = f"{name:<16}".encode('ascii')
    time_field = f"{timestamp:<12}".encode('ascii')
    uid_field = f"{uid:<6}".encode('ascii')
    gid_field = f"{gid:<6}".encode('ascii')
    mode_field = f"{mode:<8o}".encode('ascii')
    size_field = f"{size:<10}".encode('ascii')
    magic = b"`\n"
    return name_field + time_field + uid_field + gid_field + mode_field + size_field + magic

def create_tar_gz_bytes(source_dir, prefix=""):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz", format=tarfile.GNU_FORMAT) as tar:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, source_dir)
                arcname = os.path.join(prefix, rel_path).replace("\\", "/")
                tar.add(full_path, arcname=arcname)
    return buf.getvalue()

def build_ipk(app_dir, output_ipk_path, app_id, version, title="App"):
    # 1. Create control.tar.gz
    control_content = f"""Package: {app_id}
Version: {version}
Section: misc
Priority: optional
Architecture: all
Maintainer: Retro Hub dor2500
Description: {title} for LG webOS TV
"""
    ctrl_buf = io.BytesIO()
    with tarfile.open(fileobj=ctrl_buf, mode="w:gz", format=tarfile.GNU_FORMAT) as tar:
        ti = tarfile.TarInfo("control")
        ti.size = len(control_content.encode('utf-8'))
        ti.mtime = int(time.time())
        ti.mode = 0o644
        tar.addfile(ti, io.BytesIO(control_content.encode('utf-8')))
    control_tgz = ctrl_buf.getvalue()

    # 2. Create data.tar.gz
    data_tgz = create_tar_gz_bytes(app_dir, prefix=f"usr/palm/applications/{app_id}")

    # 3. Assemble debian-binary / AR archive
    deb_binary = b"2.0\n"
    
    os.makedirs(os.path.dirname(os.path.abspath(output_ipk_path)), exist_ok=True)
    with open(output_ipk_path, "wb") as f:
        # AR Magic
        f.write(b"!<arch>\n")
        
        # 1. debian-binary
        hdr1 = build_ar_header("debian-binary", len(deb_binary))
        f.write(hdr1)
        f.write(deb_binary)
        if len(deb_binary) % 2 != 0:
            f.write(b"\n")
            
        # 2. control.tar.gz
        hdr2 = build_ar_header("control.tar.gz", len(control_tgz))
        f.write(hdr2)
        f.write(control_tgz)
        if len(control_tgz) % 2 != 0:
            f.write(b"\n")
            
        # 3. data.tar.gz
        hdr3 = build_ar_header("data.tar.gz", len(data_tgz))
        f.write(hdr3)
        f.write(data_tgz)
        if len(data_tgz) % 2 != 0:
            f.write(b"\n")

    print(f"Successfully generated {output_ipk_path} ({os.path.getsize(output_ipk_path)} bytes)")

if __name__ == "__main__":
    if len(sys.argv) >= 5:
        build_ipk(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] if len(sys.argv) > 5 else "App")
    else:
        print("Usage: python build_ipk.py <app_dir> <output_ipk> <app_id> <version> [title]")
