import os
from pathlib import Path

ruta_base = Path(Path.cwd(), "Recetas")


def contarRecetas(ruta):
    """Retorna el número de archivos txt encontrados en la ruta dada"""
    contador = 0
    for _ in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def inicio():
    """Muestra el menú inicio y retorna la opción dada por el usuario"""
    opcion_menu = "x"
    while not opcion_menu.isnumeric() or int(opcion_menu) not in range(1, 7):
        os.system("clear")
        print("*" * 45)
        print("*" * 10, "Bienvenido al recetario", "*" * 10)
        print("*" * 45, "\n")

        print(f"Ruta de las recetas: {ruta_base}")
        print(f"Total de recetas: {contarRecetas(ruta_base)}\n")
        print("*" * 45, "\n")

        print("[1] -> Leer receta")
        print("[2] -> Crear receta nueva")
        print("[3] -> Crear categoría nueva")
        print("[4] -> Eliminar receta")
        print("[5] -> Eliminar categoría")
        print("[6] -> Salir...\n")
        opcion_menu = input("Elige una opción: ")
    
    return opcion_menu


def mostrarCategorias(ruta):
    """Muestra las categorias y retorna una lista con las rutas de todas las carpetas"""
    os.system("clear")
    print("*" * 15, "Categorías", "*" * 15)
    categorias = []
    contador = 1

    for path_carpeta in Path(ruta).iterdir():
        str_carpeta = str(path_carpeta.name)
        print(f"[{contador}] -> {str_carpeta}")
        categorias.append(path_carpeta)
        contador += 1
    
    return categorias


def elegirCategoria(categorias):
    opcion_categoria = "x"
    while not opcion_categoria.isnumeric() or int(opcion_categoria) not in range(1, len(categorias) + 1):
        opcion_categoria = input("Elige una categoria: ")
    
    return categorias[int(opcion_categoria) - 1]


def mostrarRecetas(ruta):
    os.system("clear")
    print("*" * 15, "Recetas", "*" * 15)
    recetas = []
    ruta_recetas = Path(ruta)
    contador = 1

    for receta in ruta_recetas.glob("**/*txt"):
        str_receta = str(receta.name)
        print(f"[{contador}] -> {str_receta}")
        recetas.append(receta)
        contador += 1

    return recetas


def elegirReceta(recetas):
    opcion_receta = "x"
    while not opcion_receta.isnumeric() or int(opcion_receta) not in range(1, len(recetas) + 1):
        opcion_receta = input("Elige una receta: ")

    return recetas[int(opcion_receta) - 1]


inicio()
menu = 0

if menu == 1:
    categorias = mostrarCategorias(ruta_base)
    categoria_seleccionada = elegirCategoria(categorias)
    recetas = mostrarRecetas(categoria_seleccionada)
    receta_seleccionada = elegirReceta(recetas)
    # mostrar receta
    # volver a inicio
    pass
elif menu == 2:
    categorias = mostrarCategorias(ruta_base)
    categoria_seleccionada = elegirCategoria(categorias)
    # crear receta
    # volver a inicio
    pass
elif menu == 3:
    categorias = mostrarCategorias(ruta_base)
    # volver a inicio
    pass
elif menu == 4:
    categorias = mostrarCategorias(ruta_base)
    categoria_seleccionada = elegirCategoria(categorias)
    recetas = mostrarRecetas(categoria_seleccionada)
    receta_seleccionada = elegirReceta(recetas)
    # eliminar receta
    # volver a inicio
    pass
elif menu == 5:
    categorias = mostrarCategorias(ruta_base)
    categoria_seleccionada = elegirCategoria(categorias)
    # volver a inicio
    pass
elif menu == 6:
    # Finalizar programa
    pass
