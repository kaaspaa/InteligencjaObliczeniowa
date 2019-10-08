import os
import csv
import random

#a)
print("a)Sprawdź ścieżkę do „working directory” i ewentualnie ustaw ją na własną.")
cwd = os.getcwd()
print("working directory: ",cwd,"\n")

#b)
print("b)Pobierz ze strony i otwórz plik osoby.csv ze wskazaniem, że kolumny mają nagłówki, a separatorem jest przecinek. Następnie wyświetl tabelę danych.")
with open('osoby.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print("odp = \n")
    for row in csv_reader:
        print(row)
    print()

#c)
print("c)Wyświetl same imiona.")

with open('osoby.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[1])
print()

#d)
print("d)Wyświetl tylko dane kobiet.")
with open('osoby.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[2] is 'k':
            print(row)
print()

#e)
print("e)Wyświetl dane mężczyzn starszych niż 50 lat i zapisz je w osobnym pliku osoby2.csv.")
with open('osoby.csv') as csv_file:
    with open('osoby2.csv', 'w') as write_csv:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(write_csv)
        for row in csv_reader:
            line_number = 0
            if row[2] is 'm' and int(row[3]) > 50:
                print(row)
                for line in row:
                    write_csv.write(line)
                    if line_number < 3:
                        write_csv.write(",")
                    line_number += 1
                write_csv.write("\n")
    write_csv.close()
print()

#f)
print("f)Za pomocą odpowiedniej komendy podaj średni wiek osób.")
with open('osoby.csv') as csv_file:
    avg = 0.00
    n_of_rows = 0
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        try:
            avg += int(row[3])
            n_of_rows += 1
        except:
            avg=avg
    print("odp = ",avg/n_of_rows)
print()

#g)
print("g)Dodaj kolumnę o nazwie „wyplata” i uzupełnij ją losowymi liczbami z zakresu (2000,5000)")
with open('osoby.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rows = []
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            row.append("wyplata")
            line_count += 1

        else:
            row.append(random.randint(2000,5000))
            line_count += 1
        rows.append(row)
    for row in rows:
        print(row)
    print()
    
#h)
    print("\nh)Dodaj nowy rekord do tabeli: Jan Kowalski, wiek 30, wypłata 3000.") 
    temp_list = ["Kowalski", "Jan", "m", "30", 3000]
    rows.append(temp_list)
    for row in rows:
        print(row)
    print()
#i)
    print("i)Zapisz zmodyfikowaną tabelę do pliku osoby3.csv.") 
    with open('osoby3.csv', 'w') as write_csv:
        for row in rows:
            line_number = 0
            for value in row:
                write_csv.write(str(value))
                if line_number < 4:
                    write_csv.write(",")
                line_number += 1
            write_csv.write("\n")
    write_csv.close()
    print("zapisano")

