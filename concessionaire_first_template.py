import json
import os

class Concesionario:
    #i think the file_path should be in main, to keep the class clear and every method of the class be aout in main
    dir = r""
    file_name = "concesionarios.json"
    file_path = os.path.join(dir, file_name)

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.automoviles = []

    @staticmethod
    def crearConcesionario(): #Create a new concessionaire
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")

        if os.path.exists(Concesionario.file_path):
            with open(Concesionario.file_path, 'r') as file:
                existing_data = json.load(file)
                for data in existing_data:
                    if nombre == data.get('nombre'):
                        raise Exception("El concesionario ya existe. Por favor, introduce uno que no exista.")
                data = Concesionario(nombre, direccion)
                existing_data.append(data.__dict__)
        else:
            existing_data = [{"nombre": nombre, "direccion": direccion, "automoviles": []}]

        with open(Concesionario.file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)

    @staticmethod
    def añadir_modelo_a_concesionario(): #Add car to a concessionaire
        marca = input("Introduce la marca del vehiculo: ")
        modelo = input("Introduce el modelo del vehiculo: ")
        year = input("Introduce el año del vehiculo: ")
        precio = input("Introduce el precio del vehiculo: ")
        nombre_del_concesionario = input("Introduce el nombre del concesionario: ")

        with open(Concesionario.file_path, 'r') as file:
            data = json.load(file)
            for existing_data in data:
                if nombre_del_concesionario == existing_data['nombre']:
                    existing_data["automoviles"].append(Automovil(marca, modelo, year, precio))

        with open(Concesionario.file_path, 'w') as file:
            json.dump(data, file, indent=4, cls=AutomovilEncoder)

    @staticmethod
    def mostrar_automoviles_en_venta(): #See al the cars in an concessionaire
        concesionario = input("Introduce el nombre del concesionario: ")
        with open(Concesionario.file_path, 'r') as file:
            data = json.load(file)
            for concesionario_data in data:
                if concesionario_data["nombre"] == concesionario:
                    automoviles = concesionario_data["automoviles"]
                    for car in automoviles:
                        print("##################")
                        print(f"Marca: {car['marca']}")
                        print(f"Modelo: {car['modelo']}")
                        print(f"Año: {car['year']}")
                        print(f"Precio: {car['precio']}")
                        print("##################\n")
                    break
            else:
                print(f"No se encontró el concesionario '{concesionario}'")

    @staticmethod
    def buscar_automovil(): #Search for a car in an named concessionaire, using brand and model
        concesionario = input("Introduce el nombre del concesionario: ")
        marca = input("Introduce la marca del automóvil: ")
        modelo = input("Introduce el modelo del automóvil: ")

        with open(Concesionario.file_path, 'r') as file:
            data = json.load(file)
            for concesionario_data in data:
                if concesionario == concesionario_data['nombre']:
                    automoviles = concesionario_data['automoviles']
                    for automovil in automoviles:
                        if automovil['marca'] == marca and automovil['modelo'] == modelo:
                            print("Automóvil encontrado:")
                            print(f"Marca: {automovil['marca']}")
                            print(f"Modelo: {automovil['modelo']}")
                            print(f"Año: {automovil['year']}")
                            print(f"Precio: {automovil['precio']}")
                            return

        print("El automóvil no se encontró en el concesionario especificado.")


    @staticmethod
    def vender_automovil():#Sell car of the concessionaire
        concesionario = input("Introduce el nombre del concesionario: ")
        with open(Concesionario.file_path, 'r+') as file:
            data = json.load(file)
            for concesionario_data in data:
                if concesionario == concesionario_data['nombre']:
                    automoviles = concesionario_data['automoviles']
                    for id, automovil in enumerate(automoviles):
                        print(f"{id + 1}. {automovil['marca']} {automovil['modelo']}")

                    automovil_index = int(input("Seleccione el número del automóvil a vender: "))
                    try:
                        sold_automovil = automoviles.pop(automovil_index - 1)
                        print(f"Se ha vendido el automóvil: {sold_automovil['marca']} {sold_automovil['modelo']}")
                    except ValueError:
                        print("Selección inválida. Introduzca un número válido.")

                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    return

        print("El concesionario no existe.")
        
   #¿This should be in Automovil.py module?     
class Automovil:
    def __init__(self, marca, modelo, year, precio):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.precio = precio

class AutomovilEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Automovil):
            return o.__dict__
        return super().default(o)

#¿This should be main.py?
while True:
    print("#### MENU #####")
    print("1. Crear concesionario.")
    print("2. Añadir automovil.")
    print("3. Buscar automovil")
    print("4. Vender automovil.")
    print("5. Mostrar automoviles disponibles.")
    print("6. Salir")
    opc = int(input("Seleccione opción: "))
    if opc not in range(1, 7):
        raise Exception("Opcion no valida")

    match opc:
        case 1:
            Concesionario.crearConcesionario()
        case 2:
            Concesionario.añadir_modelo_a_concesionario()
        case 3:
            Concesionario.buscar_automovil()
        case 4:
            Concesionario.vender_automovil()
        case 5:
            Concesionario.mostrar_automoviles_en_venta()
        case 6:
            break




