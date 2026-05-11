import re


def main():
    # Отримуємо текст від користувача
    text = input("Текст: ").strip()

    if not text:
        return

    # Рахуємо кількість літер (тільки латинські букви)
    letters = len(re.findall(r'[a-zA-Z]', text))

    # Рахуємо кількість слів
    words = len(text.split())

    # Рахуємо кількість речень (маркери: . ! ?)
    sentences = len(re.findall(r'[.!?]', text))

    # L — середня кількість літер на 100 слів
    # S — середня кількість речень на 100 слів
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Обчислення індексу Коулмана-Ліау
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    # Вивід результату згідно з вимогами
    if grade >= 16:
        print("Оцінка 16+")
    elif grade < 1:
        print("До 1-го класу")
    else:
        print(f"Оцінка {grade}")


if __name__ == "__main__":
    main()
