canciones_list = []  # BD


# --------- validaciones -----------------------------
# para el titulo y artista
def validar_texto_vacio(texto):
    if len(texto.strip() > 0):
        return True
    else:
        print("Error no puede ser vacio")
        return False


def validar_duracion(duracion):
    if duracion > 0:
        return True
    else:
        print("Error debe se mayor a cero!!!")
        return False


def imprimir_cancion(cancion):
    es_favorita = "Si" if cancion["favorita"] == True else "No"
    print(f"""
        -----------------------
        Titulo: {cancion["titulo"]}  
        Artista: {cancion["artista"]}
        Duración: {cancion["duracion"]} seg
        Favorita: {es_favorita}  """)


# --------- transacciones -----------------------------
def agregar_cancion():
    titulo = str(input("Ingrese titulo:")).strip()
    while not validar_texto_vacio(titulo):
        titulo = str(input("Ingrese titulo:")).strip()

    artista = str(input("Ingrese artista: ")).strip()
    while not validar_texto_vacio(artista):
        artista = str(input("Ingrese artista: ")).strip()

    while True:
        try:
            duracion = int(input("Ingrese duracion:"))
            while not validar_duracion(duracion):
                duracion = int(input("Ingrese duracion:"))
            break
        except:
            print("Error debe ser un N°")

    # ---- armamos json cancion -------------------
    cancion = {
        "titulo": titulo,
        "artista": artista,
        "duracion": duracion,
        "favorita": False,
    }
    # ------ cargamos el json a la lista -----------------
    canciones_list.append(cancion)
    print(" <<< Registro almacenado >>>")


# -----------------------------------------------
# es en realidad un listar!!!!!
def mostrar_canciones():
    if len(canciones_list) == 0:
        print("NO hay datos en la BD")
    else:
        for cancion in canciones_list:
            imprimir_cancion(cancion)


# ---------------------------------------------------
def buscar_cancion():
    titulo = str(input("Ingrese titulo:")).strip()
    while not validar_texto_vacio(titulo):
        titulo = str(input("Ingrese titulo:")).strip()

    encontrado = False
    for cancion in canciones_list:
        if cancion["titulo"] == titulo:
            encontrado = True
            imprimir_cancion(cancion)
    if encontrado == False:
        print("NO hay canciones con dicho titulo")
        
        
#-- data test ------------------------------
def cargar_data_test():
    cancion_1 = {
        "titulo": "Shape of You",
        "artista": "Ed Sheeran",
        "duracion": 233,
        "favorita": False,        
    }        
    cancion_2 = {
        "titulo": "Perfect",
        "artista": "Ed Sheeran",
        "duracion": 251,
        "favorita": True,        
    }
    cancion_3 = {
        "titulo": "Billie Jean",
        "artista": "Michael Jackson",
        "duracion": 202,
        "favorita": False,        
    }
    
    canciones_list.append(cancion_1)
    canciones_list.append(cancion_2)
    canciones_list.append(cancion_3)
    print("\n\n <<< data test cagada >>>")
