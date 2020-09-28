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
       
    """buscar es llamada con la agenda a buscar y el nombre o parte del mismo en minúsculas, 
          devuelve una lista en la que sus elementos son pares de id - nombre del contacto, se itera sobre esta lista siendo element_key el 
          id del contacto y element el nombre completo del mismo """
        
        for element_key,element in buscar(agenda, nombre.lower()):
            print('id: {}\t nombre: {}'.format(element_key, element)) #se imprime de manera formateada ambos valores antes mencionados

        id = input("Ingrese el id del contacto a eliminar de la agenda: ") #se obtiene el id del contacto a eliminar
         #se elimina del diccionario agenda el contacto con el id obtenido
        ids = list(agenda.keys()) #se obtienen los ids 
        ids.sort() #se ejecuta sort con intenciones de iterar en orden y uno a uno cada elemento, 0-0001 < 0-0002 
        if id == ids[-1]:
             agenda.pop(id) #si el id es el ultimo no hay necesidad de reacomodar la agenda
        else:
            for id_contacto in ids:
                if id_contacto >=  id and id_contacto != ids[-1]: #si el id de contacto está entre el id a eliminar y el penúltimo de los ids se hace lo siguiente
                    id_siguiente = int(id_contacto.split('-')[-1])+1  #se obtiene el numero del siguiente id
                    id_siguiente = '0-'+(4-len(str(id_siguiente)))*'0'+str(id_siguiente) #se pasa a su versión en string
                    agenda[id_contacto] = agenda[id_siguiente]# se asigna el valor del siguiente contacto con el siguiente id, esto entra desde el contacto a eliminar haciendo que sea el único en perder la información
            agenda.pop(ids[-1]) #se elimina el último elemento de la agenda ya que su información está ahora en el penúltimo elemento del diccionario

        
        cargar_agenda(agenda_path,agenda) #se llama al guardado del diccionario agenda actualizado en su respectiva dirección de archivo

        continuar =  input("Desea eleminar otro contacto? ( opciones 's' o 'n'):") #se pregunta y obtiene la respuesta a si se desea eliminar otro contacto
        if continuar.lower() == 'n': #de ser n la respuesta Flag pasa a ser falso y el ciclo termina
            Flag = False
        elif continuar.lower() != 's': #de ser una respuesta no contemplada el programa termina con error
            raise ValueError("Error, las opciones válidas son 's' o 'n'.")
            #de haber sido 's' la respuesta un nuevo ciclo de eliminado se ejecuta
    
    
def actualizar_contacto(agenda_path):
    """Esta función actualizar un contacto de una agenda"""
    # Asignación : Hacer que los identificadores id se reacomoden cuando se actualice un contacto.
    Flag = True #se asigna un flag para actualizar contactos mientras el usuario lo desee
    while Flag: #inicia el ciclo de actualización, una posible actualización por iteración
        nombre = input("Indique nombre (o parte del nombre) del contacto que desea actualizar de la agenda: ") #se obtiene por consola el nombre parcial o total del usuario a actualizar
        agenda = descargar_agenda(agenda_path) #hace un llamado a función que retorna la agenda en la dirección pasada por parametro
        print("Identifique el id del usuario que desea actualizar.") #imprime mensaje para solicitar la identificación del usuario a actualizar
        
        """buscar es llamada con la agenda a buscar y el nombre o parte del mismo en minúsculas, 
          devuelve una lista en la que sus elementos son pares de id - nombre del contacto, se itera sobre esta lista siendo element_key el 
          id del contacto y element el nombre completo del mismo """
        for element_key,element in buscar(agenda, nombre.lower()): 
            print('id: {}\t nombre: {}'.format(element_key, element)) #se imprime de manera formateada e indicativa ambos valores antes mencionados

        id = input("Ingrese el id del contacto a actualizar de la agenda: ") #se obtiene el id del contacto a actualizar
        deseo_actualizar =  input("desea actualizar el nombre del contacto seleccionado? presione 's' para sí, y cualquier otra tecla para no: ")
        if deseo_actualizar.lower() == 's':
            agenda[id]['Nombre'] = input("introduzca el nuevo nombre para su contacto: ")
        deseo_actualizar =  input("desea actualizar el numero del contacto seleccionado? presione 's' para sí, y cualquier otra tecla para no: ")
        if deseo_actualizar.lower() == 's':
            agenda[id]['Telefono'] = input("introduzca el nuevo telefono para su contacto: ")
        deseo_actualizar =  input("desea actualizar la direccion del contacto seleccionado? presione 's' para sí, y cualquier otra tecla para no: ")
        if deseo_actualizar.lower() == 's':
            agenda[id]['Direccion'] = input("introduzca la nueva direccion para su contacto: ")            
        
        cargar_agenda(agenda_path,agenda)  #se llama al guardado del diccionario agenda actualizado en su respectiva dirección de archivo

        continuar =  input("Desea actualizar otro contacto? ( opciones 's' o 'n'):") #se pregunta y obtiene la respuesta a si se desea actualizar otro contacto
        if continuar.lower() == 'n': #de ser n la respuesta Flag pasa a ser falso y el ciclo termina
            Flag = False
        elif continuar.lower() != 's':#de ser una respuesta no contemplada el programa termina con error
            raise ValueError("Error, las opciones válidas son 's' o 'n'.")
        #de haber sido 's' la respuesta un nuevo ciclo de actualizado se ejecuta


def mostrar_agenda(agenda_path):
    agenda = descargar_agenda(agenda_path) #obtenemos la agenda de la dirección solicitada
    for id, contacto in zip(agenda.keys(), agenda.values()): #iteramos sobre cada usuario
        print('id: {}\t nombre: {}\t numero: {}\t dirección: {}'.format(id, contacto['Nombre'], contacto['Telefono'], contacto['Direccion'] )) #se imprime formato visualizable de contacto
