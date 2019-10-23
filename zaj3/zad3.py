#Mamy labirynt 12x12 pól, przedstawiony na rysunku.
#Przez labirynt poruszamy się przesuwając z pola na pole (ruch: w lewo, prawo, do góry lub na dół).
#Nie możemy wchodzić na ściany (czarne pola).
#Naszym celem jest dojście z pola S, do pola E w maksymalnie 40 krokach. Czy istnieje taka droga?

labirynth =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0] ]