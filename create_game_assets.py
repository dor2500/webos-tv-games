import os
from PIL import Image, ImageDraw, ImageFont

def make_gradient(width, height, color1, color2):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

games_meta = {
    'angrybirds_rio': {
        'title': 'Angry Birds Rio',
        'c1': (2, 132, 199), 'c2': (21, 128, 61),
        'symbol': '🦜', 'sub': 'RIO EDITION'
    },
    'cuttherope': {
        'title': 'Cut the Rope',
        'c1': (34, 197, 94), 'c2': (113, 63, 18),
        'symbol': '🍬', 'sub': 'OM NOM'
    },
    'duckhunt': {
        'title': 'Duck Hunt',
        'c1': (234, 88, 12), 'c2': (15, 23, 42),
        'symbol': '🦆', 'sub': 'LIGHT GUN'
    },
    'mario': {
        'title': 'Super Mario',
        'c1': (239, 68, 68), 'c2': (30, 58, 138),
        'symbol': '🍄', 'sub': 'WORLD 1-1'
    },
    'tetris': {
        'title': 'Classic Tetris',
        'c1': (168, 85, 247), 'c2': (15, 23, 42),
        'symbol': '🧩', 'sub': 'RETRO 1989'
    },
    'flappybird': {
        'title': 'Flappy Bird',
        'c1': (112, 197, 206), 'c2': (116, 191, 46),
        'symbol': '🐥', 'sub': '4K RETRO'
    },
    'pacman': {
        'title': 'Pac-Man 1980',
        'c1': (250, 204, 21), 'c2': (30, 58, 138),
        'symbol': '🟡', 'sub': 'NAMCO ARCADE'
    },
    'spaceinvaders': {
        'title': 'Space Invaders',
        'c1': (34, 197, 94), 'c2': (0, 0, 0),
        'symbol': '👾', 'sub': 'TAITO 1978'
    }
}

for gid, data in games_meta.items():
    gdir = os.path.join(r"apps\retrohub\games", gid)
    os.makedirs(gdir, exist_ok=True)
    
    # 1. Icon (130x130)
    icon = make_gradient(130, 130, data['c1'], data['c2'])
    d_icon = ImageDraw.Draw(icon)
    d_icon.rectangle([0, 0, 129, 129], outline=(255, 255, 255), width=3)
    d_icon.text((65, 55), data['symbol'], fill=(255, 255, 255), anchor="mm")
    d_icon.text((65, 105), data['sub'], fill=(255, 255, 255), anchor="mm")
    icon.save(os.path.join(gdir, "icon.png"))
    
    # 2. Splash / Poster (640x360)
    splash = make_gradient(640, 360, data['c1'], data['c2'])
    d_splash = ImageDraw.Draw(splash)
    d_splash.rectangle([10, 10, 629, 349], outline=(255, 255, 255, 180), width=4)
    d_splash.text((320, 140), data['symbol'], fill=(255, 255, 255), anchor="mm")
    d_splash.text((320, 230), data['title'], fill=(255, 255, 255), anchor="mm")
    d_splash.text((320, 280), data['sub'] + " • LG webOS Edition", fill=(250, 204, 21), anchor="mm")
    splash.save(os.path.join(gdir, "splash.png"))
    
print("Generated all game icon and splash assets successfully!")
