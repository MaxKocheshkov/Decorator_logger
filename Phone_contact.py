from Logger_for_decor import logger
from Logger_for_decor_2 import logger_2


class Contact:
    def __init__(self, name, surname, phone_number, selected_contact=False, **additionally):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.selected_contact = selected_contact
        self.additionally = additionally

    @logger_2(path='my_logger_2')
    def __str__(self):
        return f' Имя: {self.name}\n Фамилия: {self.surname}\n Телефон: {self.phone_number}\n В избранных: ' \
               f'{self.selected_contact}\n Дополнительная информация:\n \t\t telegram= ' \
               f'{self.additionally.setdefault("telegram")}\n \t\t email= {self.additionally.setdefault("email")}'


if __name__ == '__main__':
    # TEST_START
    jhon = Contact('Jhon', 'Smith', '+71234567809', selected_contact=True, telegram='@jhony', email='jhony@smith.com')
    print(jhon)
