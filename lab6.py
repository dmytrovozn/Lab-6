class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def info(self):
        print(f"Ім'я: {self.name}, Оцінки: {self.grades}")
        
class StudentAction:
    def __init__(self):
        self.students = []

    def save_to_file(self):
        with open(r'C:\Users\Admin\PycharmProjects\pythonProject\1\user.txt', 'w', encoding='utf-8') as file:
            for student in self.students:
                file.write(f"{student.name};{','.join(map(str, student.grades))}\n")
    
    def add_student(self, student):
        self.students.append(student)
        self.save_to_file()

    def remove_student(self, student_name):
        new_students = []
        for student in self.students:
            if student.name != student_name:
                new_students.append(student)
        self.students = new_students
        self.save_to_file()

    def display_all_students(self):
        for student in self.students:
            student.info()

    def add_grade(self, student_name, grade):
        for student in self.students:
            if student.name == student_name:
                student.grades.append(grade)
                self.save_to_file()
                break
        else:
            print(f"Учень з ім'ям {student_name} не знайдений.")

    def load_from_file(self):
        with open(r'C:\Users\Admin\PycharmProjects\pythonProject\1\user.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(';')
                name = data[0]
                grades = data[1].split(',')
                new_student = Student(name)
                    
                not_empty_grades = []
                for grade in grades:
                    if grade:
                        not_empty_grades.append(grade)
                new_student.grades = not_empty_grades  

                self.students.append(new_student)   
                      
class_log = StudentAction()
class_log.load_from_file()

while True:
    print("""1. Додати учня.
2. Прибрати учня.
3. Додати оцінку учневі.
4. Показати всіх учнів.
5. Вийти.""")
    choice = input("Виберіть, що потрібно зробити:")
    if choice == "1":
        name = input("Введіть ім'я учня:")
        new_student = Student(name)
        class_log.add_student(new_student)
        print(f"Учень {name} доданий.")
    elif choice == "2":
        name_remove = input("Введіть ім'я учня, якого потрібно прибрати:")
        class_log.remove_student(name_remove)
        print(f"Учень {name_remove} був прибраний.")
    elif choice == "3":
        name_add_grade = input("Введіть ім'я учня, якому потрібно додати оцінку:")
        grade = input("Введіть оцінку:")
        class_log.add_grade(name_add_grade, grade)
    elif choice == "4":
        print("Список учнів:")
        class_log.display_all_students()
    elif choice == "5":
        print("Ви вийшли з программи.")
        break
    else:
        print("Введіть можливий варіант!")