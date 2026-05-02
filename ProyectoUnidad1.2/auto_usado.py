#Proyecto
import webbrowser

def buscar_proyecto():
    while True:
        eleccion = input('\n¿De qué país quieres buscar tu futuro proyecto? Estados Unidos, Alemania, Italia o Japón: ').strip().lower()

        if eleccion == 'estados unidos':
            url = 'https://www.ebay.com/sch/i.html?_nkw=cars+trucks'
            break
        elif eleccion == 'alemania':
            url = 'https://www.ooyyo.com/germany/used-cars-for-sale/'
            break
        elif eleccion == 'italia':
            url = 'https://www.ooyyo.com/italy/used-cars-for-sale/'
            break
        elif eleccion == 'japon' or eleccion == 'japón':
            url = 'https://carused.jp/'
            break
        else:
            print('Opción inválida, por favor elegí una de las 4 opciones mencionadas.')

    print(f"\nAbriendo la página web de {eleccion.title()}...")
    webbrowser.open(url)
