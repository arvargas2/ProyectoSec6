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
