import os


def get_ingredient(line):
    """returns the dict with the ingredient"""
    parts = [part.strip() for part in line.split("|")]
    return {
        "ingredient_name": parts[0],
        "quantity": (
            int(parts[1]) if parts[1].isdigit() else "Задано некорректно"
        ),
        "measure": parts[2],
    }


def read_cookbook(file):
    """reads a file with the extension .txt and returns a dict 'cook_book'"""

    if not os.path.exists(file):
        return f"Файл {file} не найден"

    cook_book = {}

    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        i += 1

        num = lines[i].strip()
        if not num.isdigit():
            return (
                f"Некорректное количество ингредиентов для блюда: {dish_name}"
            )
        ingredients_quantity = int(num)
        i += 1

        ingredients = []
        for _ in range(ingredients_quantity):
            ingredient_line = lines[i].strip()
            ingredients.append(get_ingredient(ingredient_line))
            i += 1

        cook_book[dish_name] = ingredients

        while i < len(lines) and not lines[i].strip():
            i += 1

    return cook_book


if __name__ == "__main__":
    FILENAME = "recipes.txt"
    print(read_cookbook(FILENAME))
