import time
import basicnobot
def Wstep () :
    print ('\n###################################\nProfesjonalna gra w kolko i krzyzyk\n###################################')
    print ('Uruchomien: ')
    print ('Lacznie zagranych partii: ')
    print ('Ulubiony tryb gry: ', end="")
    print ('Przykladowy tryb gry') #DO ZMIANY!!!!!!!!!!!!
    print ('###################################')
    print ('Loading...')
    time.sleep(5)
def main() :
    Wstep() #Mozna zakomentowac zeby nie czekac
    tryb =1
    while (tryb != 0) :
        tryb = int(input('\n\n\n\n\n\n\nWybierz tryb gry:\n1 - Gra na planszy 3x3 \n2 - \n0 - Wyjscie\n'))
        if (tryb == 1) :
            tryb2 = int (input('Wybrales gre 3x3, wybierz rodzaj\n1 - Z kolega \n2 - Z komputerem \n0 - Cofnij\n'))
            if (tryb2 == 0) :
                print ("Cofam...")
            elif (tryb2 == 1) :
                print ('\nRozpoczynam gre na planszy 3x3 bez bota\n')
                basicnobot.main()
            elif (tryb2 == 2) :
                print ('Gra z botem niezaimplementowana') #3x3 GRA Z KOMPUTEREM TO DO
    #zapis do pliku
    print ('Zegnaj')
    exit(0)
if __name__ == '__main__' :
    main()
