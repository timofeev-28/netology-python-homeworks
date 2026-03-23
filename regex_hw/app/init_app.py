import os
import csv
from app.utils import format_phone, normalize_name


def clean_phonebook():
    """reads and corrects data from a file and writes it to a new file"""
    filename = os.path.join(os.getcwd(), "app", "files", "phonebook_raw.csv")
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    contacts_dict = {}
    for c in contacts_list[1:]:
        lastname, firstname, surname = normalize_name(c[0], c[1], c[2])
        key = (lastname, firstname)

        phone_number = c[5]
        if phone_number:
            phone_number = format_phone(phone_number)

        if key not in contacts_dict:
            contacts_dict[key] = [
                lastname,
                firstname,
                surname,
                c[3],  # organization
                c[4],  # position
                phone_number,
                c[6],  # email
            ]
        else:
            existing = contacts_dict[key]
            new_data = [
                lastname,
                firstname,
                surname,
                c[3],
                c[4],
                phone_number,
                c[6],
            ]

            for i in range(len(existing)):
                if not existing[i] and new_data[i]:
                    existing[i] = new_data[i]

    new_list = [contacts_list[0]]
    new_list.extend(contacts_dict.values())

    new_filename = os.path.join(os.getcwd(), "app", "files", "phonebook.csv")
    os.makedirs(os.path.dirname(new_filename), exist_ok=True)
    with open(new_filename, "w", encoding="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(new_list)
