sucursales,pacientes=map(int,input().split(' '))
while sucursales < 1:
    sucursales,pacientes=map(int,input().split(' '))
paciente_list = []
sucursal_list = []
sucursal = {}
for i in range(sucursales):
    sucursal['id'] = i + 1
    medicamento_var = int(input())
    while medicamento_var < 1:
        medicamento_var = int(input())
    sucursal['existencias'] =  medicamento_var
    sucursal_list.append(sucursal)
    sucursal = {} 
for i in range(pacientes):
    sucursal_pac,presion_1,presion_2=map(int,input().split(' '))
    while sucursal_pac < 1:
        sucursal_pac,presion_1,presion_2=map(int,input().split(' '))
    dosis = 0
    if presion_1 < 91 and presion_2 < 63:
        dosis = 12
    elif (presion_1 >= 91 and presion_1 < 134) and (presion_2 >= 63 and presion_2 < 77):
        dosis = 0
    elif (presion_1 >= 134 and presion_1 < 162) and (presion_2 >= 77 and presion_2 < 105):
        dosis = 0
    elif (presion_1 >= 162 and presion_1 < 188) and (presion_2 >= 105 and presion_2 < 119):
        dosis = 1
    elif (presion_1 >= 188 and presion_1 < 201) and (presion_2 >= 119 and presion_2 < 126):
        dosis = 8
    elif (presion_1 >= 201 and presion_1 < 214) and (presion_2 >= 126 and presion_2 < 146):
        dosis = 12
    elif presion_1 >= 214  and presion_2 >= 146 :
        dosis = 32
    elif presion_1 >= 152  and presion_2 < 79 :
        dosis = 20

    paciente_list.append({'paciente': i+1, 'sucursal': sucursal_pac, 'presion_sis': presion_1, 'presion_dias': presion_2, 'dosis': dosis})
totales = {}
totales_dosis = []
for h in range(sucursales):
    total_dosis = 0
    for p in paciente_list:
        if(p['sucursal'] == h+1):
            total_dosis = total_dosis + p['dosis']
    totales_dosis.append({'sucursal': h+1, 'total_entregado': total_dosis})
    
porcentajes = []

for k in totales_dosis: 
    for c in sucursal_list:
        if k['sucursal'] == c['id']:
            if k['total_entregado'] == 0: 
                porc = float(0.00)
            else:
                porc = (k['total_entregado'] * 100) / c['existencias']
                porc = round(porc,2)
    porcentajes.append({'sucursal': k['sucursal'], 'porcentaje': porc})

existencias_real = []

for k in totales_dosis: 
    for c in sucursal_list:
        if k['sucursal'] == c['id']:
             tot =  c['existencias'] - k['total_entregado']  
    existencias_real.append({'sucursal': k['sucursal'], 'existencia': tot})
    
existencias_real.sort(key=lambda x: x['existencia'], reverse=False)
print(existencias_real[0]['sucursal'],existencias_real[0]['existencia'])
print(existencias_real[-1]['sucursal'],existencias_real[-1]['existencia'])

for s in porcentajes:
    print(s['sucursal'], "{0:.2f}".format(s['porcentaje']) + "%")
    
    
    
    



    