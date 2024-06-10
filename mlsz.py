import tkinter as tk
import time
import winsound

# Ustaw parametry
tempo = 100  # Uderzenia na minutę (BPM)
czas_trwania_taktu = 60 / tempo  # Czas trwania jednego taktu (w sekundach)
liczba_uderzen_w_takcie = 4  # Liczba uderzeń w takcie

# Dźwięki
uderzenie_wysokie = 800  # Częstotliwość dźwięku wysokiego (Hz)
uderzenie_niskie = 400  # Częstotliwość dźwięku niskiego (Hz)

# Tworzenie okna GUI
okno = tk.Tk()
okno.title("Metronom wizualny")

# Tworzenie ramki sterowania
ramka_sterowania = tk.Frame(okno)
ramka_sterowania.pack()

# Etykieta tempa
etykieta_tempo = tk.Label(ramka_sterowania, text="Tempo:")
etykieta_tempo.pack()

# Suwak tempa
suwak_tempo = tk.Scale(ramka_sterowania, from_=40, to=200, orient=tk.HORIZONTAL)
suwak_tempo.pack()

# Przycisk start/stop
przycisk_start_stop = tk.Button(ramka_sterowania, text="Start")
przycisk_start_stop.pack()

# Tworzenie ramki metronomu
ramka_metronomu = tk.Frame(okno)
ramka_metronomu.pack()

# Płótno do rysowania koła
canvas = tk.Canvas(ramka_metronomu, width=200, height=200)
canvas.pack()

# Zmienne do rysowania koła
promien = 100
x = canvas.winfo_width() / 2
y = canvas.winfo_height() / 2
kolor_akcentowany = "red"
kolor_pozostale = "gray"

# Funkcja rysowania koła
def rysuj_kolo(promien, kolor):
    canvas.delete("all")
    canvas.oval(x - promien, y - promien, x + promien, y + promien, fill=kolor)

# Funkcja metronomu
def metronom():
    global tempo, czas_trwania_taktu, liczba_uderzen_w_takcie, \
           uderzenie_wysokie, uderzenie_niskie, \
           promien, x, y, kolor_akcentowany, kolor_pozostale

    # Aktualizacja tempa z suwaka
    tempo = suwak_tempo.get()
    czas_trwania_taktu = 60 / tempo

    while True:
        for _ in range(liczba_uderzen_w_takcie):
            # Rysuj koło akcentowane
            rysuj_kolo(promien, kolor_akcentowany)
            winsound.Beep(uderzenie_wysokie, czas_trwania_taktu / 2)
            time.sleep(czas_trwania_taktu / 2)

            # Rysuj koło pozostałe
            rysuj_kolo(promien, kolor_pozostale)
            winsound.Beep(uderzenie_niskie, czas_trwania_taktu / 2)
            time.sleep(czas_trwania_taktu / 2)

# Uruchomienie metronomu po kliknięciu przycisku "Start"
def start_metronom():
    przycisk_start_stop.config(text="Stop", command=stop_metronom)
    metronom()

# Zatrzymanie metronomu
def stop_metronom():
    przycisk_start_stop.config(text="Start", command=start_metronom)

# Podpięcie funkcji do przycisków
przycisk_start_stop.config(command=start_metronom)

# Uruchomienie GUI
okno.mainloop()
