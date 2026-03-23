import re


def normalize_name(lastname: str, firstname: str, surname: str) -> list[str]:
    """collects the first name and last name in the list"""
    full_name = " ".join([lastname, firstname, surname]).split()
    normalized = ["", "", ""]
    if len(full_name) >= 1:
        normalized[0] = full_name[0]
    if len(full_name) >= 2:
        normalized[1] = full_name[1]
    if len(full_name) >= 3:
        normalized[2] = " ".join(full_name[2:])
    return normalized


def format_phone(phone: str) -> str:
    """
    converts the phone to format +7(999)999-99-99 or +7(999)999-99-99 доб.9999
    """
    extension = ""

    pattern = r"(?:доб\.?|ext\.?|extension|\#|x)\s*(\d+)"  # для доб.номера
    is_match = re.search(pattern, phone, re.IGNORECASE)
    if is_match:
        extension = is_match.group(1)
        phone = re.sub(
            pattern,
            "",
            phone,
            flags=re.IGNORECASE,
        )

    digits = re.sub(r"\D", "", phone)
    if len(digits) < 10:
        return phone

    if len(digits) == 11:
        digits = digits[1:]
    elif len(digits) == 10:
        pass
    else:
        return phone

    formatted = f"+7({digits[:3]}){digits[3:6]}-{digits[6:8]}-{digits[8:10]}"
    if extension:
        formatted += f" доб. {extension}"

    return formatted
