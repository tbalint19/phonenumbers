import csv
import sys
from person import Person


def open_csv(file_name):
    list_of_people = []
    with open(file_name) as csvfile:
        phone_book = csv.reader(csvfile)

        for row in phone_book:
            person = Person(row[0], row[1])
            list_of_people.append(person)

    return list_of_people


def get_csv_file_name(argv_list):
    file_name = argv_list[1:]
    if len(file_name) == 0:
        return None
    return file_name[0]


def format_output(person):
    return "This number belongs to: " + person.get_name()


def get_person_by_phone_number(person_list, user_input_phone_number):
    for person in person_list:
        if person.is_phone_number_matching(user_input_phone_number) == person:
            return person



def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)


    print(format_output(match_person))

if __name__ == '__main__':
    main()
