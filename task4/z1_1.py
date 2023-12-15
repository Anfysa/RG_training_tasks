class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in self.courses_in_progress:
                if course in lecturer.courses_attached:
                    if course in lecturer.lecture_grades:
                        lecturer.lecture_grades[course].append(grade)
                        print(f"Оценка выставлена.")
                    else:
                        print(f"Ошибка: лектор не преподает курс.")
                else:
                    print(f"Ошибка: лектор не преподает курс.")
            else:
                print(f"Ошибка: студент не записан на курс.")
        else:
            print("Ошибка: переданный объект не является лектором.")

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()
    
    def get_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_subjects = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_subjects if total_subjects > 0 else 0
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = []

    def __str__(self):
        avg_lecture_grade = sum(sum(grades) / len(grades) for grades in self.lecture_grades.values()) / len(self.lecture_grades) if self.lecture_grades else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_lecture_grade:.1f}'

    def get_average_lecture_grade(self):
        total_grades = sum(sum(grades) for grades in self.lecture_grades.values())
        total_lectures = sum(len(grades) for grades in self.lecture_grades.values())
        return total_grades / total_lectures if total_lectures > 0 else 0
    
    def __lt__(self, other):
        return self.get_average_lecture_grade() < other.get_average_lecture_grade()

    def __eq__(self, other):
        return self.get_average_lecture_grade() == other.get_average_lecture_grade()

    def __gt__(self, other):
        return self.get_average_lecture_grade() > other.get_average_lecture_grade()
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nУ лекторов'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
student1 = Student('Ruoy', 'Eman', 'Male')
student1.courses_in_progress = ['Python', 'Data Science']
student1.finished_courses = ['JavaScript']
student1.grades = {'Python': [8, 9, 7], 'Data Science': [10, 9, 8]}

student2 = Student('John', 'Doe', 'Male')
student2.courses_in_progress = ['Python', 'JavaScript']
student2.finished_courses = ['Data Science']
student2.grades = {'Python': [7, 8, 9], 'JavaScript': [10, 8, 9]}

lecturer1 = Lecturer('Jane', 'Doe')
lecturer1.courses_attached = ['Python']
lecturer1.lecture_grades = {'Python': [9, 10, 8]}

lecturer2 = Lecturer('Bob', 'Smith')
lecturer2.courses_attached = ['JavaScript']
lecturer2.lecture_grades = {'JavaScript': [10, 8, 9]}

reviewer1 = Reviewer('Alice', 'Johnson')
reviewer1.courses_attached = ['Python', 'JavaScript']

reviewer2 = Reviewer('Charlie', 'Brown')
reviewer2.courses_attached = ['Data Science']

# Вызываем методы
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer2, 'JavaScript', 9)

print(lecturer1)
print(lecturer2)

print(f"Средняя оценка студента 1: {student1.get_average_grade()}")
print(f"Средняя оценка студента 2: {student2.get_average_grade()}")
print(student1.__lt__(student2))
print(student1.__eq__(student2))

print(f"Средняя оценка лектора 1: {lecturer1.get_average_lecture_grade()}")
print(f"Средняя оценка лектора 2: {lecturer2.get_average_lecture_grade()}")
print(lecturer2.__gt__(lecturer1))
