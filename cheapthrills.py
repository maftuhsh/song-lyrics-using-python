import time
from threading import Thread, Lock
import sys

# Lirik lagu dan kecepatan animasi per baris
lyrics = [
    ("Just trust me, you'll be fine", 0.09),
    ("And when I'm back in Chicago, I feel it", 0.09),
    ("Another version of me, I was in it", 0.09),
    ("I wave goodbye to the end of beginning", 0.08),
    ("Goodbye, goodbye, goodbye, goodbye", 0.08),
]

# Delay waktu tampilnya tiap baris
delays = [0, 0.5, 11.0, 17.0, 20.8]

# Kunci agar tidak tumpang tindih output antar thread
print_lock = Lock()

# Fungsi untuk animasi ketik karakter demi karakter
def animate_text(text, speed=0.1):
    with print_lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()  # newline setelah selesai

# Fungsi untuk tiap thread menyanyikan baris lirik
def sing_lyric(text, delay, speed):
    time.sleep(delay)
    animate_text(text, speed)

# Fungsi utama menjalankan semua thread
def sing_song():
    threads = []
    for i in range(len(lyrics)):
        line, speed = lyrics[i]
        delay = delays[i]
        t = Thread(target=sing_lyric, args=(line, delay, speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Mulai program
if __name__ == "__main__":
    sing_song()
