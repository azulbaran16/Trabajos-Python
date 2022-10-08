pacientes = int(input())
i = 1 
hombres_baja = 0
hombres_alta = 0
hombres_normal = 0
mujeres_baja = 0
mujeres_alta = 0
mujeres_normal = 0
while  i <= pacientes:
    var_1 = float(input())
    genero = int(input())
    
    while genero != 1 and genero != 2:
        genero = int(input())
        
    if genero == 1:
        if var_1 <  12.2:
            mujeres_baja += 1
        elif var_1 >= 12.2 and var_1 <= 15.6:
            mujeres_normal += 1
        elif var_1 > 15.6:
            mujeres_alta += 1 
    elif genero == 2:
        if var_1 < 11.6:
          hombres_baja += 1
        elif var_1 >= 11.6 and var_1 <= 15:
          hombres_normal += 1
        elif var_1 > 15:
          hombres_alta += 1
    i=i+1
print(hombres_baja,hombres_alta,hombres_normal,mujeres_baja,mujeres_alta,mujeres_normal)
