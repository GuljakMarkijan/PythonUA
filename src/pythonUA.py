import sys
import re

translations = {
    "функція": "def", "метод": "def", "повернути": "return", "якщо": "if", "інакше": "else",
    "інакше_якщо": "elif", "для": "for", "доки": "while", "вийди": "break",
    "продовжити": "continue", "в": "in", "і": "and", "або": "or", "не": "not",
    "вивести": "print", "ДонтПушЗеХорсес": "pass", "Правда": "True", "Брехня": "False",
    "Ніц": "None", "клас": "class", "спробувати": "try", "лови": "except",
    "нарешті": "finally", "з": "with", "як": "as", "лямбда": "lambda",
    "глобально": "global", "не_локально": "nonlocal", "певне": "assert",
    "видалити": "del", "поруч": "yield", "викинути": "raise", "імпорт": "import",
    "з_": "from", "ввести": "input", "діапазон": "range",
    "довжина": "len", "сума": "sum", "мінімум": "min", "максимум": "max",
    "від": "abs", "круг": "round", "список": "list", "кортеж": "tuple",
    "словник": "dict", "множина": "set", "фільтр": "filter", "мапа": "map",
    "зменшити": "reduce", "виклик": "callable", "існує": "isinstance",
    "відкрити": "open", "рядок": "str", "число": "int", "число_з_плав": "float",
    "байти": "bytes", "байт_масив": "bytearray", "декілька": "enumerate",
    "спроба_поділити": "divmod", "співставити": "zip", "відновити": "reversed",
    "викликати": "eval", "від_рядка": "exec", "допомога": "help", "тип": "type",
    "глобальні": "globals", "локальні": "locals", "ідентифікатор": "id",
    "приєднати": "dir", "хеш": "hash", "відкрити_файл": "open", "сорт": "sorted",
    "повернути_рядок": "repr", "дійсне": "float", "ціле": "int"
}

def translate_ua_to_py(code: str) -> str:
    py_code = code
    for uk, py in translations.items():
        py_code = re.sub(rf'\b{uk}\b', py, py_code)
    return py_code

REQUIRED_HEADER = "# Слава Ісусу Христу!"

def run_script(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            ua_code = f.read()

        if not ua_code.startswith(REQUIRED_HEADER):
            raise SyntaxError(f"Файл .ua має починатися з: {REQUIRED_HEADER}")

        py_code = translate_ua_to_py(ua_code)
        exec(py_code, globals())
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
    except SyntaxError as e:
        print(f"Синтаксична помилка: {e}")
    except Exception as e:
        print(f"Помилка виконання: {e}")

def repl():
    print("Український Python – Ctrl+C для виходу")
    buffer = ""
    while True:
        try:
            prompt = ">> " if buffer == "" else "... "
            line = input(prompt)
            buffer += line + "\n"
            try:
                exec(translate_ua_to_py(buffer), globals())
                buffer = ""
            except SyntaxError:

                continue
            except Exception as e:
                print(f"Помилка: {e}")
                buffer = ""
        except (EOFError, KeyboardInterrupt):
            print("\nВихід з REPL")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_script(sys.argv[1])
    else:
        repl()