# Asignación: agregar una función para editar un contacto.



def cargar_agenda(agenda_path, agenda):
    """La función cargar_agenda crea el archivo de texto donde se
    almacenará una agenda dada y escribe o sustituye su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""
    
    """se crea en la ruta agenda_path.txt, en modo escritura
    se usa la gestión de archivo with as file para el correcto cerrado del mismo en cualquier circunstancia"""

    with open(agenda_path+'.txt', 'wt') as file:
        count = 0 #se incializa un contador a 0
        for id, contenido in zip(agenda.keys(), agenda.values()): #se itera sobre cada par llave-valor (id-diccioniario de contacto) del diccionario agenda
            if count == 0:  #si es la primera iteración
                id_tag = 'id:{}'.format(id) #se formatea un string a 'id:*valor del id del primer contacto en el diccionario*
                count += 1 #se aumenta el contador en 1
            else:  #si no es la primera iteración
                id_tag = '\nid:{}'.format(id) #se formatea como en el primer caso pero añadiendo un salto de línea

            file.writelines([id_tag,'\n\tContacto:{}'.format(contenido['Nombre']),\
            '\n\tTelefono:{}'.format(contenido['Telefono']),'\n\tDireccion:{}'.format(contenido['Direccion'])])
 
""" escribe los elementos de la lista al archivo primero el id_tag formateado según la iteración
  luego una nueva linea en ella una tabulación y formateado el string Contacto:*Nombre completo del contacto*
  luego una nueva linea en ella una tabulación y formateado el string Telefono:*Telefono del contacto*
  luego una nueva linea en ella una tabulación y formateado el string Dirección:*Direccion del contacto*
  """
  #finalmente al salir del ciclo por error o por finalización de los pares de la agenda se cierra el archivo en la ruta definida


def descargar_agenda(agenda_path):
    """La función descargar_agenda busca el archivo de texto donde se
    encuentra almacenada una agenda dada y descarga su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""
    agenda = {} #se asigna a agenda un diccionario vacío
    """se abre o se crea en la ruta 'agenda_path'.txt, se abre en modo lectura
    se usa la gestión de archivo with as file para el correcto cerrado del mismo en cualquier circunstancia"""
    with open(agenda_path+'.txt', 'r') as file:
        content = file.read().split('\n') #el contenido se lee y se convierte a una lista donde cada elemento es una linea del archivo esto gracias al usar  split con el separador de nueva linea
        if content != ['']:  #si el contenido no está vacío
            #se itera sobre un rango de 0 a numero de lineas del archivo, cada iteración de 4 en 4 debido a que la info de cada contacto se guarda en 4 lineas
            for i in range(0,len(content),4): #indice y lo que retorna,para el primer contacto 0-id, 1-nombre, 2-telefono, 3-direccion, para el segundo contacto 4-id, 5-nombre, 6-telefono, 7-direccion, y así tantos contactos hayan
                #la instrucción .split(':')[1]  en las siguientes linea sirve para obtener el valor de la linea formateada de 'id:0-0001' se obtiene el 0-0001 por ejemplo:
                 
                id = content[i].split(':')[1] #se obtiene el id del contacto
                nombre = content[i + 1].split(':')[1] #se obtiene el nombre del contacto
                telefono = content[i + 2].split(':')[1]#se obtiene el telefono del contacto
                direccion = content[i + 3].split(':')[1]#se obtiene la direccion del contacto
                contacto = {'Nombre': nombre, 'Telefono': telefono, 'Direccion': direccion} #se crea el diccionario contacto con los valores leídos
                agenda.update( {id: contacto} ) #actualización o creacion de la llave-valor id-diccionario contacto en el diccionario agenda

    return agenda #retorno de la agenda leída del archivo de nombre pasado por parametro

def crear_si_no_existe(agenda_path):
    """La funcion crear_si_no_existe funcion crea de forma segura el archivo agenda.txt. La
    implementacion se realiza sin importar ningun modulo de python, además, se
    al final del subprograma en comentarios se adjunto una implementacion
    importando el modulo os."""

    try: #inicio de bloque try
        with open('agenda.txt', 'r') as file: #intento de lectura del archivo, puede emitir error
            pass   #se continúa, lectura correcta del archivo
    except FileNotFoundError: #si no existe el archivo el bloque except obtendra un error FileNotFoundError
        with open('agenda.txt', 'w'): #se abre el archivo a en modo de escritura si no existe lo crea
            pass
    # import os.path
    # file_exists = os.path.isfile(agenda_path)
    # if file_exists:
    #   pass
    # else:
    #   with open('agenda.txt', 'w'):
    #       pass


def buscar(agenda, nombre):
    lista_id = [] #se asigna a lista_id una lista vacía
    lista_nombre = []  #se asigna a lista_nombre una lista vacía
    for id in agenda.keys(): #se itera sobre las llaves/id del diccionario agenda
        if nombre.lower() in agenda[id]['Nombre'].lower():  #se verifica si el nombre completo  y en minisculas del contacto con id igual al id iterado contiene el nombre en minusculas pasado por parametro
            lista_id.append(id) #se añade el id del contacto iterado a la listas de ids
            lista_nombre.append(agenda[id]['Nombre'])#se añade el nombre completo del contacto iterado a la lista de nombres

    return zip(lista_id, lista_nombre) #las listas de igual tamaño y ordenadas se comprimen para tener una lista de tuples conformados por pares (id, nombre completo)

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
