var_1 = float(input())
var_2 = int(input())

if var_2 == 2:
    if var_1 <  12.2:
        print("Baja")
    elif var_1 >= 12.2 and var_1 <= 15.6:
        print("Normal")
    elif var_1 > 15.6:
        print("Alta")
elif var_2 == 1:
    if var_1 < 11.6:
        print("Baja")
    elif var_1 >= 11.6 and var_1 <= 15:
        print("Normal")
    elif var_1 > 15:
        print("Alta")
else:
    print("No es posible generar la alerta")
    