import os


def read_files(files):
    """reads files and sorts them in ascending order"""
    files_list = []
    for file in files:
        if not os.path.exists("./exercise3/" + file):
            print(f"Файл {file} не найден")
            continue
        with open("./exercise3/" + file, "r", encoding="utf-8") as f:
            content = f.readlines()
        files_list.append(
            {"name": file, "length": len(content), "text": content}
        )
    sorted_files = sorted(files_list, key=lambda f: f["length"])
    return sorted_files


def write_file():
    """writes the resulting file"""
    files_list = ["1.txt", "2.txt", "3.txt"]
    files = read_files(files_list)
    name = "result_file.txt"

    with open(name, "w", encoding="utf-8") as f:
        for file in files:
            f.write(f"{file['name']}\n")
            f.write(f"{file['length']}\n")
            f.write(f"{"".join(file["text"])}")


if __name__ == "__main__":
    write_file()
