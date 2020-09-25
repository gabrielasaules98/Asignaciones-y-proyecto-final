#Universidad Central de Venezuela
#Facultad de Ingeniería
#Programación (0790)
#Profesor: Carlos E. González C. github: c27gc
#Estudiante: Gabriela Saules CI:26470714 github: gabrielasaules98

#Descripción: En este código se implementará una agenda telefónica básica, y
#tiene como fin único la enseñanza de Python, en particular la manipulación de
#archivos de texto.

#Para el nombramiento de las variables (objetos) se utilizará el estandar de nomenclatura
#recomendado en el PEP 8 de python. 
#más información en este link: https://www.python.org/dev/peps/pep-0008/


#Asignación: comente cada línea del código explicando que hace.

#Asignación: empaquete las funciones de este archivo en un módulo independiente.

def crear_contacto(agenda_path):
    """Esta función agrega un contacto a una agenda"""
    nombre = input("Ingrese el nombre del contacto: ")  # imprime mensaje solicitando el nombre del contacto a crear y  lee por consola el nombre del contacto a añadir
    telefono = input("Ingrese el telefono de {} :".format(nombre)) # imprime mensaje formateado con el nombre del contacto solicitando su teléfono para ser leído por consola
    direccion = input("Ingrese la dirección de {} :".format(nombre)) # imprime mensaje formateado con el nombre del contacto solicitando su dirección para ser leída por consola

    contacto = {'Nombre':nombre, 'Telefono': telefono, 'Direccion': direccion} #con la información provista por el usuario se crea un diccionario contacto
    agenda = descargar_agenda(agenda_path) #hace un llamado a función que retorna la agenda en la dirección pasada por parametro
    if len(agenda.keys()) == 0: #si se ha devuelto una agenda vacía se asigna el valor del primer id de contacto
        id_contact = '0-0001'
    else:
        last_contact = int(list(agenda.keys())[-1].split('-')[-1])+1
        """se obtiene la última llave y id de la agenda descargada
          se procede a usar la función split con el separador - y se accede al último índice de la lista resultante
          obteniendo el número de contacto, ejemplo de '0-0001' se obtiene el '0001', ese string se pasa a su representación entera
          y luego se aumenta en uno, en el ejemplo anterior last_contact quedaría en el entero 2"""
        last_contact = (4-len(str(last_contact)))*'0'+str(last_contact)
        """ se formatea el entero del último contacto a
        su representación string correspondiente
        esto se hace primero obteniendo la diferencia de 4 con la cantidad de digitos que tenga el número del id más reciente
        esa será la cantidad de de ceros que irán antes de la representación entera del id,  ejemplo:
        representación enterada último id : 2, dígitos de ese número: 1, 0 a agregar antes de el: 4-1 = 3
        finalmente se concatenan los dos strings para obtener '0002'"""
        id_contact = '0-{}'.format(last_contact)
         # se finaliza el formato concatenando un prefijo 0-ejemplo: de last_contact = '0002' se obtiene un id_contact = '0-0002'

    agenda.update( {id_contact:contacto} )
     """se llama a actualización de la agenda con un diccionario como parametro
    este dicionario tiene como unica llave el id_contact antes generado y como valor el diccionario contact con los valores 
    introducidos por consola, si un contacto con mismo id existe en dicha agenda actualiza la llave-valor de ese contacto,
    si no existe dicho contacto lo crea y añade al diccionario agenda como es nuestro caso"""

    cargar_agenda(agenda_path,agenda) #se llama al guardado del diccionario agenda actualizado en su respectiva dirección de archivo

def eliminar_contacto(agenda_path):
    """Esta función elimina un contacto de una agenda"""
    # Asinación : Hacer que los identificadores id se reacomoden cuando se elimine un contacto.
    Flag = True #se asigna un flag para eliminar contactos mientras el usuario lo desee
    while Flag: #inicia el ciclo de eliminación iterando
        nombre = input("Indique nombre (o parte del nombre) del contacto que desea eliminar de la agenda: ") #se obtiene el nombre parcial o total del usuario a eliminar
        agenda = descargar_agenda(agenda_path) #hace un llamado a función que retorna la agenda en la dirección pasada por parametro
        print("Identifique el id del usuario que desea eliminar.") #imprime mensaje para solicitar la identificación del usuario a eliminar
        for element_key,element in buscar(agenda, nombre.lower()):
            print('id: {}\t nombre: {}'.format(element_key, element))

        id = input("Ingrese el id del contacto a eliminar de la agenda: ")
        
        agenda.pop(id)
        
        cargar_agenda(agenda_path,agenda)

        continuar =  input("Desea eleminar otro contacto? ( opciones 's' o 'n'):")
        if continuar.lower() == 'n':
            Flag = False
        elif continuar.lower() != 's':
            raise ValueError("Error, las opciones válidas son 's' o 'n'.")

    
