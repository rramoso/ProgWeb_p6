#! /usr/bin/env python

import curses, os
from suds.client import Client

url = 'http://localhost:8080/ServerService?wsdl'
client = Client(url)

def printMenu():
    print 'SOAP Client Side'
    print 'Students Management'
    print '=======================\n'

    print 'Menu:'
    print '1: Create'
    print '2: Search'
    print '3: Update'
    print '4: Delete'
    print '5: Read'
    print '0: Exit'

def createStudentOnServer():
    os.system('clear')
    print 'Creating new student...:\n'
    studentId = raw_input('Student ID => ')
    name = raw_input('Name => ')
    career = raw_input('Career => ')

    print('\nAvaiable Subjects:')
    subjects = client.service.listAsignatura()
    for i, subject in enumerate(subjects):
        print '{}: {}'.format(i, subject.name)

    subjectsString = raw_input('Type the code of the subject => ')
    subArray = subjectsString.split(',')
    studentSubjects = []
    for sub in subArray:
        studentSubjects.append(subjects[int(sub)])

    client.service.crearEstudiante(studentId, name, career, studentSubjects)
    raw_input('Student saved. Press ENTER for menu')

def getStudentFromServer():
    os.system('clear')
    studentId = raw_input('Enter the student ID you would like to search => ')
    student = client.service.getEstudiante(studentId)

    print student

    raw_input('Press ENTER for menu')

def updateStudentOnServer():
    os.system('clear')
    studentId = raw_input('Enter the student ID you would like to update => ')
    student = client.service.getEstudiante(studentId)
    student.name = raw_input('Name => ')
    student.career = raw_input('Career => ')
    print('\nAvaiable Subjects:')
    subjects = client.service.listAsignatura()
    for i, subject in enumerate(subjects):
        print '{}: {}'.format(i, subject.name)

    subjectsString = raw_input('Type the code of the subject: => ')
    subArray = subjectsString.split(',')
    studentSubjects = []
    for sub in subArray:
        studentSubjects.append(subjects[int(sub)])

    student.subjects = studentSubjects

    client.service.updateEstudiante(student)

    raw_input('Student updated. Press ENTER for menu')

def removeStudentFromServer():
    os.system('clear')
    studentId = raw_input('Enter the student  ID you would like to delete => ')
    client.service.removeEstudiante(studentId)

    raw_input('Student deleted. Press ENTER for menu')

def listAllStudents():
    os.system('clear')
    print 'Students list\n'
    students = client.service.listEstudiantes()
    for student in students:
        print student

    raw_input('Press ENTER for menu.')

def main():
    while True:
        os.system('clear')
        printMenu()
        select = raw_input('\nEnter the option => ')
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
        if select == '0':
            print '\nClient closed'
            break

if __name__ == '__main__':
    main()
