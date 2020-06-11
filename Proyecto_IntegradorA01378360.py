#Brenda Vega Méndez A01378360
#-----------------------------------------------------------------------------------------------------------
import random as r

class Usuario:
    '''Esta clase permite al usuario ingresar sus datos (nombre, destino y aerolinea) para comprar un
    boleto, también tiene una función para asignar asientos y para imprimir el pase de abordar.'''
    
    __asiento = 1
     
    def __init__(self, nombre, destino, aerolinea):
        '''Esta función, al igual que en las otras clases, podríamos decir que reparte los diferentes
        valores a los atributos del objeto.'''
        self.__nombre = nombre
        self.__destino = destino
        self.__aerolinea = aerolinea
        self.__vuelo = []
        self.__asiento = Usuario.__asiento
        Usuario.__asiento+= 1
        
    @property
    def vuelo(self):
        return self.__vuelo
        
    @property
    def asiento(self):
        '''Gracias a esta @property, podemos acceder a este atributo ya que es privado. Lo mismo
        pasa en las otras clases.'''
        return self.__asiento
        
    def escoger_vuelo(self, vuelos):
        '''Esta función permite al usuario ver si hay un vuelo disponible de acuerdo a su destino y
        aerolinea.'''
        if (self.__destino == vuelos.destino) and (self.__aerolinea == vuelos.aerolinea): 
            print('Este vuelo esta disponible: \n', vuelos)
            self.__vuelo = vuelos
        else:
            print('No hay vuelos disponibles.')
            
    def asientos(self):
        '''Aquí le damos un número de asiento al azar al usuario del 1 al 60.'''
        self.__asiento = r.randrange(0,61)
        return self.__asiento
    
    def imprimir_pase(self, aeropuerto, vuelo):
        '''Con este método podemos imprimir los datos del vuelo y del usuario con formato de un pase
        de abordar.'''
        print(f'Pase de Abordar | {self.__nombre}')
       
        print(f'Asiento: {self.asiento}           Puerta: {aeropuerto.puerta}           Terminal: {aeropuerto.term(self.vuelo)}')
            
    def __str__(self):
        '''Aquí se le da formato a los datos del usuario.'''
        return f'Nombre: {self.__nombre} - Destino: {self.__destino} - Aerolinea: {self.__aerolinea}'
        
class Vuelos:
    '''En esta clase creamos los diferentes vuelos que el usuario puede encontrar.'''
    
    num_vuelo = 1
    
    def __init__(self, destino, aerolinea, horario, avion):
        self.__destino = destino
        self.__aerolinea = aerolinea
        self.__horario = horario
        self.__num_vuelo = Vuelos.num_vuelo
        Vuelos.num_vuelo += 1
        self.avion = avion
       
    
    @property
    def destino(self):
        return self.__destino
    
    @property
    def aerolinea(self): 
        return self.__aerolinea
    
    @property
    def horario(self):
        return self.__horario
    
    
    def __str__(self):
        '''Este método le la formato al objeto (al vuelo) para cada vez que tenga que ser mostrado'''
        return f'Número de Vuelo: {self.__num_vuelo} * Origen: CDMX * Destino: {self.__destino} * Aerolinea: {self.__aerolinea} * Horario: {self.__horario}'
    
    def apartar_asiento(self, nCol, nFil):
        self.avion.apartar_asiento(nCol,nFil)
     
