class Account:
    def create_Account(self):
        aname = input("Введіть ім'я: ")
        abirthday = input("Введіть дату народження: ")
        aphonenumber = input("Введіть номер телефону: ")
        ae_mail = input("Введіть електрону адресу: ")
        return aname, abirthday, aphonenumber, ae_mail
        print("Аккаунт створено")

    def __init__(self, account_id, aname, abirthday, aphonenumber, ae_mail):
        self.aname = aname
        self.abirthday = abirthday
        self.account_id = account_id
        self.aphonenumber = aphonenumber
        self.ae_mail = ae_mail

    class User(Account):
        def __init__(self, aname, abirthday, account_id, aphonenumber, ae_mail):
            super().__init__(aname, abirthday, account_id, aphonenumber, ae_mail)

    def name_change(self):
        self.aname = input("Введіть нове ім'я: ")
        return self.aname


class Courses:
    def __init__(self, course_name):
        self.course_name = course_name
        self.lesson_name = "null"
        self.course_date = 0

    def create_lesson(self):
        lesson_name = input("Введіть назву заняття")
        course_date = input("Дата публікації заняття")
        return course_date, lesson_name

    def data_change(self):
        self.course_date = input("Нова дата публікації заняття")
        return self.course_date


    def lesson_change(self):
        self.lesson_name = input("Нова назва заняття")
        return self.lesson_name

    def course_info(self):
        return self.course_name, self.course_date, self.lesson_name

    def machine_check(self):
        return self.course_info

