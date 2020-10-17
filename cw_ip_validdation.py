data = '121.45.16.07'
# data = '123'


def is_valid_ip(string):
    true_counter = 0
    for item in string.split('.'):
        if item.isdigit() and 0 <= int(item) <= 255 and item[0] != '0':
            true_counter += 1

    if true_counter == 4:
        return True
    else:
        return False


print(is_valid_ip(data))

#  == вариант через ipaddress ==
# import ipaddress
#
#
# def check_ip(ip):
#     try:
#         ipaddress.ip_address(ip)
#     except ValueError:
#         return False
#     else:
#         return True

#  ==== вариант через регулярку ===
# import re
# def is_valid_IP(strng):
#     return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))