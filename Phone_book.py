from Phone_contact import Contact
from Logger_for_decor import logger

book_dict = {}


class PhoneBook:

    def __init__(self, name_book):
        self.name_book = name_book
        self.contacts = []

    def write_in_book(self, contact: Contact):
        self.contact_dict = {
            'Имя': contact.name,
            'Фамилия': contact.surname,
            'Номер телефона': contact.phone_number,
            'В избранных': contact.selected_contact,
            'Дополнительная информация': contact.additionally
        }
        self.contacts.append(self.contact_dict)
        book_dict.update({self.name_book: self.contacts})

    @logger
    def conclusion(self):
        return book_dict

    def del_for_number(self):
        user_del_number = int(input('Введите номер для удаления: '))
        for contacts_list in book_dict.values():
            for self.contact_dict in contacts_list:
                if user_del_number in self.contact_dict.values():
                    contacts_list.remove(self.contact_dict)
                    return f'{book_dict}'

    def selected_phone(self):
        output_list = []
        for contacts_list in book_dict.values():
            selected_list = contacts_list.copy()
            for self.contact_dict in selected_list:
                if self.contact_dict['В избранных'] == 'да':
                    dict_index = selected_list.index(self.contact_dict)
                    output_list.append(selected_list.pop(dict_index))
                    output_list.extend(output_list)
                    return output_list

    def name_search(self):
        user_search_name = input('Введите имя для поиска: ')
        user_search_surname = input('Введите фамилию для поиска: ')
        for contacts_list in book_dict.values():
            for self.contact_dict in contacts_list:
                if user_search_name in self.contact_dict['Имя'] and user_search_surname in self.contact_dict['Фамилия']:
                    return self.contact_dict
