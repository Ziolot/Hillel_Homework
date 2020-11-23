def convert_temp():
    if scale == 1:
        return fck()
    elif scale == 2:
        return cfk()
    elif scale == 3:
        return kcf()
    else:
        print("Needs to be 1 or 2 or 3!")


def cfk():
    c = float(input(" Enter Celsius (Degree) : "))
    f = ((9 * c) / 5) + 32
    k = c - 273
    print(" Temperature : ", c, " Degree Celsius & ", f, " Degree Fahrenheit & ", k, " Kelvin")


def fck():
    f = float(input(" Enter Fahrenheit (Degree) : "))
    c = (5 * (f - 32)) / 9
    k = c - 273
    print(" Temperature : ", round(c, 3), " Degree Celsius & ", f, " Degree Fahrenheit & ", round(k, 3), " Kelvin")


def kcf():
    k = float(input(" Enter Kelvin : "))
    c = k - 273
    f = ((9 * c) / 5) + 32
    print(" Temperature : ", c, " Degree Celsius & ", f, " Degree Fahrenheit & ", k, " Kelvin")


scale = int(input("Select Fahrenheit=1, Celsius=2 or Kelvin=3: "))
convert_temp()