import time
import sys
from colorama import init, Fore, Style
import os

# Inisialisasi colorama
init(autoreset=True)

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def animasi_tulis(teks, warna=Fore.CYAN, delay_per_huruf=0.05):
    """Efek ketikan dengan warna"""
    hide_cursor()
    for huruf in teks:
        sys.stdout.write(warna + huruf + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay_per_huruf)
    print()
    show_cursor()
os.system('cls')
lirik = [
    ("Di kehidupan kedua", 1.5),
    ("semoga kau tak terlalu keras kepala", 2.5),
    ("Atau mungkin ini bukan yang pertama", 2.0),
    ("dan kita diberi kesempatan berubah", 2.9),
    ("Ku yakin nyawa kita bertautan", 2.5),
    ("khatam berbagai cobaan", 2.9),
    ("Selalu menertawakan ramalan bintang, kartu tarot,", 2.9),
    ("orang pintar pembaca nasib", 2.5),
    ("Namun aku bingung kenapa ku tak pergi", 2.5),
    ("Aku bingung kalian masih di sini", 2.3),
    ("Apa mungkin karena terlalu lama", 2.0),
    ("Apa benar 'tuk berbagi derita", 3.5),
    ("Mungkin nanti semua justru memburuk", 2.0),

]

#  animasi
for baris, jeda in lirik:
    animasi_tulis(baris, warna=Fore.CYAN, delay_per_huruf=0.05)
    time.sleep(jeda)