class Aeropuerto:
    '''La asignación de puertas y terminales se encuentra dentro de esta clase,recibe el dato
    de la puerta por medio de un randrange importado del modulo 'random'.'''


    def __init__(self, puerta):
        self.__puerta = puerta
        self.__terminal = 0
        self.__vuelos = {}
        
    @property
    def puerta(self):
        return self.__puerta
    
    @property
    def terminal(self):
        return self.__terminal
    
    @property
    def vuelos(self):
        return self.__vuelos
    
    def term(self, vuelo):
        '''Aquí determinamos si el vuelo saldrá de la terminal 1 o 2, dependiendo si el destino se
        encuentra en la lista de los detinos t1 (estados de la República, nacionales).'''
        t1 = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Chiapas', 'Campeche', 'Chihuahua', 'Coahuila', 'Colima', 'Durango', 'Guanajuato', \
              'Hidalgo', 'Jalisco', 'Michoacan', 'Morelos', 'Nayarit', 'Nuevo Leon', 'Oaxaca', 'Puebla', 'Queretaro', 'Quntana Roo', 'San Luis Potosi', 'Sinaloa', \
              'Sonora', 'Tabasco', 'Tamaulipas', 'Veracruz', 'Yucatán', 'Zacatecas']
        
        if vuelo.destino in t1:
            self.__terminal = 1
        else:
            self.__terminal = 2
        return self.__terminal
       
    
    def agregar_vuelo(self, vuelo):
        ''' Aquí se recibe un vuelo y se agrega a un diccionario para que se mantenga un registro
        de los vuelos en existencia.'''
        self.__vuelos[vuelo] = vuelo
    
    def consultar_vuelos(self):
        '''Este metodo permite al usuario ver en un formato agradable los vuelos para un determinado
        día.'''
        print(f'Vuelos programados para hoy:')
        for v in self.__vuelos:
            print(v)
            
class Avion:
    
    def __init__(self, idAvion, sala):
       self.idAvion= idAvion
       self.sala = sala
       asientosTemp = []
       self.asientos= []
       for i in range (20):
           for j in range (3):
               asientosTemp.append(Asiento())
           self.asientos.append(asientosTemp)
           asientosTemp = []
           
    def apartar_asiento(self, nCol, nFil):
           nCol -= 1
           nFil = nFil -1
           self.asientos[nCol][nFil].ocupar()
           #print(self.asientos[nCol][nFil].verificar())
           
    def mostrar_asientos(self):
           print('Imprimiendo lista de asientos:')
           print("sala {0}".format(self.sala))
           for k in self.asientos:
               print(k)
               
    def capacidad(self):
           for i in self.asientos:
               for j in i:
                   if not j.verificar:
                       return "Aun hay disponibilidad"
           return "El avión esta lleno"
    
        
class Asiento:
    
    def __init__(self):
        self.ocupado= 0
        
    def ocupar(self):
        if self.ocupado == 0:
            self.ocupado= 1
        else:
            print("El lugar ya esta ocupado")
        
    def verificar(self):
        return self.ocupado
        
    def __repr__(self):
        if self.ocupado == 0:
            return "O"
        else:
            return "X"

    
     
#--------------------------------------------------------------------------------        
def main():
    u1 = Usuario('Omar', 'Zacatecas', 'AeroMéxico')
    v1 = Vuelos('Zacatecas', 'AeroMéxico', '10:15 am', Avion("ion",5))
    u2 = Usuario('Brenda', 'Morelos', 'Interjet')
    v2 = Vuelos('Morelos', 'Interjet', '8:30 pm', Avion("ion", 5))
    u3 = Usuario('Jorge', 'Baja California', 'Volaris')
    v3 = Vuelos('Baja California', 'Volaris', '1:15 am', Avion("ion",5))
    a1 = Aeropuerto(r.randrange(8))
    a1.agregar_vuelo(v1)
    a1.agregar_vuelo(v2)
    a1.agregar_vuelo(v3)
    #v1.avion.mostrar_asientos()
    print(u1)
    u1.escoger_vuelo(v1)
    u1.imprimir_pase(a1, v1)
    u1.vuelo.apartar_asiento(3,3)
    u1.vuelo.avion.mostrar_asientos()
    print()
    print(u2)
    u2.escoger_vuelo(v2)
    u2.imprimir_pase(a1, v2)
    u2.vuelo.apartar_asiento(1,3)
    u2.vuelo.avion.mostrar_asientos()
    print()
    print(u3)
    u3.escoger_vuelo(v3)
    u3.imprimir_pase(a1, v3)
    u3.vuelo.apartar_asiento(2,2)
    u3.vuelo.avion.mostrar_asientos()
    print()
    #print(v1)
    
    
    print()
    #u1.imprimir_pase(a1, v1)
    #u2.imprimir_pase(a1, v2)
    #u3.imprimir_pase(a1, v3)
    
    print()
    #print(u1.vuelo)
    #u1.vuelo.apartar_asiento(3,3)
    #u1.vuelo.avion.mostrar_asientos()
    
if __name__ == "__main__":
    main()

