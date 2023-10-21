from School import School, ClassRoom, Subject
from Person import Student, Teacher

def main():
    school = School('Adamjee School', 'Model School')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students
    abul = Student('Abul Khan', eight)
    school.student_admission(abul)
    babul = Student('Babul Khan', eight)
    school.student_admission(babul)
    kabul = Student('Kabul Khan', eight)
    school.student_admission(kabul)

    # Subjects
    physics_teacher = Teacher('Azad Sir')
    physics = Subject('physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Topon Sir')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)

    Math_teacher = Teacher('Forid Sir')
    Math = Subject('Math', Math_teacher)
    eight.add_subject(Math)

    eight.take_final_exam()

    print(school)


if __name__ == '__main__':
    main()