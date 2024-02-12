# Author:       Ernesto Jaboneta
# File Name:    PokeBattle.py
# Last Update:  02-09-2024
# Version:      0.040

DIR = '/Games/PokeBattle'
from sys import path
if not DIR in path:
    path.append( DIR )

# IMPORTS
import gc
import time
import thumby
import math
import random
from pokemon import get_pokemon
# from moves import get_move
from thumbyGrayscale import display, Sprite

# INITIAL SETTINGS
display.brightness(40)
display.setFPS(30)


# INITIAL VALUES
currentScreen = 'main'
showingMessage = 0


def wrapText(text):
    width = 15
    lines = []
    line = ""
    for word in text.split():
        if len(line) + len(word) <= 15:
            line += word + " "
        else:
            lines.append(line.rstrip())
            line = word + " "
    lines.append(line.rstrip())
    return lines

def showMessage(message):
    global showingMessage
    start_time = time.ticks_ms()
    showingMessage = 1
    while showingMessage:
        display.drawFilledRectangle(0,16,72,24,1)
        display.drawRectangle(1,17,70,22,0)
        messageY = 21
        
        for line in wrapText(message):
            display.drawText(line, 4, messageY, 0)
            messageY += 8
        if thumby.buttonA.justPressed() or time.ticks_ms() - start_time >= 4000:
            showingMessage=0
            return 0
        
        display.update()
        
def process_round(move):
    global attacking,Pokemon1,Pokemon2
    # Get Player2(CPU) move
    opp_move = random.choice(Pokemon2.moves)
    
    # Determine attack order
    if Pokemon1.speed > Pokemon2.speed:
        attack(Pokemon1,Pokemon2,move)
        attack(Pokemon2,Pokemon1,opp_move)
    else:
        attack(Pokemon2,Pokemon1,opp_move)
        attack(Pokemon1,Pokemon2,move)
        
    attacking = 0
    

def attack(attacker,target,move):
    showMessage(attacker.name + ' used ' + move.name)
    # Formula: Damage = floor(floor(floor(2 * Level / 5 + 2) * Attach * Power / Defense) / 50) + 2
    damage = math.floor(math.floor(math.floor(2 * 50 / 5 + 2) * Pokemon1.attack * move.power / Pokemon2.defense) / 50) + 2
    target.set_hp(target.hp - damage)
    showMessage(target.name + ' took ' + str(damage) + ' damage')
    
def drawHp():
    global Pokemon1,Pokemon2
    display.drawRectangle(31,35,30,3,0)
    display.drawFilledRectangle(31,36,Pokemon1.hp_bar,1,0)
    display.drawRectangle(10,7,30,3,0)
    display.drawFilledRectangle(10,8,Pokemon2.hp_bar,1,0)
        
    
# A Button Bitmap
aMap = bytearray([131,125,130,234,234,234,130,125,131,
           1,1,0,0,0,0,0,1,1])

Pokemon1 = get_pokemon(25)
Pokemon2 = get_pokemon(151)
gc.collect
# Arrow Bitmap
arrowMap = bytearray([0,17,27])  

menu_pos = 0
attacking = 0

while(1):
    if(currentScreen == 'main'):
        display.fill(1)
        display.setFont("/lib/font3x5.bin", 3, 5, 1)
        
        # Player / Pikachu
        Pokemon1.frontPic.x = 0
        Pokemon1.frontPic.y = int(round(display.height) - (28))
        display.drawSprite(Pokemon1.frontPic) 
        display.drawText(Pokemon1.name, 31, 29, 0)
        
        # Opponent / Mew
        Pokemon2.backPic.x = int(display.width -28)
        Pokemon2.backPic.y = int(0)
        display.drawSprite(Pokemon2.backPic)
        display.drawText(Pokemon2.name, 10, 1, 0)
        
        drawHp()
        
        # Blink A Button
        aButtonIcon = thumby.Sprite(9,9,aMap,62,30)
        if time.ticks_ms() % 1000 < 500:
            display.drawSprite(aButtonIcon)
    
        #
        if(attacking):
            process_round(Pokemon1.moves[menu_pos])
    
        if thumby.buttonA.justPressed():
            currentScreen = 'show_moves'
            
                
    elif(currentScreen == 'show_moves'):
        display.fill(1)
        display.drawRectangle(1, 1, display.width-2, display.height-2, 0)
        display.drawFilledRectangle(40, 1, 26, 8, 1)
        display.drawText("FIGHT!", 42, 1, 0)
    
        # Display the list of moves
        moveX = 10
        moveY = 8
        for i, move in enumerate(Pokemon1.moves):
            Pokemon1.moves[i].y = moveY
            display.drawText(move.name, moveX, Pokemon1.moves[i].y, 0)
            moveY += 7
            
            
        # Display arrow cursor
        arrow = Sprite(3, 5, arrowMap)
        arrow.x = 5
        arrow.y = Pokemon1.moves[menu_pos].y
        display.drawSprite(arrow)
        
        # Move arrow for move selection
        if thumby.buttonU.justPressed() and menu_pos > 0:
            menu_pos -= 1
            arrow.y = Pokemon1.moves[menu_pos].y
            print(menu_pos)
            
        if thumby.buttonD.justPressed() and menu_pos < len(Pokemon1.moves) - 1:
            menu_pos += 1
            arrow.y = Pokemon1.moves[menu_pos].y
            print(menu_pos)
        
        # Select Move 
        if thumby.buttonA.justPressed():
            print('A Pressed')
            attacking=1
            currentScreen = 'main'
            
        # Go back
        if thumby.buttonB.justPressed():
            print('B Pressed')
            currentScreen = 'main'
    
    display.update()