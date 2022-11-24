class Consumer:
    def __init__(self, name, surname, consumer_id, credit_card):
        self.name = name
        self.surname = surname
        self.consumer_id = consumer_id
        self.credit_card = credit_card

    def name_change(self):
        self.name = input("Введіть нове ім'я: ")
        return self.name


class Courses:
    def __init__(self, course_name):
        self.course_name = course_name
        self.lesson_name = "null"
        self.course_date = 0
        self.time = 0

    def create_lesson(self):
        self = input("Введіть назву курсу")
        course_date = input("Дата курсу")
        return course_date, lesson_name

    def time_to_lesson(self, current_time):
        time_to_les = current_time - selfesteem.time
        return time_to_les

    def data_change(self):
        self.course_date = input("Нова дата курсу")
        return self.course_date

    def time_change(self):
        self.time = input("Новий час курсу")
        return self.time

    def lesson_change(self):
        self.lesson_name = input("Нова назва курсу")
        return self.lesson_name

    def course_info(self):
        return self.course_name, self.course_date, self.lesson_name, self.time

    def machine_check(self):
        return self.course_info


class Lector(Consumer):

    def create_description(self):
        description = input("Введіть опис курсу: ")
        return print(description)
