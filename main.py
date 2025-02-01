nombre = "Juan"
apellido = "Perez"

def cambiar_nombre_y_apellido(nuevo_nombre, nuevo_apellido):
    global nombre, apellido
    nombre = nuevo_nombre
    apellido = nuevo_apellido

    if True:
        nombre = "Arty"
        apellido = "Gomez"

    return nombre, apellido

if __name__ == "__main__":
    print(f"Hello {nombre} {apellido}")

    nombre2, apellido2 = cambiar_nombre_y_apellido("Arty", "Gomez")

    print(f"Hello {nombre2} {apellido2}")
