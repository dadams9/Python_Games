# Game Setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
CAPTION = "Star Wars: Empire Strikes First"
FILL_COLOR = 'white'

#UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80
UI_FONT = "Consolas" #pg.font.SysFont("Arial", 18)
UI_FONT_SIZE = 18

#UI Colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#Upgrade Menu
TEXT_COLOR_SELECTED = '#111111' #red : '#FF0000'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#General Colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'


#Weapons
weapon_data = {'saber': {'cooldown': 100, 'damage': 15, 'graphic': 'images/characters/vader/attacks/saber/full.png'},
               'lightning_1': {'cooldown': 100, 'damage': 15, 'graphic': 'images/characters/vader/attacks/lightning_1/right.png'},
               'drain_1': {'cooldown': 100, 'damage': 15, 'graphic': 'images/characters/vader/attacks/drain_1/right.png'}}
#weapon_data = {'laser': {'cooldown': 100, 'damage': 15, 'graphic': 'images/wookie/laser/full.png'}}

force_data = {'push': {'strength': 0, 'cost': 2, 'level': 1, 'graphic': 'images/particles/force/push/right/force_push_4.png'},
              'lightning': {'strength': 20, 'cost': 5, 'level': 1, 'graphic': 'images/particles/force/lightning/right/lightning_particles-3.png'},
              'drain': {'strength': 10, 'cost': 10, 'level': 1, 'graphic': 'images/particles/force/drain/right/drain-1.png'}}
#'pull': {'strength': 0, 'cost': 2, 'level': 1, 'graphic': 'images/particles/force/push/left/force_push-12.png'},


#Enemies
enemy_data = {
    'wookie': {'health': 200, 'exp': 100, 'damage': 30, 'attack_type': 'bowcaster', 'attack_sound': 'audio_path', 'speed': 1.5, 'resistance': 2, 'attack_radius': 80, 'notice_radius': 300},
    'chewy': {'health': 300, 'exp': 300, 'damage': 50, 'attack_type': 'bowcaster', 'attack_sound': 'audio_path', 'speed': 1.5, 'resistance': 2, 'attack_radius': 100, 'notice_radius': 300}
}



WORLD_MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    ]
