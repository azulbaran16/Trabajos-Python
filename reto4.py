sucursales,tipo,pacientes=map(int,input().split(' '))
while sucursales < 1 or tipo < 1:
    sucursales,tipo,pacientes=map(int,input().split(' '))
paciente_list = []
sucursal_list = []
sucursal = {}
for i in range(sucursales):

    medicamento_var = input().split(' ')
    cont = 1
    for n in medicamento_var:
        sucursal['id'] = i + 1
        sucursal['tipo'] = cont
        sucursal['existencias'] = int(n)
        sucursal_list.append(sucursal)
        cont = cont + 1
        sucursal = {} 
    # print(sucursal_list)
    
entrega_final = []
programadas_sucu = []    
for i in range(pacientes):
    sucursal_pac,tipo_med,existencias_sol,presion_1,presion_2=map(int,input().split(' '))
    while sucursal_pac < 1:
        sucursal_pac,presion_1,presion_2=map(int,input().split(' '))
    entrega = False
    if presion_1 < 91 and presion_2 < 63:
        entrega = True
    elif (presion_1 >= 91 and presion_1 < 134) and (presion_2 >= 63 and presion_2 < 77):
        entrega = False
    elif (presion_1 >= 134 and presion_1 < 162) and (presion_2 >= 77 and presion_2 < 105):
        entrega = False
    elif (presion_1 >= 162 and presion_1 < 188) and (presion_2 >= 105 and presion_2 < 119):
        entrega = True
    elif (presion_1 >= 188 and presion_1 < 201) and (presion_2 >= 119 and presion_2 < 126):
        entrega = True
    elif (presion_1 >= 201 and presion_1 < 214) and (presion_2 >= 126 and presion_2 < 146):
        entrega = True
    elif presion_1 >= 214  and presion_2 >= 146 :
        entrega = True
    elif presion_1 >= 152  and presion_2 < 79 :
        entrega = True

    if sucursal_pac > sucursales:
        entrega = False
    if tipo_med > tipo:
        entrega = False
    if existencias_sol < 0:
        entrega = False
    
    entrega_final.append({'sucursal': sucursal_pac, 'tipo': tipo_med, 'cantidad_med': existencias_sol, 'programada': entrega})

for n in sucursal_list:
    for c in entrega_final:
        if c['sucursal'] == n['id']:
            if c['tipo'] == n['tipo']:
                if c['programada'] == True:
                    n['existencias'] = n['existencias'] - c['cantidad_med']

sucursal_list.sort(key=lambda x: x['existencias'], reverse=False)

prom_entregadas = []
paciente_sucu = []
entrega_final.sort(key=lambda x: x['cantidad_med'], reverse=False)
for s in entrega_final:
    for n in range(sucursales):

        for k in range(tipo):
            if n+1 == s['sucursal'] and s['tipo'] == k+1:
                if s['programada']:
                    programadas_sucu.append({'sucursal': s['sucursal'], 'tipo': s['tipo'], 'cantidad': s['cantidad_med']})
                    prom_entregadas.append({'sucursal': s['sucursal'], 'tipo': s['tipo'], 'cantidad': s['cantidad_med']})
            else:
                programadas_sucu.append({'sucursal': n+1, 'tipo': k+1, 'cantidad': 0})
                
# res = min(entrega_final, key= lambda x: x['cantidad_med'])
for n in range(sucursales):
    cont_pac = 0
    for k in range(tipo):
        for s in entrega_final:
            if n+1 == s['sucursal'] and s['tipo'] == k+1:
                cont_pac = cont_pac + 1

    paciente_sucu.append({'sucursal': n+1, 'pacientes': cont_pac})

filtrada = []
filtrada_suc = []
filtrada2 = []
for n in range(sucursales):
    print(n+1)

    for s in sucursal_list:
        if s['id'] == n+1:
            filtrada_suc.append({'tipo': s['tipo'], 'existencias': s['existencias']})
            # print(s['tipo'], s['existencias'])
    min_suc = min(filtrada_suc, key= lambda x: x['existencias'])
    max_suc = max(filtrada_suc, key= lambda x: x['existencias'])
    print(min_suc['tipo'],min_suc['existencias'])   
    print(max_suc['tipo'],max_suc['existencias'])   
    for h in programadas_sucu:
        if h['sucursal'] == n+1:
            filtrada.append(h['cantidad'])
    for f in prom_entregadas:
        if f['sucursal'] == n+1:
            filtrada2.append(f['cantidad'])
    promedio = 0
    for l in filtrada:
        promedio = promedio + l     
    promedio2 = 0
    for j in filtrada2:
        promedio2 = promedio2 + j 

    for m in paciente_sucu:
        if m['sucursal'] == n+1:
            pac = m['pacientes']

    if promedio2 != 0 and pac != 0:   
        resul = promedio2/pac
    else: 
        resul = 0
    print("{0:.2f}".format(min(filtrada)), "{0:.2f}".format(promedio/tipo),"{0:.2f}".format(max(filtrada)))
    print("{0:.2f}".format(resul))
    filtrada = []
    filtrada2 = []
    filtrada_suc = []
min_max = []

# print(programadas_sucu)
for n in programadas_sucu:
    if int(n['tipo']) == 1:
        min_max.append({'sucursal': n['sucursal'], 'cantidad': n['cantidad']})
# min_max.sort(key=lambda x: x['cantidad'], reverse=False)


# res = min(entrega_final, key= lambda x: x['cantidad_med'])

res = min(min_max, key= lambda x: x['cantidad'])
res2 = max(min_max,  key= lambda x: x['cantidad'])
print(res['sucursal'], res['cantidad'])
print(res2['sucursal'], res2['cantidad'])
# print(programadas_sucu)
# print(min_max)
                
    
    
    
    



    