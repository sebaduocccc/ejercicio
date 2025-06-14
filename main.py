#### Clinica Proyecto

pacientes = {}
farmacos = {}
insumos_clinicos = {}
productos_terminados = {}
prestaciones_medicas = {}
proveedores = {}

def mantencion_maestros(categoria,accion):
    print(f"categoria: {categoria}, accion: {accion}")
    diccionario_seleccionado = None
    if categoria == "Pacientes":
        diccionario_seleccionado = pacientes
    elif categoria == "Farmacos":
        diccionario_seleccionado = farmacos
    elif categoria == "Insumos Clinicos":
        diccionario_seleccionado = insumos_clinicos
    elif categoria == "Productos terminados":
        diccionario_seleccionado = productos_terminados
    elif categoria == "Prestaciones medicas":
        diccionario_seleccionado = prestaciones_medicas
    elif categoria == "Proveedores":
        diccionario_seleccionado = proveedores
    else:
        print("Categoria no especificada.")

    match accion:

        case "crear":
            nombre_cat_crear = input(f"Ingresa un nombre de indice para agregar a {categoria}: ")
            if not nombre_cat_crear or nombre_cat_crear == "":
                print("Ingresa un nombre válido para agregar!")
                input()
            elif nombre_cat_crear in diccionario_seleccionado:
                print(f"Este item ya esta en {categoria}, Intentalo nuevamente!")
                input()
            else:
                codigo_cat_crear = input(f"Ingresa el codigo para identificar a {nombre_cat_crear} en {categoria}: ")
                if not codigo_cat_crear or codigo_cat_crear == "":
                    print("Ingresa un codigo válido para agregar!! Vuelve a intentarlo nuevamente.")
                    input()
                else:
                    descripcion_cat_crear = input(f"Ingresa una descripción para {nombre_cat_crear}: ")
                    if not descripcion_cat_crear or descripcion_cat_crear == "":
                        print("Escribe una descripción valida!! Vuelve a intentarlo.")
                        input()
                    
                    else:
                        diccionario_seleccionado[nombre_cat_crear] = {"bloqueado":False,"Codigo":codigo_cat_crear,"Descripción":descripcion_cat_crear,"Existencias":0}
                        print(diccionario_seleccionado)
                        input()




        case "modificar":
            if not diccionario_seleccionado:
                print(f"No hay items en {categoria}, Intenta agregar items para empezar!")
            else:
                ### Imprimir todos los items de la categoria
                print(f"---{categoria}---")
                for indice,detalles in diccionario_seleccionado.items():
                    codigo = detalles.get("Codigo",None)
                    descripcion = detalles.get("Descripción",None)
                    estado = detalles.get("bloqueado",None)
                    existencias = detalles.get("Existencias",None)
                    if estado == False:
                        estado = "Desbloqueado"
                    else:
                        estado = "Bloqueado"
                    print(f"{indice}: Estado:{estado}, Codigo:{codigo},  Descripción:{descripcion} , Stock:{existencias}")
                
                modificar_item = input(f"Ingresa el nombre del item a modificar en {categoria}: ")
                if modificar_item in diccionario_seleccionado:
                    print(f"¿Que quieres modificar de {modificar_item}?")
                    print("1.Codigo\n" \
                    "2.Descripción\n" \
                    "3.Stock")
                    modificar_opcion = input("Ingresa una opción: ")
                    
                else:
                    print("No existe ese item")
                    input()

        case "bloquear":
            print("bloqueando")



####Empieza el programa
programa = True

while programa:
    print("SISTEMA DE CLINICA")
    print("¿Que desea hacer?\n" \
    "1.Mantención de maestros\n" \
    "2.Inventario\n" \
    "3.Producción\n" \
    "4.Ventas")
    opcion = input("Ingresa tu opción: ")

    match opcion:
        case "1":
            mantencion_menu = True
            opciones_de_mantencion = {
                "a":"Pacientes",
                "b":"Farmacos",
                "c":"Insumos Clinicos",
                "d":"Productos terminados",
                "e":"Prestaciones medicas",
                "f":"Proveedores"
            }
            while mantencion_menu:
                print("Mantención de maestros")
                print("Selecciona una categoria:\n" \
                "a. Pacientes\n" \
                "b. Fármacos\n" \
                "c. Insumos clínicos.\n" \
                "d. Productos terminados.\n" \
                "e. Prestaciones médicas.\n" \
                "f. Proveedores.\n")
                opcion_mantencion = input("Ingresa una opción ('salir' para volver al menu principal): ")
                if opcion_mantencion.lower() == "salir":
                    mantencion_menu = False
                elif opcion_mantencion in opciones_de_mantencion:
                    categoria_seleccionada = opciones_de_mantencion[opcion_mantencion]
                    print(f"Seleccionaste {categoria_seleccionada}")
                    input()
                    opcion_accion_menu = True

                    while opcion_accion_menu:
                        print(f"¿Que quieres hacer con la categoria {categoria_seleccionada}?")
                        print("1.Crear items\n" \
                        "2.Modificar items\n" \
                        "3.Bloquear items\n" \
                        "'salir' para volver al menu principal")

                        opcion_accion = input("Ingresa tu opción: ")

                        if opcion_accion.lower() == "salir":
                            opcion_accion_menu = False
                            mantencion_menu = False
                        elif opcion_accion == "1":
                            accion = "crear"
                            mantencion_maestros(categoria_seleccionada,accion)
                        elif opcion_accion == "2":
                            accion = "modificar"
                            mantencion_maestros(categoria_seleccionada,accion)
                        elif opcion_accion == "3":
                            accion = "bloquear"
                            mantencion_maestros(categoria_seleccionada,accion)

                        else:
                            print("Ingresa una opción valida!")
                            input()

                else:
                    print("Ingresa una opción valida.")
                    input()

        case "2":
            print("caso 2")
        
        case "3":
            print("caso 3")
        
        case "4":
            print("caso 4")

        case ___:
            print("Selecciona una opción valida")