from collections import Counter

def menu():
    print("1. Pobierz plik z internetu ")
    print("2. Zlicz liczbę liter w pobranym pliku ")
    print("3. Zlicz liczbę wyrazów w pliku ")
    print("4. Zlicz liczbę znaków interpunkcyjnych w pliku ")
    print("5. Wygeneruj raport o użyciu liter (A-Z) ")
    print("6. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt ")
    print("7. Wyjście z programu ")
    choice= int(input("Enter choice: "))
    if choice==1:
        try:
            file = open("C:\data.txt", "r")
            cont = file.read()

            #sobota
    elif choice==2:
        print("")
    elif choice==3:
        print("3")
    elif choice==4:
        try:
            #instructions
        except FileNotFoundError:
            print("Something goes wrong, download file again")
    elif choice==5:
        print("5")
    elif choice==6:
        print("6")
    elif choice==7:
        print("7")
        exit()
    else:
        print("Invalid choice")
    menu()

menu()
