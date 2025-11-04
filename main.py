while True:
    while True:
        temp = int(input("Какая сейчас температура воздуха ? "))
        if temp <= 0:
            print("прохладно")
        elif 0 < temp <= 12:
            print("чуть теплее нуля")
        elif 12 < temp <= 18:
            print("тeпло")
        elif 18 < temp <= 25:
            print("теплее тёплого")
        elif 25 < temp <= 32:
            print("Жарко")
        elif temp > 32:
            print("Умираю от жары не от холода ")