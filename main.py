from threading import local

from pyscript import display, document

class student:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

student1 = student('Apostol', '10-Emerald', 'Music')
student2 = student('Banaag', '10-Emerald', 'Math')
student3 = student('Zaragoza', '10-Emerald', 'English')
student4 = student('Mamauag', '10-Emerald', 'SS')
student5 = student('Lim', '10-Emerald', 'VE')

def add(e):
    document.getElementById('output').innerHTML = ""

    name = document.getElementById('name').value
    section = document.getElementById('section').value
    subject = document.getElementById('subject').value

    global student6
    student6 = student(name, section, subject)

    display(f'{student6.name} is in {student6.section}. Their favorite subject is {student6.subject}.', target='output')

def introduce(e):
    document.getElementById('output').innerHTML = ""

    global student1, student2, student3, student4, student5, student6

    display(f'{student1.name} is in {student1.section}. Their favorite subject is {student1.subject}.', target='output')
    display(f'{student2.name} is in {student2.section}. Their favorite subject is {student2.subject}.', target='output')
    display(f'{student3.name} is in {student3.section}. Their favorite subject is {student3.subject}.', target='output')
    display(f'{student4.name} is in {student4.section}. Their favorite subject is {student4.subject}.', target='output')
    display(f'{student5.name} is in {student5.section}. Their favorite subject is {student5.subject}.', target='output')
    display(f'{student6.name} is in {student6.section}. Their favorite subject is {student6.subject}.', target='output')

    student1 = student1
    student2 = student2
    student3 = student3
    student4 = student4
    student5 = student5
    student6 = student6