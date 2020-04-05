def main():
    name_and_email = {}
    email = input("Enter you email address:- ")
    if email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/N) ".format(name))
        confirmation.upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
            name_and_email[email] = name

        elif confirmation == "Y":
            for email, name in name_and_email.items():
                print("Welcome {} Your email address is ({})".format(name, email))


def get_name_from_email(email):
    # Pull name from email address
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