# Asignación: agregar una función para editar un contacto.


def cargar_agenda(agenda_path, agenda):
    """La función cargar_agenda crea el archivo de texto donde se
    almacenará una agenda dada y escribe o sustituye su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""

    with open(agenda_path+'.txt', 'wt') as file:
        count = 0
        for id, contenido in zip(agenda.keys(), agenda.values()):
            if count == 0:
                id_tag = 'id:{}'.format(id)
                count += 1
            else:
                id_tag = '\nid:{}'.format(id)

            file.writelines([id_tag,'\n\tContacto:{}'.format(contenido['Nombre']),\
            '\n\tTelefono:{}'.format(contenido['Telefono']),'\n\tDireccion:{}'.format(contenido['Direccion'])])



def descargar_agenda(agenda_path):
    """La función descargar_agenda busca el archivo de texto donde se
    encuentra almacenada una agenda dada y descarga su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""
    agenda = {}
    with open(agenda_path+'.txt', 'r') as file:
        content = file.read().split('\n')
        if content != ['']:
            for i in range(0,len(content),4):
                id = content[i].split(':')[1]
                nombre = content[i + 1].split(':')[1]
                telefono = content[i + 2].split(':')[1]
                direccion = content[i + 3].split(':')[1]
                contacto = {'Nombre': nombre, 'Telefono': telefono, 'Direccion': direccion}
                agenda.update( {id: contacto} )

    return agenda

def crear_si_no_existe(agenda_path):
    """La funcion crear_si_no_existe funcion crea de forma segura el archivo agenda.txt. La
    implementacion se realiza sin importar ningun modulo de python, además, se
    al final del subprograma en comentarios se adjunto una implementacion
    importando el modulo os."""

    try:
        with open('agenda.txt', 'r') as file:
            pass
    except FileNotFoundError:
        with open('agenda.txt', 'w'):
            pass
    # import os.path
    # file_exists = os.path.isfile(agenda_path)
    # if file_exists:
    #   pass
    # else:
    #   with open('agenda.txt', 'w'):
    #       pass


def buscar(agenda, nombre):
    lista_id = []
    lista_nombre = []
    for id in agenda.keys():
        if nombre.lower() in agenda[id]['Nombre'].lower():
            lista_id.append(id)
            lista_nombre.append(agenda[id]['Nombre'])

    return zip(lista_id, lista_nombre)

def main():
    """La función main es la instancia principal del programa, utiliza el tipo
    de dato dict para representar la agenda telefónica, así como para
    representar los contactos. Ejemplo:

        contacto1 = {'Nombre':'Carlos C. González E.', 'Telefono': '+58 0412 223
        1222', 'Direccion': 'Colinas de Bellomonte.'}

        contacto2 = {'Nombre':'Pedro P. McFly D.', 'Telefono': '+58 0413 333
        1442', 'Direccion': 'El Recreo.'}

        agenda = {'0-0001': contacto1, '0-0002': contacto2}"""
    # Asignación: agregar una opcion para mostrar un resumen del calendario en la consola,
    # este resumen debe estar formateado para facilitar su lectura.
    crear_si_no_existe('agenda.txt')
    
    while(True):
        accion = input("Quiere crear, eliminar un contacto o salir del programa? (Escriba 'crear' o 'eliminar', 'salir'): ")

        if accion.lower() == 'crear':
            crear_contacto('agenda')
        elif accion.lower() == 'eliminar':
            eliminar_contacto('agenda')
        elif accion.lower() == 'salir':
            break
        else:
            raise ValueError("Error, opción no válida. Las opciones válidas son crear y editar.")

    print("Fin del programa, gracias por utilizar la agenda")

if __name__ == '__main__':
    main()
