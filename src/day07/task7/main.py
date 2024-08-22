from user import studentList

names = [ ]
def nameCreate( ) :
    global names
    newName = input('newName : ')
    newAge = input('newAge : ')
    student = studentList(newName,newAge)
    names.append(student)
    return

def nameRead( ) :
    global names
    for a in names :
        print(a)
    return

def nameUpdate(  ) :
    global names
    oldName = input('oldName : ')
    for student in names :
        if student.name == oldName :
            newName = input('newName : ')
            newAge = input('newAge : ')
            student.name = newName
            student.age = newAge
            print(student)
        else: print("잘못입력했습니다")
    return

def nameDelete( ) :
    global names
    deleteName = input('deleteName : ')
    for student in names:
        if student.name == deleteName:
            names.remove(student)
        else: print("잘못입력했습니다")
    return


#깃 참조 안보임
if __name__ == "__main__" :
    while True :
        ch = int( input('1.create 2.read 3.update 4.delete : ') )
        if ch == 1 : nameCreate()
        elif ch == 2 : nameRead()
        elif ch == 3 : nameUpdate()
        elif ch == 4 : nameDelete()
        else: break
