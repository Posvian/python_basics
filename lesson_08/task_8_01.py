import re


def email_parse(email_address):
    re_email = re.compile(r"(?P<username>[A-z0-9'\._\+-]+)@(?P<domain>[A-z0-9-]+\.+[A-z]+\.*[A-z]*)")
    rezult = re_email.match(email_address)
    if rezult is None:
        raise ValueError(f'wrong email: {email_address}')
    else:
        rezult = re_email.finditer(email_address)
        for i in rezult:
            return i.groupdict()


print(email_parse('someone@geekbrains.ru'))
