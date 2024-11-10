import pgzrun
import random

TITLE = "gallaga"
WIDTH = 1200
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (65,105,225)
speed = 5
enemies = []
bullets = []
score = 0
direction = 1
for x in range(8):
    for y in range(4):
        enemy = Actor("bug")
        enemies.append(enemy)
        enemies[-1].x = 100 + 50*x
        enemies[-1].y = 80 + 50*y

ship = Actor("galaga")
ship.pos = (WIDTH//2, HEIGHT-50)

def draw():
    screen.clear()
    screen.fill(BLUE)
    ship.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    if len(enemies) == 0:
        game_over()
    
    display_score()
def update():
    global score, direction
    move_down = False
    if keyboard.left:
        if ship.x <= 50:
            ship.x = 50
        ship.x -= 5
    if keyboard.right:
        if ship.x >= WIDTH-50:
            ship.x = WIDTH-50
        ship.x += 5
    """if keyboard.space:
        global bullets
        bullet = Actor("bullet")
        bullets.append(bullet)
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y""" 
    for bullet in bullets:
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

def on_key_down(key):
    if key == keys.SPACE:
        global bullets 
        bullet = Actor("bullet")
        bullets.append(bullet)
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-50

def display_score():
    screen.draw.text("score:" + str(score), (50, 50))

def game_over():
    if score == 32:
        screen.draw.text("You won! Your score is:", str(score), (WIDTH//2 - 50, HEIGHT//2))
    else:
        screen.draw.text("Womp womp, you lost. Your score is:", str(score), (WIDTH//2 - 50, HEIGHT//2))
pgzrun.go()