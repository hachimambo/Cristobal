from os import system
system("cls")

pelis = []
peliculas = {
'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

pelis.append(peliculas)

print(peliculas['P101'])

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

def validar_espacios_ni_vacio(mensaje):
    while(True):
        texto = input(f"Ingrese {mensaje}: ")
        if texto == "" or " " in texto:
            print("El texto ingresado no debe contener espacios en blanco ni estar vacío")
        else:
            return(texto)

def validar_numero_entero(texto):
    while(True):
        try:
            numero = int(input(f"Ingrese {texto}: "))
            if numero < 0:
                print("El numero ingresado debe ser mayor a cero")
            else:
                return(numero)
        except:
            print("Solo se permite el ingreso de numeros")    

def clasificacion():
    while(True):
        letra = input("Ingrese la clasificacion de la audiencia |A|B|C: ").upper()
        if letra == "A" or letra == "B" or letra == "C":
            return(letra)
        else:
            print("Solo puede ingresar la clasificacion A, B o C")

def es_3d():
    while(True):
        print("Responda (s) si es verdadero")
        print("Responda (n) si es falso")
        opcion = input("El formato de la funcion es 3D? ").lower()
        if opcion == "s":
            return(True)
        elif opcion == "n":
            return(False)
        else:
            print("Solo puede responder (s) o (n)")
def menu_principal():
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
def leer_opcion():
    while(True):
        validacion = validar_numero_entero("una opcion")
        if validacion in range(1,7):
            return (validacion)
        else:
            print("Debe seleccionar una opción válida")

def cupos_genero():
            genero_pelicula = input(f"Ingrese el genero de la pelicula: ").lower()
            for genero in pelis:
                print(genero["genero"])
#cupos_genero()