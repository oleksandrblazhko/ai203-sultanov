    # Мова програмування Python
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

        def create_lesson(selfesteem):  # Створюемо заняття
            lesson_name = input("Введіть назву заняття")  # Вводимо назву
            course_date = input("Дата заняття")  # Вводимо дату
            time = input("Час заняття")  # Вводимо час
            return course_date, time, lesson_name  # повертаємо значення до системи

        def time_to_lesson(selfesteem, current_time):  # Час до заняття
            time_to_les = selfesteem.time - current_time  # обчислюємо різниця
            return time_to_les  # повертаємо інформацію до системи

        def data_change(selfesteem):  # Зміна дати
            selfesteem.course_date = input("Нова дата заняття")
            return selfesteem.course_date

        def time_change(selfesteem):  # Зміни часу
            selfesteem.time = input("Новий час заняття")
            return selfesteem.time

        def lesson_change(selfesteem):  # Зміна назви
            selfesteem.lesson_name = input("Новий назва заняття")
            return selfesteem.lesson_name

        def course_info(selfesteem):  # Беремо інформацію про весь курс
            return selfesteem.course_name, selfesteem.course_date, selfesteem.lesson_name, selfesteem.time

        def machine_check(selfesteem):  # Надаємо машині інформацію про курс
            return selfesteem.course_info

    class Lector(Consumer):

        def create_description(selfesteem):
            description = input("Введіть опис курсу: ")
            return print(description)
