class Student:
    def __init__(self, name, surname, gender):
        self._name = name
        self._surname = surname
        self._gender = gender
        self._finished_courses = []
        self._courses_in_progress = []
        self._grades = {}

    @property
    def courses_in_progress(self):
        return self._courses_in_progress

    @courses_in_progress.setter
    def courses_in_progress(self, course):
        if isinstance(course, list):
            self._courses_in_progress.extend(course)
        elif isinstance(course, str):
            self._courses_in_progress.append(course)

    @property
    def finished_courses(self):
        return self._finished_courses

    @finished_courses.setter
    def finished_courses(self, course):
        if isinstance(course, list):
            self._finished_courses.extend(course)
        elif isinstance(course, str):
            self._finished_courses.append(course)

    @property
    def grades(self):
        return self._grades

    def rate_lecture(self, lecturer, course, grade):
        """the student gives a grade to the lecturer"""
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def get_average_grade(self):
        """calculates the average score based on the grades for all courses"""
        if self._grades:
            grades_list = [
                grade for gr_list in self._grades.values() for grade in gr_list
            ]
            return round(sum(grades_list) / len(grades_list), 2)
        return 0.0

    def __str__(self):
        return (
            f"Имя: {self._name}\n"
            f"Фамилия: {self._surname}\n"
            f"Средняя оценка за домашние задания: {self.get_average_grade()}\n"
            f"Курсы в процессе изучения: {', '.join(self._courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self._finished_courses)}"
        )

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() > other.get_average_grade()
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return False


class Mentor:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._courses_attached = []

    @property
    def courses_attached(self):
        return self._courses_attached

    @courses_attached.setter
    def courses_attached(self, course):
        if isinstance(course, list):
            self._courses_attached.extend(course)
        elif isinstance(course, str):
            self._courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._grades = {}

    @property
    def grades(self):
        """По причине того, что геттер возвращает ссылку на словарь оценок,
        для изменений словаря (изменяемого объекта) тоже достаточно данного
        геттера.
        Понимаю, что во 'взрослой жизни' так поступать нельзя"""
        return self._grades

    def get_average_grade(self):
        """calculates the average score based on the grades for all courses"""
        if self.grades:
            grades_list = [
                grade for gr_list in self.grades.values() for grade in gr_list
            ]
            return round(sum(grades_list) / len(grades_list), 2)
        return 0.0

    def __str__(self):
        return (
            f"Имя: {self._name}\n"
            f"Фамилия: {self._surname}\n"
            f"Средняя оценка за лекции: {self.get_average_grade()}"
        )

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() == other.get_average_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() > other.get_average_grade()
        return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return False


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """the reviewer evaluates the student"""
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self._name}\nФамилия: {self._surname}"


def calculate_average_grade_students(students, course):
    """
    calculates the average grade for homework for all students
    in a particular course
    """
    grades_list = []
    for student in students:
        grade = student.grades.get(course)
        if grade:
            grades_list += grade
    if grades_list:
        return round(sum(grades_list) / len(grades_list), 2)
    return 0.0


def calculate_average_grade_lecturers(lecturers, course):
    """
    calculates the average grade for the lectures of all
    lecturers within the course
    """
    grades_list = []
    for lecturer in lecturers:
        grade = lecturer.grades.get(course)
        if grade:
            grades_list += grade
    if grades_list:
        return round(sum(grades_list) / len(grades_list), 2)
    return 0.0


lecturer_1 = Lecturer("Иван", "Иванов")
lecturer_2 = Lecturer("Моисей", "Шниперсон")
student_1 = Student("Ольга", "Алёхина", "Ж")
student_2 = Student("Абрам", "Рабинович", "М")
reviewer_1 = Reviewer("Пётр", "Петров")
reviewer_2 = Reviewer("Сара", "Зальцман")

lecturer_1.courses_attached = ["Python", "Git"]
lecturer_2.courses_attached = ["Python", "Java"]

student_1.courses_in_progress = ["Python", "Java", "Git"]
student_1.finished_courses = ["Введение в программирование"]
student_1.rate_lecture(lecturer_1, "Python", 10)
student_1.rate_lecture(lecturer_1, "Git", 6)
student_1.rate_lecture(lecturer_2, "Python", 9)
student_1.rate_lecture(lecturer_2, "Git", 9)

student_2.courses_in_progress = ["Python", "C++", "Git"]
student_2.finished_courses = ["JavaScript", "Git"]
student_2.rate_lecture(lecturer_1, "Python", 7)
student_2.rate_lecture(lecturer_1, "Git", 7)
student_2.rate_lecture(lecturer_2, "Python", 8)
student_2.rate_lecture(lecturer_2, "Git", 8)

reviewer_1.courses_attached = ["Python", "C++", "Git"]
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Git", 6)
reviewer_1.rate_hw(student_2, "Python", 7)
reviewer_1.rate_hw(student_2, "Git", 10)

reviewer_2.courses_attached = ["Python", "Git"]
reviewer_2.rate_hw(student_1, "Python", 10)
reviewer_2.rate_hw(student_1, "Git", 8)
reviewer_2.rate_hw(student_2, "Python", 8)
reviewer_2.rate_hw(student_2, "Git", 7)


print("ЛЕКТОРЫ")
print(lecturer_1)
print("-" * 12)
print(lecturer_2)
print("=" * 16)
print("ПРОВЕРЯЮЩИЕ")
print(reviewer_1)
print("-" * 12)
print(reviewer_2)
print("=" * 16)
print("СТУДЕНТЫ")
print(student_1)
print("-" * 12)
print(student_2)
print("=" * 16)
print("Равенство студентов по средней оценке успеваемости:")
print(student_1 == student_2)
print("Ошибочное сравнение студента и проверяющего:")
print(student_2 == reviewer_1)
print("Успеваемость у студента_1 лучше, чем у студента_2 ?:")
print(student_1 > student_2)
print("Успеваемость у студента_1 хуже, чем у студента_2 ?:")
print(student_1 < student_2)
print("=" * 16)
print("Равенство лекторов по средней оценке за лекции:")
print(lecturer_1 == lecturer_2)
print("Средняя оценка за лекции у лектора_1 выше, чем у лектора_2 ?:")
print(lecturer_1 > lecturer_2)
print("Средняя оценка за лекции у лектора_1 ниже, чем у лектора_2 ?:")
print(lecturer_1 < lecturer_2)
print("=" * 16)

print("Средняя оценка всех студентов за домашние задания по Python:")
print(calculate_average_grade_students([student_1, student_2], "Python"))
print("Средняя оценка всех студентов за домашние задания по Git:")
print(calculate_average_grade_students([student_1, student_2], "Git"))

print("Средняя оценка всех лекторов за курс по Python:")
print(calculate_average_grade_lecturers([lecturer_1, lecturer_2], "Python"))
print("Средняя оценка всех лекторов за курс по Git:")
print(calculate_average_grade_lecturers([lecturer_1, lecturer_2], "Git"))
