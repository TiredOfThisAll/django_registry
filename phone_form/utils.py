def split_phone_number(phone_number):
    phone_number_dict = {}
    phone_number_dict["country_code"] = phone_number[0]
    phone_number_dict["operator_code"] = phone_number[1:4]
    phone_number_dict["rest_numbers"] = phone_number[4:]
    return phone_number_dict
