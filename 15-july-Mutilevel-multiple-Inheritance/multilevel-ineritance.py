

class Teacher:

    def teach_class(self):
        print('Teacher is teaching')


class ClassTeacher(Teacher):

    def teach_class(self):
        print('Class teacher is teaching')

class Admin(ClassTeacher):
    pass


admn1=Admin()
admn1.teach_class()

print(Admin.mro())