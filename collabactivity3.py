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
    print("")
    print("Choose your snack")
    print("")
    print("1. Popcorn with Drinks")
    print("2. Hotdog with Drinks")
    print("3. Chips with Drinks")
    print("")
    snack=int(input("Enter here: "))
    print("")

    if snack == 1:
        print("Choose a size")
        print("")
        print("1. Large")
        print("2. Medium")
        print("3. Small")
        print("")
        size=int(input("Enter here: "))
        print("")
        if size == 1:
            print("Your snack is a Large size Popcorn with Drinks")
            fee = 180
        elif size == 2:
            print ("Your snack is a Medium size Popcorn with Drinks")
            fee = 130
        elif size == 3:
            print ("Your snack is a Small size Popcorn with Drinks")
            fee = 70
        else: 
            print ("Invalid Input")

    elif snack == 2:
        print ("Choose your Hotdog")
        print ("")
        print ("1. Original")
        print ("2. Footlong")
        print ("3. Hotdog with Cheese")
        print ("4. Jumbo Hotdog")
        print ("")
        type=int(input("Enter here: "))
        print ("")
        if type == 1:
            print ("Your snack is a Hotdog with Drinks")
            fee = 60
        elif type == 2:
            print ("Your snack is a Footlong with Drinks")
            fee = 100
        elif type == 3:
            print ("Your snack is a Hotdog with cheese with Drinks")
            fee = 70
        elif type == 4:
            print ("Youe snack is a Jumbo Hotdog with Drinks")
            fee = 80
        else:
            print ("Invalid Input")

    elif snack == 3:
        print ("Choose Your Chips")
        print ("")
        print ("1. Piatos")
        print ("2. Nova")
        print ("3. V-cut" )
        print("")
        chips = int(input("Enter Here: "))
        if chips == 1:
            print ("Your snacks is a Piatos with drinks")
            fee = 60
        elif chips == 2:
            print ("Your snacks is a Nova with drinks")
            fee = 60
        elif chips == 3:
            print ("Your snack is a V-cut with drinks")
            fee = 60

    else:
        print("Invalid Input")

    ff =(tp+fee)

    print("MOVIE A - Avengers: Endgame")
    print("Age: ", age)
    print("Ticket Price : ",tp)
    print ("Your Total Fee is {} ".format(tp+fee))


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
    print("")
    print("Choose your snack")
    print("")
    print("1. Popcorn with Drinks")
    print("2. Hotdog with Drinks")
    print("3. Chips with Drinks")
    print("")
    snack=int(input("Enter here: "))
    print("")

    if snack == 1:
        print("Choose a size")
        print("")
        print("1. Large")
        print("2. Medium")
        print("3. Small")
        print("")
        size=int(input("Enter here: "))
        print("")
        if size == 1:
            print("Your snack is a Large size Popcorn with Drinks")
            fee = 180
        elif size == 2:
            print ("Your snack is a Medium size Popcorn with Drinks")
            fee = 130
        elif size == 3:
            print ("Your snack is a Small size Popcorn with Drinks")
            fee = 70
        else: 
            print ("Invalid Input")

    elif snack == 2:
        print ("Choose your Hotdog")
        print ("")
        print ("1. Original")
        print ("2. Footlong")
        print ("3. Hotdog with Cheese")
        print ("4. Jumbo Hotdog")
        print ("")
        type=int(input("Enter here: "))
        print ("")
        if type == 1:
            print ("Your snack is a Hotdog with Drinks")
            fee = 60
        elif type == 2:
            print ("Your snack is a Footlong with Drinks")
            fee = 100
        elif type == 3:
            print ("Your snack is a Hotdog with cheese with Drinks")
            fee = 70
        elif type == 4:
            print ("Youe snack is a Jumbo Hotdog with Drinks")
            fee = 80
        else:
            print ("Invalid Input")

    elif snack == 3:
        print ("Choose Your Chips")
        print ("")
        print ("1. Piatos")
        print ("2. Nova")
        print ("3. V-cut" )
        print("")
        chips = int(input("Enter Here: "))
        if chips == 1:
            print ("Your snacks is a Piatos with drinks")
            fee = 60
        elif chips == 2:
            print ("Your snacks is a Nova with drinks")
            fee = 60
        elif chips == 3:
            print ("Your snack is a V-cut with drinks")
            fee = 60

    else:
        print("Invalid Input")

    ff =(tp+fee)
    print("MOVIE B- Godzilla vs Kong")
    print("Age: ", age)
    print("Ticket Price : ",tp)
    print ("Your Total Fee is {} ".format(tp+fee))
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
    print("")
    print("Choose your snack")
    print("")
    print("1. Popcorn with Drinks")
    print("2. Hotdog with Drinks")
    print("3. Chips with Drinks")
    print("")
    snack=int(input("Enter here: "))
    print("")

    if snack == 1:
        print("Choose a size")
        print("")
        print("1. Large")
        print("2. Medium")
        print("3. Small")
        print("")
        size=int(input("Enter here: "))
        print("")
        if size == 1:
            print("Your snack is a Large size Popcorn with Drinks")
            fee = 180
        elif size == 2:
            print ("Your snack is a Medium size Popcorn with Drinks")
            fee = 130
        elif size == 3:
            print ("Your snack is a Small size Popcorn with Drinks")
            fee = 70
        else: 
            print ("Invalid Input")

    elif snack == 2:
        print ("Choose your Hotdog")
        print ("")
        print ("1. Original")
        print ("2. Footlong")
        print ("3. Hotdog with Cheese")
        print ("4. Jumbo Hotdog")
        print ("")
        type=int(input("Enter here: "))
        print ("")
        if type == 1:
            print ("Your snack is a Hotdog with Drinks")
            fee = 60
        elif type == 2:
            print ("Your snack is a Footlong with Drinks")
            fee = 100
        elif type == 3:
            print ("Your snack is a Hotdog with cheese with Drinks")
            fee = 70
        elif type == 4:
            print ("Youe snack is a Jumbo Hotdog with Drinks")
            fee = 80
        else:
            print ("Invalid Input")

    elif snack == 3:
        print ("Choose Your Chips")
        print ("")
        print ("1. Piatos")
        print ("2. Nova")
        print ("3. V-cut" )
        print("")
        chips = int(input("Enter Here: "))
        if chips == 1:
            print ("Your snacks is a Piatos with drinks")
            fee = 60
        elif chips == 2:
            print ("Your snacks is a Nova with drinks")
            fee = 60
        elif chips == 3:
            print ("Your snack is a V-cut with drinks")
            fee = 60

    else:
        print("Invalid Input")

    ff =(tp+fee)
    print("MOVIE C - Fast and Furious 9 ")
    print("Age: ", age)
    print("Ticket Price : ",tp)
    print ("Your Total Fee is {} ".format(tp+fee))
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
    print("")
    print("Choose your snack")
    print("")
    print("1. Popcorn with Drinks")
    print("2. Hotdog with Drinks")
    print("3. Chips with Drinks")
    print("")
    snack=int(input("Enter here: "))
    print("")

    if snack == 1:
        print("Choose a size")
        print("")
        print("1. Large")
        print("2. Medium")
        print("3. Small")
        print("")
        size=int(input("Enter here: "))
        print("")
        if size == 1:
            print("Your snack is a Large size Popcorn with Drinks")
            fee = 180
        elif size == 2:
            print ("Your snack is a Medium size Popcorn with Drinks")
            fee = 130
        elif size == 3:
            print ("Your snack is a Small size Popcorn with Drinks")
            fee = 70
        else: 
            print ("Invalid Input")

    elif snack == 2:
        print ("Choose your Hotdog")
        print ("")
        print ("1. Original")
        print ("2. Footlong")
        print ("3. Hotdog with Cheese")
        print ("4. Jumbo Hotdog")
        print ("")
        type=int(input("Enter here: "))
        print ("")
        if type == 1:
            print ("Your snack is a Hotdog with Drinks")
            fee = 60
        elif type == 2:
            print ("Your snack is a Footlong with Drinks")
            fee = 100
        elif type == 3:
            print ("Your snack is a Hotdog with cheese with Drinks")
            fee = 70
        elif type == 4:
            print ("Youe snack is a Jumbo Hotdog with Drinks")
            fee = 80
        else:
            print ("Invalid Input")

    elif snack == 3:
        print ("Choose Your Chips")
        print ("")
        print ("1. Piatos")
        print ("2. Nova")
        print ("3. V-cut" )
        print("")
        chips = int(input("Enter Here: "))
        if chips == 1:
            print ("Your snacks is a Piatos with drinks")
            fee = 60
        elif chips == 2:
            print ("Your snacks is a Nova with drinks")
            fee = 60
        elif chips == 3:
            print ("Your snack is a V-cut with drinks")
            fee = 60

    else:
        print("Invalid Input")

    ff =(tp+fee)
    print("MOVIE D - Lion King ")
    print("Age: ", age)
    print("Ticket Price : ",tp)
    print ("Your Total Fee is {} ".format(tp+fee))
else:
    print("Invalid Input")






