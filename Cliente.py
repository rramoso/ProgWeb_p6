#! /usr/bin/env python

import curses, os
from suds.client import Client

url = 'http://localhost:8080/ServerService?wsdl'
client = Client(url)

def printMenu():
    print 'Cliente SOAP WebService'
    print '=======================\n'

    print 'Opciones:'
    print '1: Crear Estudiante'
    print '2: Obtener Estudiante'
    print '3: Actualizar Estudiante'
    print '4: Borrar Estudiante'
    print '5: Lista de Estudiantes'
    print '0: Cerrar Cliente'

def createStudentOnServer():
    os.system('clear')
    print 'Creando nuevo Estudiante:\n'
    studentId = raw_input('Matricula => ')
    name = raw_input('Nombre => ')
    career = raw_input('Carrera => ')

    print('\nAsignaturas disponibles:')
    subjects = client.service.listAsignatura()
    for i, subject in enumerate(subjects):
        print '{}: {}'.format(i, subject.name)

    subjectsString = raw_input('Ingrese los codigos de asignaturas a la que pertenece este estudiante => ')
    subArray = subjectsString.split(',')
    studentSubjects = []
    for sub in subArray:
        studentSubjects.append(subjects[int(sub)])

    client.service.crearEstudiante(studentId, name, career, studentSubjects)
    raw_input('Estudiante creado con exito! Presione ENTER para volver al menu.')

def getStudentFromServer():
    os.system('clear')
    studentId = raw_input('Ingrese la matricula del estudiante que desea => ')
    student = client.service.getEstudiante(studentId)

    print student

    raw_input('Presione ENTER para volver al menu.')

def updateStudentOnServer():
    os.system('clear')
    studentId = raw_input('Ingrese la matricula del estudiante que desea actualizar => ')
    student = client.service.getEstudiante(studentId)
    student.name = raw_input('Ingrese el nombre del Estudiante => ')
    student.career = raw_input('Ingrese la carrera del Estudiante => ')
    print('\nAsignaturas disponibles:')
    subjects = client.service.listarAsignaturas()
    for i, subject in enumerate(subjects):
        print '{}: {}'.format(i, subject.name)

    subjectsString = raw_input('Ingrese los codigos de asignaturas a la que pertenece este estudiante => ')
    subArray = subjectsString.split(',')
    studentSubjects = []
    for sub in subArray:
        studentSubjects.append(subjects[int(sub)])

    student.subjects = studentSubjects

    client.service.updateEstudiante(student)

    raw_input('Estudiante actualizado con exito! Presione ENTER para volver al menu.')

def removeStudentFromServer():
    os.system('clear')
    studentId = raw_input('Ingrese la matricula del estudiante que desea eliminar => ')
    client.service.removeEstudiante(studentId)

    raw_input('Estudiante eliminado con exito! Presione ENTER para volver al menu.')

def listAllStudents():
    os.system('clear')
    print 'Lista de Estudiantes:\n'
    students = client.service.listEstudiantes()
    for student in students:
        print student

    raw_input('Presione ENTER para volver al menu.')

def main():
    while True:
        os.system('clear')
        printMenu()
        select = raw_input('\nDigite una de las opciones => ')
        if select == '1':
            createStudentOnServer()
        if select == '2':
            getStudentFromServer()
        if select == '3':
            updateStudentOnServer()
        if select == '4':
            removeStudentFromServer()
        if select == '5':
            listAllStudents()
        if select == '0:
            print '\nGracias por utilizar el Cliente SOAP!'
            break

if __name__ == '__main__':
    main()
