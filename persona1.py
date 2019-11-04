class Estudiante:
    def iniciar(self,nom,asigna,nota1,nota2,nota3):
        self.nom=nom
        self.asigna=asigna
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
    
    def promedio(self):
        return (self.nota1+self.nota2+self.nota3)/3
    
    def estado(self):
        if(self.promedio()>=4):
            return "Ha aprobado!"
        else:
            return "Siga intentando!"            

    def imprimir(self):
        print("Nombre: ",self.nom)
        print("Asignatura: ",self.asigna)
        print("Nota 1: ",self.nota1, " Nota 2: ",self.nota2, " Nota 3: ", self.nota3)


seguir=True 
while(seguir):
    print (" ---- Clase Estudiante ----")
    print ("1. Ingresar Estudiante ")
    print ("2. Mostrar Estudiante ")
    print ("3. Mostrar Promedio y Estado")
    print ("4. Salir ")
    op=int(input("Digite opcion 1,2,3,4: "))
    sw=False
    if (op==1): 
        unEstudiante=Estudiante()
        nom=input("Nombre?: ")
        asigna=input("Asignatura?: ")
        n1=float(input("Nota 1: "))
        n2=float(input("Nota 2: "))
        n3=float(input("Nota 3: "))
        unEstudiante.iniciar(nom,asigna,n1,n2,n3)
        print("Estudiante Creado con Exito!")
        sw=True
    if (op==2):
    	if(sw==True):
    	   	unEstudiante.imprimir()
    	else:
    		print("Debe crear estudiante antes")
    if (op==3):    
        print("El promedio de la asignatura es: {0:.2f}".format(unEstudiante.promedio()))
        print("Su situación es: ", unEstudiante.estado())
    if (op==4):
        seguir=False 
        print("Programa Terminado!")
