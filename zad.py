from collections import Counter
import requests

def menu():
    print("1. Pobierz plik z internetu ")
    print("2. Zlicz liczbę liter w pobranym pliku ")
    print("3. Zlicz liczbę wyrazów w pliku ")
    print("4. Zlicz liczbę znaków interpunkcyjnych w pliku ")
    print("5. Zlicz liczbę zdań w pliku")
    print("6. Wygeneruj raport o użyciu liter (A-Z) ")
    print("7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt ")
    print("8. Wyjście z programu ")
    choice= int(input("Enter choice: "))
    if choice==1:
        url = "http://s3.zylowski.net/public/input/5.txt"
        r = requests.get(url)
        with open('file.txt', 'w') as file:
                file.write(r.text)
    elif choice==2:

        plik = open('file.txt')
        try:
            tekst = plik.read()
        finally:
            plik.close()

        num_of_char = len(tekst)
        print('Count in text file :', num_of_char)

    elif choice==3:
        plik = open('file.txt')
        try:
            tekst = plik.read()
        finally:
            plik.close()

        data = tekst.split(" ")
        num_of_char = len(data)
        print('Count in text file :', num_of_char)
    elif choice==4:
        try:
            #inst
        except FileNotFoundError:
            print("Something goes wrong, download file again")
    elif choice==5:
        plik = open('file.txt')
        try:
            tekst = plik.read()
        finally:
            plik.close()

        data = tekst.split(".")
        num_of_char = len(data)
        print('Count in text file :', num_of_char)
    elif choice==6:
        print("6")
    elif choice==7:
        print("7")
        exit()
    else:
        print("Invalid choice")
    menu()

menu()
