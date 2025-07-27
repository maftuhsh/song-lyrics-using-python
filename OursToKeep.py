import time
import sys

# Fungsi untuk mengetik lirik satu karakter
def type_lyric(text, typing_speed=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print()  # ganti baris setelah selesai

# Fungsi untuk nyanyi tiap lirik (pakai delay setelah baris selesai)
def sing_lyric(line, delay=2.5):
    type_lyric(line)
    time.sleep(delay)

# Header
print("\n🎵 Playing: Ours to Keep - Kendis 🎵\n")
time.sleep(1)

# Lirik lagu dengan animasi
sing_lyric("Do you ever feel the need to get away from me?", delay=3.0)
sing_lyric("Do I bore you?", delay=2.5)
sing_lyric("Or do you want to take me from this crowded place to", delay=3.2)
sing_lyric("Somewhere we can find some peace", delay=2.8)
sing_lyric("And the world is ours to keep", delay=3.0)

# Penutup
type_lyric("\n🎶 End of snippet 🎶", typing_speed=0.08)
