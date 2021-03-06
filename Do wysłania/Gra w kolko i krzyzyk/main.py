import time
import os
import game3x3
import game3x3bot
import game3x3time
import game3x3timebot
import game4x4
import game5x5

def zliczanie():
    global ulubionytryb #nie ma go w pliku
    global zagran # nie ma go w pliku
    global uruchomien
    global t11
    global t12
    global t13
    global t14
    global t20
    global t30
    ulubionytryb = 'Brak, pokaze sie wkrotce =]'
    if not os.path.exists('zliczenia.txt'):
        plikzliczenia = open('zliczenia.txt','w') #STRUKTURA PLIKU: uruchomien, kolejnetryby11, 12, 13, 21, 22 ... wszystko w innych wierszach
        plikzliczenia.write("0\n0\n0\n0\n0\n0\n0")
        plikzliczenia.close()
    plikzliczenia = open('zliczenia.txt', 'r')
    linie=plikzliczenia.readlines()
    plikzliczenia.close()
    uruchomien = int(linie[0])
    t11=int(linie[1])
    t12=int(linie[2])
    t13=int(linie[3])
    t14=int(linie[4])
    t20=int(linie[5])
    t30=int(linie[6])
    uruchomien += 1
    zapis_zliczen()

#Ustalanie ulubionego trybu gry
    if t11 > max(t12, t13, t14, t20, t30):
        ulubionytryb = '3x3 z przyjacielem'
    if t12 > max(t11, t13, t14, t20, t30):
        ulubionytryb = '3x3 z komputerem'
    if t13 > max(t11, t12, t14, t20, t30):
        ulubionytryb = '3x3 z przyjacielem na czas'
    if t14 > max(t11, t12, t13, t20, t30):
        ulubionytryb = '3x3 z komputerem na czas'
    if t20 > max(t11, t12, t13, t14, t30):
        ulubionytryb = '4x4 z przyjacielem'
    if t30 > max(t11, t12, t13, t14, t20):
        ulubionytryb = '5x5 z przyjacielem'
    zagran = t11 + t12 + t13 + t14 + t20 + t30


def zapis_zliczen():
    plikzliczenia = open('zliczenia.txt', 'w')
    plikzliczenia.write(str(uruchomien))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t11))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t12))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t13))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t14))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t20))
    plikzliczenia.write("\n")
    plikzliczenia.write(str(t30))
    plikzliczenia.close()


def statystyki_inicjalizacja():
    global wygrane_graczy
    wygrane_graczy = {}

    # --- File structure ---
    # [player name] [player wins]

    if not os.path.exists('statystyki.txt'):
        plik_statystyki = open('statystyki.txt', 'w')
        plik_statystyki.close()

    plik_statystyki = open('statystyki.txt', 'r')
    lines = plik_statystyki.readlines()
    plik_statystyki.close()

    for line in lines:
        line_data = line.split()
        wygrane_graczy[line_data[0]] = int(line_data[1])


def zapis_statystyki():
    plik_statystyki = open('statystyki.txt', 'w')
    plik_statystyki.truncate()
    for player, wins in wygrane_graczy.items():
        plik_statystyki.write(player + " " + str(wins) + "\n")
    plik_statystyki.close()

def wstep():
    print ('\n###################################\nProfesjonalna gra w kolko i krzyzyk\n###################################')
    if uruchomien == 10:
        print ('TO JUZ DZIESIATE URUCHOMIENIE =]')
    elif uruchomien == 100:
        print ('SETNE URUCHOMIENIE, MUSI CI SIE PODOBAC <3')
    elif uruchomien == 1000:
        print ('TYSIECZNE URUCHOMIENIE, TO JUZ BYCIE NERDEM XD')
    else:
        print ('Uruchomien:', uruchomien)
    print ('Lacznie zagranych partii:', zagran)
    print ('Ulubiony tryb gry:', ulubionytryb)
    print ('###################################')
    print ('Loading...')
    time.sleep(5)
    print("\n\n\n\n\n\n\n\n")


def main() :
    zliczanie()
    statystyki_inicjalizacja()
    wstep()
    tryb = 1 #dowolna wartosc rozna od zera zeby ponizsza petla sie wykonywala
    while tryb != 0 :
        global wygrane_graczy
        tryb = int(input('\nWybierz tryb gry:\n1 - Gra na planszy 3x3 dodatkowe funkcjonalnosci \n2 - Gra na planszy 4x4 w dwie osoby\n3 - Gra na planszy 5x5 w dwie osoby\n0 - Wyjscie\n'))
        if tryb == 1 :
            tryb1 = int (input('Wybrales gre 3x3, wybierz rodzaj\n1 - Z kolega \n2 - Z komputerem \n3 - Z kolega na czas\n4 - Z komputerem na czas\n0 - Cofnij\n'))
            if tryb1 == 0 :
                print ("Cofam...")
            elif tryb1 == 1 :
                print ('\nRozpoczynam gre na planszy 3x3 z przyjacielem\n')
                global t11
                gamesResult = game3x3.main()
                t11 += gamesResult.games_played
                for player, wins in gamesResult.players_winnings.items():
                    if player in wygrane_graczy:
                        wygrane_graczy[player] += wins
                    else:
                        wygrane_graczy[player] = wins
                zapis_zliczen()
                zapis_statystyki()
            elif tryb1 == 2:
                print ('Rozpoczynam gre na planszy 3x3 z komputerem')
                global t12
                gamesResult = game3x3bot.main()
                t12 += gamesResult.games_played
                for player, wins in gamesResult.players_winnings.items():
                    if player in wygrane_graczy:
                        wygrane_graczy[player] += wins
                    else:
                        wygrane_graczy[player] = wins
                zapis_zliczen()
                zapis_statystyki()
            elif tryb1 == 3:
                print ('Rozpoczynam gre na planszy 3x3 z przyjacielem na czas')
                global t13
                gamesResult = game3x3time.main()
                t13 += gamesResult.games_played
                for player, wins in gamesResult.players_winnings.items():
                    if player in wygrane_graczy:
                        wygrane_graczy[player] += wins
                    else:
                        wygrane_graczy[player] = wins
                zapis_zliczen()
                zapis_statystyki()
            elif tryb1 == 4 :
                print ('Rozpoczynam gre na planszy 3x3 z komputerem na czas')
                global t14
                gamesResult = game3x3timebot.main()
                t14 += gamesResult.games_played
                for player, wins in gamesResult.players_winnings.items():
                    if player in wygrane_graczy:
                        wygrane_graczy[player] += wins
                    else:
                        wygrane_graczy[player] = wins
                zapis_zliczen()
                zapis_statystyki()
        if tryb == 2 :
            print ('\nRozpoczynam gre na planszy 4x4\n')
            global t20
            gamesResult = game4x4.main()
            t20 += gamesResult.games_played
            for player, wins in gamesResult.players_winnings.items():
                if player in wygrane_graczy:
                    wygrane_graczy[player] += wins
                else:
                    wygrane_graczy[player] = wins
            zapis_zliczen()
            zapis_statystyki()
        if tryb == 3:
            print ('\nRozpoczynam gre na planszy 5x5\n')
            global t30
            gamesResult = game5x5.main()
            t30 += gamesResult.games_played
            for player, wins in gamesResult.players_winnings.items():
                if player in wygrane_graczy:
                    wygrane_graczy[player] += wins
                else:
                    wygrane_graczy[player] = wins
            zapis_zliczen()
            zapis_statystyki()
    print ('Zegnaj')
    exit(0)


if __name__ == '__main__':
    main()