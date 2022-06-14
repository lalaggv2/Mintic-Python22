# -*- coding: utf-8 -*-
"""Funciones y clases.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CW-0tlsqM9PKKdeTBgbK9l8v6MyThpVa

**Funciones**
"""

#Función que no recibe ningun parámetro
def digaHola():
  print("Hola")

digaHola()

#Función que recibe un parámetro tipo string, el + concatena texto
def holaconNombre(name):
  print("Hola "+name+"!")

holaconNombre("Erika")

#Función que recibe dos parametros de tipo entero, y almacena un valor en un parámetro
def sumar(numero1,numero2=5):
  print(numero1+numero2)

sumar(2)
sumar(5,8)

"""**Clases**"""

class Alumno:
  #Definimos la funcion constructora, creamos el objeto
  def __init__(self,nombre):
    print(f"Creando el alumno {nombre}")
    self.nombre=nombre
  #Función/método que saluda al alumno
  def saludar(self):
    print(f"¡Hola, {self.nombre} !")

#Llamamos el contenido de la clase
alumno = Alumno("Margarita")
alumno.saludar()

class Perro: 

  #Definimos una función o método __init__ funciona para crear el objeto
  def __init__(self, nombre,raza):
    print(f"Creando perro {nombre}, {raza}")

    self.nombre = nombre
    self.raza = raza 

  def ladra(self):
    print("Guau")
  
  def camina(self,pasos):
    print(f"Caminando {self.nombre} {pasos} pasos")


miPerro = Perro("Mila","Westy")
miPerro.ladra()
miPerro.camina(15)

otroPerro = Perro("Tommy","Bulldog")
otroPerro.camina(80)

#Clase anidada
class Departamento:
  def __init__(self, nombreD):
    self.nombreD=nombreD

  class Profesor:
    def __init__(self, nombreP):
      self.nombreP = nombreP

departamento1 = Departamento("Matematicas")
profesorDepto = Departamento.Profesor("Alex")

print(departamento1.nombreD)
print(profesorDepto.nombreP)