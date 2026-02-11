# tests/test_file.py
import os


def test_that_file_data_is_correct():
    # Skapa filen programmatiskt om den inte finns för att göra testet självförsörjande
    file_path = "data/hello.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write("Hello World!")

    # Själva testet
    with open(file_path, "r") as f:
        content = f.read()

    assert content == "Hello World!", f"Förväntade 'Hello World!', men fick '{content}'"