import time
from PIL import ImageGrab
import pyautogui

bg_color = (247,247,247)
dino_color = (83,83,83)


def capture_screen():
    screen = ImageGrab.grab()
    return screen

def detect_obstacle(screen):
    for x in range(380, 410):
        for y in range(580, 720):
            color = screen.getpixel((x , y))
            if color == (83, 83, 83):
                return True

def jump():
    pyautogui.press("up")

print ("start in 2 seconds")
time.sleep(2)

while True:
    screen = capture_screen()
    if detect_obstacle(screen):
        jump()
