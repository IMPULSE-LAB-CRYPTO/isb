import math


#
def frequency_test(sequence):
    """
    Проверяет, что количество нулей и единиц в последовательности примерно одинаково.
    :param sequence: Передаваемая последовательность (бит)
    :return: P-значение (если P->0 значит seq предсказуема, P->1 - seq случайна)
    """
    n = len(sequence)
    ones = sequence.count('1')
    zeros = sequence.count('0')

    s = abs(ones - zeros) / (n ** 0.5)
    p_value = math.erfc(s / (2 ** 0.5))
    return p_value

