task_text = ("КwЧ5Д>ЫХЧ1ЪЕt Й2>ХИЬЧЙ ФХ 1 ХБЧБХЫПЫХЪ-"
             "ЕЩЕtФЙХБЕ2rtЫИИ ХrЕЯЩЕ1ФУЙХДЫХЙЕ17БЕХ8ЛЛЫБЙ" 
             "ЩДЕХМtЧД Й7ХБЕДЛ wЫД4 Ч17Д>ЫХwЧДД>ЫХДЕХ ХДЧrt" 
             "2ЫtХЯДЧ5 ЙЫ17ДЕХК2ЫД7О" 
             "Й7ХtЧЯ2ЫtХrtЕЪtЧ22>ХБЕЙЕtКУХЯЧХЕw ДХrt" 
             "Ы2Х2ЕЬДЕХЯЧЪtКЯ Й7ХЩХrЧ2ФЙ7Х Х ИrЕ1Д" 
             "Й7ХИКПЫИЙЩКЫЙХДЫХ2ЫД7ОЫХwУЬ Д>ХtЧЯ1" 
             "5Д>МХКrЧБЕЩП БЕЩХ ИrЕ1Д 2>МХЛЧА1ЕЩХДЫБЕЙЕt>ЫХ" 
             "ЯХД МХИЕwЫtЬЧЙХtЫЧ1 ЯЧ4 ХЧ1ЪЕt Й2ЕЩХО ЛtЕЩЧД" 
             "ФХИХ4Ы17УХКИ1ЕЬД Й7ХЬ ЯД7ХrЕЙЫД4" 
             "Ч17Д>2ХМЧБЫtЧ2ХДЕХД ХЩХЕwДЕАХ ЯХД МХЧ1ЪЕt Й2ХО" 
             "ЛtЕЩЧД ФХД БЧБХДЫХИЩФЯЧДХИХЧ1ЪЕt Й2Е2ХИЬЧЙ ФХЕД" 
             "ХtЫЧ1 ЯЕЩЧД>ХБЧБХЕЙwЫ17Д>ЫХЧ1ЪЕt Й2>Х Х" 
             "ИrЕ17ЯКУЙИФХtЧЯwЫ17ДЕ")

def replace_chars(text, target_char, replacement_char):
    """
    Заменяет все вхождения target_char на replacement_char в тексте.
    :param text: исходный текст
    :param target_char: символ, который нужно заменить
    :param replacement_char: символ, на который нужно заменить
    :return: текст с выполненными заменами
    """
    return text.replace(target_char, replacement_char)

def calculate_char_percentages(text):
    """
    Вычисляет процент встречаемости каждого символа в тексте.
    :param text: исходный текст
    :return: словарь, где ключ — символ, значение — процент его встречаемости
    """
    char_count = {}  # Словарь
    text_len = len(text)

    # Подсчет кол-ва символов в текстк
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Вычисление процентного соотношения
    char_percentages = {}
    for char, count in char_count.items():
        char_percentages[char] = (count / text_len) * 100

    return char_percentages



def main():
    original_text = ""
    print(task_text)


    #Вывод процентного соотношения
    percent_dict = calculate_char_percentages(task_text)
    #Сортировка ключей
    print("\n\n\n")
    sorted_dict = {}
    for key in sorted(percent_dict, key=percent_dict.get):
        sorted_dict[key] = percent_dict[key]
    print(sorted_dict)

    text = task_text
    print("______________________________________________________________\n\nПрототип 1:\n")
    text_p1 = replace_chars(task_text, "Х", "о")
    print(text_p1)

    print("_______________________________________________________________\n\nПрототип 2:\n")
    text_p2 = replace_chars(text_p1, "Е", "и")
    print(text_p2)


    print("_______________________________________________________________\n\nПрототип 3:\n")
    text_p3 = replace_chars(text_p2, "Д", "е")
    print(text_p3)

    print("_______________________________________________________________\n\nПрототип 4:\n")
    text_p4 = replace_chars(text_p3, "Ч", "а")
    print(text_p4)

    print("_______________________________________________________________\n\nПрототип 5:\n")
    text_p5 = replace_chars(text_p4, "Ы", "н")
    print(text_p5)

    # догадка слово ФQЁ Мое
    print("_______________________________________________________________\n\nПрототип 6:\n")
    text_p6 = replace_chars(text_p5, "Я", "м")
    print(text_p6)

    print("_______________________________________________________________\n\nПрототип 7:\n")
    text_p7 = replace_chars(text_p6, "Й", "т")
    print(text_p7)

    print("_______________________________________________________________\n\nПрототип 8:\n")
    text_p8 = replace_chars(text_p7, "t", "с")
    print(text_p8)

    print("_______________________________________________________________\n\nПрототип 9:\n")
    text_p9 = replace_chars(text_p8, "1", "в")
    print(text_p9)

    print("_______________________________________________________________\n\nПрототип 10:\n")
    text_p10 = replace_chars(text_p9, "2", "р")
    print(text_p10)

    print("_______________________________________________________________\n\nПрототип 11:\n")
    text_p11 = replace_chars(text_p10, "7", "м")
    print(text_p11)

    print("_______________________________________________________________\n\nПрототип 12:\n")
    text_p12 = replace_chars(text_p11, "Я", "л")
    print(text_p12)

    print("_______________________________________________________________\n\nПрототип 13:\n")
    text_p13 = replace_chars(text_p12, "Б", "д")
    print(text_p13)

    print("_______________________________________________________________\n\nПрототип 14:\n")
    text_p14 = replace_chars(text_p13, "И", "я")
    print(text_p14)






    # Вывод результата
    print("\n\n\n")
    print("Измененный текст:")
    print(original_text)

if __name__ == "__main__":
    main()