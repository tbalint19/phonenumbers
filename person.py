class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        # implent this method
        self.name = name
        self.phone_number = phone_number
        # pass  # delete this

    def is_phone_number_matching(self, input_phone_number):
        if Person.normalize_phone_number(input_phone_number) == Person.normalize_phone_number(self.phone_number):
            return self
        else:
            return None


    def get_name(self):
        return self.name

    @staticmethod
    def normalize_phone_number(phone_number):
        number_list = []
        for char in phone_number:
            try:
                number_list.append(str(int(char)))
            except:
                continue
        return "".join(number_list)
