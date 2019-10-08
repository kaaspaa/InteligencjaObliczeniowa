import sys
import random
import statistics

def sumuj(a,b):
    s = a + b
    return s

def losuj(a,b):
    if a<b:
        return random.randint(a,b)
    else:
        return random.randint(b,a)

def standaryzuj(v):
    mean = statistics.mean(v)
    stdev = statistics.stdev(v)
    answ = []
    for value in v:
        answ.append((value-mean)/stdev)
    return answ

def wyszukaj1(v,x):
    num = 0
    for n in v:
        if n > x:
            num += 1
    return num

def wyszukaj2(v,x):
    num = 0
    i = 0
    while i < len(v):
        if v[i] > x:
            num += 1
        i += 1
    return num

option = 0
while option <1 or option >6:
    print("wybierz opcje:\n",
            "1 - sumuj\n",
            "2 - losuj\n",
            "3 - standaryzuj\n",
            "4 - normalizuj\n",
            "5 - wyszukaj(z 'for')\n",
            "6 - wyszukaj(bez 'for')")
    try: 
        option = int(input())
    except:
        print("musisz podac liczbe calkowita")
if option == 1:
    if len(sys.argv) is 3:
        print("suma ", sys.argv[1], "+ ", sys.argv[2], " = ", sumuj(int(sys.argv[1]),int(sys.argv[2])))
    else:
        print("suma 12 + 30 = ", sumuj(12,30))
elif option == 2:
    if len(sys.argv) is 3:
        print("losowa liczba w przedziale ", sys.argv[1], "/", sys.argv[2], " to:", losuj(int(sys.argv[1]),int(sys.argv[2])))
    else:   
        num1 = 0
        num2 = 0
        print("podaj 1 liczbe: ")
        try:
            num1 = int(input())
        except:
            print("Trzeba bylo podac liczbe...")
            sys.exit()
        print("podaj 2 liczbe: ")
        try:
            num2 = int(input())
        except:
            print("Trzeba bylo podac liczbe...")
            sys.exit()
        print("losowa liczba w przedziale ", num1, "/", num2, " to:", losuj(num1,num2))
elif option == 3:
    option2 = 0
    vect_v = []
    while option2 == 0:
        print("dodaj liczbe do wektora ")
        try:
            vect_v.append(int(input()))
        except:
            print("podaj liczbe calkowita")
        print("twoj wektor: ", vect_v)
        if len(vect_v) != 0:
            print("czy chcesz dodac liczbe do twojego wektora?(y = tak, cokolwiek innego = nie)")
            o = input()
            if o != "y":
                option2 = 1
                print("wynik funkcji standaryzuj to: ", standaryzuj(vect_v))


elif option == 4:
    #nie wiem
    sys.exit()
elif option == 5:
    option2 = 0
    vect_v = []
    x = "a"
    while option2 == 0:
        print("dodaj liczbe do wektora ")
        try:
            vect_v.append(int(input()))
        except:
            print("podaj liczbe calkowita")
        print("twoj wektor: ", vect_v)
        if len(vect_v) != 0:
            print("czy chcesz dodac liczbe do twojego wektora?(y = tak, cokolwiek innego = nie)")
            o = input()
            if o != "y":
                option2 = 1
                while isinstance(x,int) is False:
                        print("podaj szukana wartosc 'x'")
                        try:
                            x = int(input())
                        except:
                            print("x musi byc liczba calkowita")
                print("wynik funkcji 'wyszukaj' to: ", wyszukaj1(vect_v,x))
elif option == 6:
    option2 = 0
    vect_v = []
    x = "a"
    while option2 == 0:
        print("dodaj liczbe do wektora ")
        try:
            vect_v.append(int(input()))
        except:
            print("podaj liczbe calkowita")
        print("twoj wektor: ", vect_v)
        if len(vect_v) != 0:
            print("czy chcesz dodac liczbe do twojego wektora?(y = tak, cokolwiek innego = nie)")
            o = input()
            if o != "y":
                option2 = 1
                while isinstance(x,int) is False:
                        print("podaj szukana wartosc 'x'")
                        try:
                            x = int(input())
                        except:
                            print("x musi byc liczba calkowita")
                print("wynik funkcji 'wyszukaj' to: ", wyszukaj1(vect_v,x))

