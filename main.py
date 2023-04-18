from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[2J"


def alarm(seconds):
    time_elapse = 0

    print(CLEAR)
    while time_elapse < seconds:
        time.sleep(1)
        time_elapse += 1

        time_left = seconds - time_elapse
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")


minutest = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))
total_seconds = minutest * 60 + seconds

alarm(total_seconds)
