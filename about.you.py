import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:  
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)  
    animate_text(lyric, speed)  

def sing_song():
    lyrics = [
        ("do you think i have forgetten?", 0.1),
        ("do you think i have forgetten?", 0.1),
        ("do you think i have forgetten?", 0.1),
        ("about you?", 0.2),
        ("there was something bout you that now i can't remember", 0.08),
        ("its the same damn thing that made my heart surrender", 0.1),
        ("and i miss you on a train, i miss you in the morning", 0.1),
        ("i never know what to think about", 0.1),
        ("i think about youuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", 0.1),
    ]
    delay = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delay[i], speed))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()

