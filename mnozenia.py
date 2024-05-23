import math
import time

def gcd(a, b):
    while b != 0:  # Dopóki b nie jest równa 0
        a, b = b, a % b  # Aktualizuj a na b, a b na resztę z dzielenia a przez b
    return a

def modInverse(a, m):
    return pow(a, -1, m)  # Oblicz odwrotność a modulo m

def montgomeryMultiplication(a, b, N, R, R_inverse):
    result = 0
    while b > 0:  # Dopóki b jest większe od 0
        if b & 1:  # Jeśli ostatni bit b jest równy 1
            result = (result + a) % N  # Dodaj a do wyniku modulo N
        a = (a << 1) % N  # Przesuń a o 1 bit w lewo i zastosuj operację modulo N
        if a >= N:  # Jeśli a jest większe lub równe N
            a = (a - N) % N  # Odejmij N od a i zastosuj operację modulo N
        b = b >> 1  # Przesuń b o 1 bit w prawo
    t = (result * R_inverse) % N  # Oblicz t jako iloczyn wyniku i odwrotności R modulo N
    if t < 0:  # Jeśli t jest mniejsze od 0
        t += N  # Dodaj N do t
    return t

def multiplication_modulo(A, B, Modulo):
    result = (A * B) % Modulo  # Oblicz iloczyn A i B modulo Modulo
    return result

def findBestR(N):
    R = 1
    while R <= N:  # Dopóki R jest mniejsze lub równe N
        R = R << 1  # Przesuń R o 1 bit w lewo
    while gcd(R, N) != 1:  # Dopóki największy wspólny dzielnik R i N nie jest równy 1
        R += 1  # Zwiększ R o 1
    return R

if __name__ == "__main__":
    A = int(input("Podaj liczbę A: "))  # Wczytaj liczbę A
    B = int(input("Podaj liczbę B: "))  # Wczytaj liczbę B
    Modulo = int(input("Podaj modulo: "))  # Wczytaj modulo
    R = findBestR(Modulo)  # Znajdź najlepszą wartość R dla danego modulo
    if gcd(R, Modulo) != 1:  # Jeśli największy wspólny dzielnik R i Modulo nie jest równy 1
        print("R i Modulo nie są względnie pierwsze!")  # Wyświetl komunikat o nieprawidłowej wartości R i Modulo
        exit(1)  # Zakończ program z kodem błędu
    R_inverse = modInverse(R, Modulo)  # Oblicz odwrotność R modulo Modulo
    print("R:", R)  # Wyświetl wartość R
    start_time2 = time.perf_counter()  # Rozpocznij pomiar czasu
    result = multiplication_modulo(A, B, Modulo)  # Oblicz wynik mnożenia A i B modulo Modulo
    end_time2 = time.perf_counter()  # Zakończ pomiar czasu
    print("Wynik mnożenia modulo:", result)  # Wyświetl wynik mnożenia modulo
    print("Czas wykonania mnożenia modulo:", (end_time2 - start_time2) * 1000000, "microsekund")  # Wyświetl czas wykonania mnożenia modulo
    start_time = time.perf_counter()  # Rozpocznij pomiar czasu
    A_mont = (A * R) % Modulo  # Przekształć liczbę A do postaci Montgomery'ego
    B_mont = (B * R) % Modulo  # Przekształć liczbę B do postaci Montgomery'ego
    result_mont = montgomeryMultiplication(A_mont, B_mont, Modulo, R, R_inverse)  # Wykonaj mnożenie Montgomery'ego
    result = montgomeryMultiplication(result_mont, 1, Modulo, R, R_inverse)  # Wykonaj konwersję wyniku Montgomery'ego
    end_time = time.perf_counter()  # Zakończ pomiar czasu

    print("Wynik w postaci liczby Montgomery'ego:", result_mont)  # Wyświetl wynik w postaci liczby Montgomery'ego
    print("Wynik Montgomery'ego:", result)  # Wyświetl wynik Montgomery'ego
    print("Czas wykonania Montgomery'ego:", (end_time - start_time) * 1000000, "microsekund")  # Wyświetl czas wykonania Montgomery'ego
