# ФУНКЦИЯ get_average_grade ПОВТОРЯЕТСЯ 2 РАЗА - я не уверен, нормально ли это
# в рамках задания, или можно сделать общий класс с name, surname и
# get_average_grade для всех, и далее наследоваться...


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        if self.grades:
            grades_list = [
                grade for gr_list in self.grades.values() for grade in gr_list
            ]
            return round(sum(grades_list) / len(grades_list), 2)
        return 0.0

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.get_average_grade()}\n"
            f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {", ".join(self.finished_courses)}"
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
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

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
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
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
        return f"Имя: {self.name}\nФамилия: {self.surname}"
