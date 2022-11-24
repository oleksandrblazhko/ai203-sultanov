
class Consumer:
    def __init__(selfesteem, name, surname, consumer_id, credit_card):
        selfesteem.name = name
        selfesteem.surname = surname
        selfesteem.consumer_id = consumer_id
        selfesteem.credit_card = credit_card

    def name_change(selfesteem):
        selfesteem.name = input("Введіть нове ім'я: ")
        return selfesteem.name


class Courses:
    def __init__(selfesteem, course_name):
        selfesteem.course_name = course_name
        selfesteem.lesson_name = "null"
        selfesteem.course_date = 0
        selfesteem.time = 0

    def create_lesson(selfesteem):
        lesson_name = input("Введіть назву заняття")
        course_date = input("Дата публікації заняття")
        return course_date, lesson_name

    def time_to_lesson(selfesteem, current_time):
        time_to_les = current_time - selfesteem.time
        return time_to_les

    def data_change(selfesteem):
        selfesteem.course_date = input("Нова дата заняття")
        return selfesteem.course_date

    def time_change(selfesteem):
        selfesteem.time = input("Новий час заняття")
        return selfesteem.time

    def lesson_change(selfesteem):
        selfesteem.lesson_name = input("Нова назва заняття")
        return selfesteem.lesson_name

    def course_info(selfesteem):
        return selfesteem.course_name, selfesteem.course_date, selfesteem.lesson_name, selfesteem.time

    def machine_check(selfesteem):
        return selfesteem.course_info


class Lector(Consumer):

    def create_description(selfesteem):
        description = input("Введіть опис курсу: ")
        return print(description)
