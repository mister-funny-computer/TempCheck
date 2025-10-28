while True:
    while True:
        temp = int(input("Какая сейчас температура воздуха ? "))
        if temp <= 0:
            print("прохладно")
        elif 0 < temp <= 12:
            print("чуть теплее нуля")