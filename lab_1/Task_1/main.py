import argparse

def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Шифрование текста с использованием шифра Виженера")
    parser.add_argument("_text", type=str, help="Текст для шифрования")
    parser.add_argument("_key", type=str, help="Ключ для шифрования")
    args = parser.parse_args()
    return args


text_1 = (
    "Посол Франции в Риме Блез де Виженер, познакомившись с трудами Тритемия, Белазо, Кардано, Порта, Альберти,"
    "также увлёкся криптографией. В 1585 году он написал «Трактат о шифрах», в котором излагаются основы криптографии. "
    "В этом труде он замечает: «Все вещи в мире представляют собой шифр. Вся природа является просто шифром и "
    "секретным письмом». Эта мысль была позднее повторена Блезом Паскалем — одним из основоположников теории "
    "вероятностей, а в XX веке и Норбертом Винером — «отцом кибернетики». По сути дела Виженер объединил подходы "
    "Тритемия, Беллазо, Порта к шифрованию открытых текстов, по существу не внеся в них ничего оригинального."
)
key_1 = "ибас"


def shifr(text, key):
    """
    Функция кодирования текста при помощи метода Вижинера
    :param text: шифруемый текст
    :param key: ключ шифрования
    :return: зашифрованный текст
    """
    shifr_text = []
    key_len = len(key)

    #ASCII-код
    int_key = [ord(i) for i in key]
    int_text = [ord(i) for i in text]

    #растянуть ключ на длину текста (пока не нужно)
    #key_repeat = (key*(---))

    for i in range (len(int_text)):
        if text[i].isalpha():
            shift = int_key[i % key_len] % 32  # Учитываем только буквы
            if text[i].isupper():
                shifr_text.append(chr((int_text[i] + shift - 1040) % 32 + 1040))
            else:
                shifr_text.append(chr((int_text[i] + shift - 1072) % 32 + 1072))
        else:
            shifr_text.append(text[i])  # Не изменяем небуквенные символы

    return ''.join(shifr_text)

def main():
    args = parsing()
    text = args._text
    key = args._key

    # Шифруем текст
    shifr_text = shifr(text, key)
    print("Зашифрованный текст: ")
    print(shifr_text)

if __name__ == "__main__":
    main()

