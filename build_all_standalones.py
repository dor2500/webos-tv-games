import os
import shutil
import json
from build_ipk import build_ipk

games = [
    {
        'id': 'com.dor.flappybird',
        'title': 'פלאפי בירד 4K',
        'src': r'apps\retrohub\games\flappybird',
        'version': '1.0.0'
    },
    {
        'id': 'com.dor.pacman',
        'title': 'פאק-מן 1980 קלאסי',
        'src': r'apps\retrohub\games\pacman',
        'version': '1.0.0'
    },
    {
        'id': 'com.dor.spaceinvaders',
        'title': 'Space Invaders 1978',
        'src': r'apps\retrohub\games\spaceinvaders',
        'version': '1.0.0'
    },
    {
        'id': 'com.dor.cuttherope',
        'title': 'Cut the Rope (חתוך את החבל)',
        'src': r'apps\retrohub\games\cuttherope',
        'version': '1.0.0'
    },
    {
        'id': 'com.dor.duckhunt',
        'title': 'דאק האנט (Duck Hunt)',
        'src': r'apps\retrohub\games\duckhunt',
        'version': '1.0.0'
    },
    {
        'id': 'com.dor.mario',
        'title': 'סופר מריו קלאסי',
        'src': r'apps\retrohub\games\mario',
        'version': '1.0.0'
    },
    {
        'id': 'com.dor.tetris',
        'title': 'טטריס קלאסי',
        'src': r'apps\retrohub\games\tetris',
        'version': '1.0.0'
    }
]

for g in games:
    app_dir = os.path.join("apps", g['id'].split('.')[-1])
    os.makedirs(app_dir, exist_ok=True)
    
    # Copy files
    for f in os.listdir(g['src']):
        src_file = os.path.join(g['src'], f)
        dst_file = os.path.join(app_dir, f)
        if os.path.isfile(src_file):
            shutil.copy(src_file, dst_file)
            
    # Make sure largeIcon exists
    if not os.path.exists(os.path.join(app_dir, "largeIcon.png")):
        shutil.copy(os.path.join(app_dir, "icon.png"), os.path.join(app_dir, "largeIcon.png"))
        
    # Write appinfo.json
    appinfo = {
        "id": g['id'],
        "version": g['version'],
        "vendor": "Retro TV Collection dor2500",
        "type": "web",
        "main": "index.html",
        "title": g['title'],
        "icon": "icon.png",
        "largeIcon": "largeIcon.png",
        "bgImage": "splash.png",
        "splashBackground": "splash.png",
        "resolution": "1920x1080",
        "bgColor": "#000000",
        "iconColor": "#38BDF8",
        "supportGIP": False,
        "requiredPermissions": [],
        "handlesRelaunch": True,
        "uiRevision": 2
    }
    with open(os.path.join(app_dir, "appinfo.json"), "w", encoding="utf-8") as f:
        json.dump(appinfo, f, indent=2, ensure_ascii=False)
        
    out_ipk = os.path.join("packages", f"{g['id']}_{g['version']}_all.ipk")
    build_ipk(app_dir, out_ipk, g['id'], g['version'], g['title'])
    print(f"Built standalone IPK: {out_ipk}")

print("All standalone IPKs created successfully!")
