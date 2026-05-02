import random
import numpy as np
import time
import sys
import matplotlib.pyplot as plt
import auto_usado


# Leer archivo japoneses
with open("autos_japoneses.csv", 'r', encoding='utf-8') as f:
    jdm_lista = [line.strip() for line in f if line.strip()]

# Leer archivo yankees
with open("autos_yankees.csv", 'r', encoding='utf-8') as f:
    yankees_lista = [line.strip() for line in f if line.strip()]

# Leer archivo italianos
with open("autos_italianos.csv", 'r', encoding='utf-8') as f:
    italia_lista = [line.strip() for line in f if line.strip()]
    
# Leer archivo alemanes
with open("autos_alemanes.csv", 'r', encoding='utf-8') as f:
    alemania_lista = [line.strip() for line in f if line.strip()]

# Saludo inicial
print('Somos Prestige Motor Sports, nos dedicamos a importar autos desde Estados Unidos, Alemania, Italia y Japón')
nombre = input('¿Cómo te llamas?  ')


frases_garage = [
    'quiero armar mi garage', 'armar mi garage', 'quiero formar mi garage',
    'quiero construir mi garage', 'armar'
]
frases_proyecto = ['buscar', 'buscar un proyecto', 'buscar mi proyecto', 'proyecto']
paises = ['Estados Unidos', 'Alemania', 'Italia', 'Japón']


while True:
    difurcacion = input('\n¿Querés armar tu garage o querés buscar algún proyecto? (escribí "salir" para terminar)  ').lower()
    sys.stdout.write("\nTanner está trabajando" + "."*3 )
    sys.stdout.flush()
    time.sleep(1)
    if difurcacion in frases_proyecto:
        auto_usado.buscar_proyecto()
        continue
        
    
    if difurcacion == 'salir':
        sys.stdout.write("\nTanner está trabajando" + "."*3 )
        sys.stdout.flush()
        time.sleep(1)
        print('¡Gracias por visitar Prestige Motor Sports! Hasta pronto.')
        break

    if difurcacion in frases_garage:
        print(f'\nHola {nombre.capitalize()}, soy Tanner y te voy a armar un garaje con autos de los países antes mencionados.')

        arranque = input(f'\n¿Estás listo {nombre.capitalize()}? (si/no)  ').lower()
        
        #Si arranque es 'no'
        if arranque == 'no':
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            print('\nOk, volvamos a empezar.\n')
            continue
        
        #Si el usuario escribe cualquier cosa
        if arranque != 'si':
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            print('\nRespuesta no reconocida, volvamos a empezar.\n')
            continue

        # Si arranque es 'si'
        if arranque == 'si':
            print('\n')
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            dado = int(input('\n¿Cuántos autos querés que tenga tu garage?:  '))
        else:
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            print('\nEso no es un número válido. Volvamos a empezar.\n')
            continue

        autos_yankes = yankees_lista
        autos_japoneses = jdm_lista
        autos_italianos = italia_lista
        autos_alemanes = alemania_lista

        mis_paises = []
        garage = []
        
        sys.stdout.write("\nTanner está trabajando" + "."*3 )
        sys.stdout.flush()
        time.sleep(1)
        print(f'\nVamos a tirar un dado {dado} veces para definir la nacionalidad de tus {dado} autos...')

        for i in range(dado):
            eleccion = random.choice(paises)
            mis_paises.append(eleccion)
        print(f'\nLos países de origen de tus {dado} autos son: {", ".join(mis_paises)}')
        sys.stdout.write("\nTanner está trabajando" + "."*3 )
        sys.stdout.flush()
        time.sleep(1)
        print('\nAhora tiremos el dado para llenar tu garage!!')

        if 'Estados Unidos' in mis_paises:
            for _ in range(mis_paises.count('Estados Unidos')):
                yan = random.choice(autos_yankes)
                garage.append(yan)
        else:
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            print('\nNo salió ningún auto de Estados Unidos')

        if 'Italia' in mis_paises:
            for _ in range(mis_paises.count('Italia')):
                ita = random.choice(autos_italianos)
                garage.append(ita)
        else:
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            print('\nNo salió ningún auto de Italia')
        
        if 'Alemania' in mis_paises:
            for _ in range(mis_paises.count('Alemania')):
                ale = random.choice(autos_alemanes)
                garage.append(ale)
        else:
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            print('\nNo salió ningún auto de Alemania')
        
        if 'Japón' in mis_paises:
            for _ in range(mis_paises.count('Japón')):                            
                jap = random.choice(autos_japoneses)
                garage.append(jap)
        else:
            sys.stdout.write("\nTanner está trabajando" + "."*3 )
            sys.stdout.flush()
            time.sleep(1)
            print('\nNo salió ningún auto de Japón')
            
        sys.stdout.write("\nTanner está trabajando" + "."*3 )
        sys.stdout.flush()    
        time.sleep(1)
        print("\nTu garage quedó armado con estos autos:")
        for auto in garage:
            print("-", auto)
        
        sys.stdout.write("\nTanner está trabajando" + "."*3 )
        sys.stdout.flush()
        time.sleep(1)
        print("\n¡Garage armado! Si querés armar otro, elegí de nuevo.\n")
        
        #Importo el grafico
        # Contar cuántos autos hay de cada país
        nacionalidad_yankee = mis_paises.count('Estados Unidos')
        nacionalidad_japonesa = mis_paises.count('Japón')
        nacionalidad_italiana = mis_paises.count('Italia')
        nacionalidad_alemana = mis_paises.count('Alemania')

        # Etiquetas y valores para el gráfico
        etiquetas = ['Alemania', 'Japón', 'Estados Unidos', 'Italia']
        valores = [nacionalidad_alemana, nacionalidad_japonesa, nacionalidad_yankee, nacionalidad_italiana]

        # Gráfico de barras
        plt.bar(etiquetas, valores, color='blue')
        plt.title('Cantidad de autos por país en mi garaje')
        plt.ylabel('Cantidad de autos')
        plt.grid(axis='y')
        plt.show(block=True)


    else:
        print('\nOpción no reconocida. Probá escribir algo como "armar mi garage" o escribí "salir" para terminar.\n')

