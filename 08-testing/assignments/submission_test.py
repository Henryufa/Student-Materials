import pytest
import System
import json
import TA
import Student


username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.login(username,password)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    if grading_system.users[username]['password'] == data[username]['password']:
        assert True
    else:
        assert False

def test_check_password(grading_system):
    username = 'calyam' 
    password =  '#yeet'
    grading_system.login(username,password)
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False
    else:
        assert True

#Tests if the program can change a grade
def test_change_grade(grading_system):
    username = 'cmhbf5'
    password =  'bestTA'
    Stusername = 'akend3'
    course = 'databases'
    assignment = 'assignment1'
    grade = -10
    grading_system.login(username,password)
    grading_system.usr.change_grade(Stusername,course, assignment, grade)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    print(data[Stusername]['courses'][course][assignment]['grade'])
    if data[Stusername]['courses'][course][assignment]['grade'] == grade:
        assert True
    else:
        assert False

def test_create_assignment(grading_system):
    TAusername = 'cmhbf5'
    TApassword =  'bestTA'
    assignment = 'foofaa'
    due_date1 = '2/1/22'
    course1 = 'comp_sci'
    grading_system.login(TAusername,TApassword)
    grading_system.usr.create_assignment(assignment,due_date1,course1)
    with open('Data/courses.json', "r") as f:
        data = json.load(f)
        if data[course1]['assignments'][assignment]['due_date'] == due_date1:
            assert True
        else:
            assert False


#Tests if the program can add a student to a class
def test_add_student(grading_system):
    profUser = 'goggins'
    profPass = 'augurrox'
    Stusername = 'akend3'
    courseToAdd = 'software_engineering'
    grading_system.login(profUser,profPass)
    grading_system.usr.add_student(Stusername,courseToAdd)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    res = False
    for key in data[Stusername]['courses']:
        if key == 'comp_sci':
            res = True
    assert res



#Tests if the program can drop a student
def test_drop_student(grading_system):
    course1 = 'comp_sci'
    course2 = 'databases'
    Stusername = 'akend3'
    courseToAdd = 'comp_sci'
    grading_system.login(profUser,profPass)
    grading_system.usr.drop_student(Stusername,courseToAdd)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    res = True
    for key in data[Stusername]['courses']:
        if key == 'comp_sci':
            res = False
    assert res

def test_submit_assignment(grading_system):
    Stusername = 'akend3'
    Stpassword = '123454321'
    course = 'databases'
    assignment = 'assignment1'
    submission = 'foofoo'
    submission_date = '1/2/22'
    grading_system.login(Stusername,Stpassword)
    grading_system.usr.submit_assignment(course,assignment,submission,submission_date)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    assignmentInDB = data[Stusername]['courses'][course][assignment]
    if assignmentInDB['submission'] == submission and assignmentInDB['submission_date'] == submission_date and assignmentInDB['ontime'] == False:
        assert True
    else:
        assert False

def test_check_ontime(grading_system):
    Stusername = 'akend3'
    Stpassword = '123454321'
    grading_system.login(Stusername,Stpassword)
    first_date = '1/2/22'
    second_date = '1/3/22'
    res = True
    if True != grading_system.usr.check_ontime(first_date,second_date):
        res = False
    if False != grading_system.usr.check_ontime(second_date,first_date):
        res = False
    assert res

def test_check_grades(grading_system):
    Stusername = 'akend3'
    Stpassword = '123454321'
    course = 'databases'
    grading_system.login(Stusername,Stpassword)    
    grades = grading_system.usr.check_grades(course)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    gradesInDB = []
    assignments = data[Stusername]['courses'][course]
    for key in assignments:
        grades.append([key, assignments[key]['grade']])
    res = True
    for grade in gradesInDB:
        if grade not in grades:
            res = False
    assert res

def test_view_assignments(grading_system):
    Stusername = 'akend3'
    Stpassword = '123454321'
    course = 'databases'
    grading_system.login(Stusername,Stpassword)      
    assignments = grading_system.usr.view_assignments(course)
    with open('Data/courses.json', "r") as f:
        data = json.load(f)   
    course = data[course]['assignments']
    assignmentsInDB = []
    for key in course:
        assignmentsInDB.append([key,course[key]['due_date']])  
    res = True 
    for assignment in assignmentsInDB:
        if assignment not in assignments:
            res = False
    assert res

def test_add_student_to_wrong_class(grading_system):
    profUser = 'goggins'
    profPass = 'augurrox'
    Stusername = 'hdjsr7'
    courseToAdd = 'comp_sci'
    grading_system.login(profUser,profPass)
    grading_system.usr.add_student(Stusername,courseToAdd) 
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    res = False
    for key in data[Stusername]['courses']:
        if key == courseToAdd:
            res = True
    assert res

def test_drop_student_wrong_class(grading_system):
    profUser = 'saab'
    profPass = 'boomr345'    
    Stusername = 'akend3'
    courseToDrop = 'databases'
    grading_system.login(profUser,profPass)
    grading_system.usr.drop_student(Stusername,courseToDrop)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    res = False
    for key in data[Stusername]['courses']:
        if key == courseToDrop:
            res = True
    assert res

def test_change_grade_wrong_course(grading_system):
    username = 'cmhbf5'
    password =  'bestTA'
    Stusername = 'hdjsr7'
    course = 'databases'
    assignment = 'assignment1'
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    grade = -10
    originalGrade = data[Stusername]['courses'][course][assignment]['grade']
    grading_system.login(username,password)
    grading_system.usr.change_grade(Stusername,course, assignment, grade)
    with open('Data/users.json', "r") as f:
        data = json.load(f)
    print(data[Stusername]['courses'][course][assignment]['grade'])
    if data[Stusername]['courses'][course][assignment]['grade'] == originalGrade:
        assert True
    else:
        assert False

def test_create_assignment_wrong_course(grading_system):
    TAusername = 'cmhbf5'
    TApassword =  'bestTA'
    assignment = 'foofaa'
    due_date1 = '2/1/22'
    course1 = 'comp_sci'
    grading_system.login(TAusername,TApassword)
    grading_system.usr.create_assignment(assignment,due_date1,course1)
    with open('Data/courses.json', "r") as f:
        data = json.load(f)
        if data[course1]['assignments'][assignment]['due_date'] == due_date1:
            assert False
        else:
            assert True
def test_check_grades_wrong_course(grading_system):
    TAusername = 'cmhbf5'
    TApassword =  'bestTA'
    Stusername = 'hdjsr7'
    course = 'databases'
    grading_system.login(TAusername,TApassword)    
    grades = grading_system.usr.check_grades(Stusername,course)
    if(len(grades) > 0):
        assert False
    else:
        assert True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


