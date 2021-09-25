print("          MOVIE TICKETING")
print("A - Avengers: Endgame      B- Gozilla vs Kong")
print("C - Fast and Furious 9     D- Liong King")
print("")
print(" Rated PG-13: Parents strongly cautioned")
print("Some material may be inappropriate for children under 13")
print("Ticket Price : Php 200")
print("Ages below 7 has 100'%' discount")
print("Ages 8-18 has 10'%' discount")
print("Ages 60 above has 15'%' discount")
mov=str(input("Selec Movie: "))
age=int(input("Age: "))
if (mov=='A' or mov=='a'):
    if (age<=7):
        tp=0
    elif (age>=8 and age<=18):
        d=200*.10
        tp=200-d
    elif (age>=19 and age<=59):
        tp=200
    else:
        d=200*.15
        tp=200-d
    print("MOVIE A - Avengers: Endgame")
    print("Age: ", age)
    print("Ticket Price : ",tp)

elif (mov=='B' or mov=='b'):
    if (age<=7):
        tp=0
    elif (age>=8 and age<=18):
        d=200*.10
        tp=200-d
    elif (age>=19 and age<=59):
        tp=200
    else:
        d=200*.15
        tp=200-d
    print("MOVIE B- Godzilla vs Kong")
    print("Age: ", age)
    print("Ticket Price : ",tp)
elif (mov=='C' or mov=='c'):
    if (age<=7):
        tp=0
    elif (age>=8 and age<=18):
        d=200*.10
        tp=200-d
    elif (age>=19 and age<=59):
        tp=200
    else:
        d=200*.15
        tp=200-d
    print("MOVIE C - Fast and Furious 9 ")
    print("Age: ", age)
    print("Ticket Price : ",tp)
elif (mov=='D' or mov=='d'):
    if (age<=7):
        tp=0
    elif (age>=8 and age<=18):
        d=200*.10
        tp=200-d
    elif (age>=19 and age<=59):
        tp=200
    else:
        d=200*.15
        tp=200-d
    print("MOVIE D - Lion King ")
    print("Age: ", age)
    print("Ticket Price : ",tp)
else:
    print("Invalid Input")



