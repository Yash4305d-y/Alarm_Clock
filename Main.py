from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alaram(seconds):
    time_elapsed = 0 
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left  = seconds - time_elapsed
        minute_left = time_left // 60 
        second_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in {minute_left:02d}:{second_left:02d}") 
    
    
    playsound("alaram.mp3")

    # Colorful flashing WAKE UP 
    
    colors = ["\033[1;31m", "\033[1;33m", "\033[1;32m", "\033[1;34m", "\033[1;35m"]
    for i in range(10):
        color = colors[i % len(colors)]
        print(color + "WAKE UP! WAKE UP! WAKE UP!\033[0m")
        time.sleep(0.5)


minutes = int(input("How many minutes u want to wait: "))
seconds = int(input("How many seconds u want to wait: "))
total_seconds = minutes * 60 + seconds

alaram(total_seconds)
