import json


def main():
    # Путь к файлу Jupyter Notebook
    notebook_path = "Intro_into_Pytorch.ipynb"

    # Чтение содержимого файла
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    # Удаляем metadata.widgets, если он есть
    if "widgets" in notebook_data.get("metadata", {}):
        del notebook_data["metadata"]["widgets"]

    # Перезаписываем файл
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(notebook_data, f, indent=2)

if __name__ == "__main__":
    main()
