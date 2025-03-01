task_text = "КwЧ5Д>ЫХЧ1ЪЕt Й2>ХИЬЧЙ ФХ 1 ХБЧБХЫПЫХЪ- ЕЩЕФЙХБЕ2НЫИИ ХЕЯЩЕ1ФУЙХДЫХЙЕ17БЕХ8ЛЛЫБЙ ЩДЕХМА́ЧД Й7ХБЕДЛ wЫД4 Ч17Д>ЫХwЧДД>ЫХДЕХ ХДЧrt 2ЫХЯДЧ5 ЙЫ17ДЕХК2ЫД70 Й7Х+ЧЯ2ЫХЕЪtЧ22>ХБЕЙЕtКУХЯЧХЕw ДХrt Ы2Х2ЕЬДЕХЯЧЪКЯ Й7ХЩХ Ч2ФЙ7Х Х ИГЕ1Д Й7ХИКПЫИЙЩКЫЙХДЫХ2ЫД7ОЫХwУЬ Д>ХА́ЧЯ1 5Д>МХК ЧБЕЩП БЕЩХ ИЕ1Д 2>МХЛЧА1ЕЩХДЫБЕЙЕt>ЫХ ЯХД МХИЕwЫЬЧЙХЫЧ1 ЯЧ4 ХЧ1ЪЕ Й2ЕЩХО ЛЕЩЧД ФХИХ4Ы17УХКИ1ЕЬД Й7ХЬ ЯД7Х ЕЙЫД4 Ч17Д>2ХМЧБЫЧ2ХДЕХД ХЩХЕwДЕАХ ЯХД МХЧ1ЪЕt Й2ХО ЛЕЩЧД ФХД БЧБХДЫХИЩФЯЧДХИХЧ1ЪЕ Й2E2ХИЬЧЙ ФХЕД ХЫЧ1 ЯЕЩЧД>ХБЧБХЕЙwЫ17Д>ЫХЧ1ЪЕt Й2>Х ХИГЕ17ЯКУЙИФХЧЯwЫ17ДЕ"

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

    #Вывод процентного соотношения
    percent_array = calculate_char_percentages(task_text)
    print(percent_array)

    #Сортировка ключей
    print("\n\n\n")
    sorted_dict = dict(sorted(percent_array.items()))
    print(sorted_dict)

    # Вывод результата
    print("\n\n\n")
    print("Измененный текст:")
    print(original_text)

if __name__ == "__main__":
    main()