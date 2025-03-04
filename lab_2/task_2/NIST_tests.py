import math


#
def frequency_test(sequence):
    """
    Проверяет, что количество нулей и единиц в последовательности примерно одинаково
    :param sequence: Передаваемая последовательность (бит)
    :return: P-значение (если P->0 значит seq предсказуема, P->1 - seq случайна)
    """
    n = len(sequence)
    ones = sequence.count('1')
    zeros = sequence.count('0')
    sum = ones - zeros;
    S_n = abs(sum) / (n ** 0.5)
    p_value = math.erfc(S_n / (2 ** 0.5))
    return p_value


def runs_test(sequence):
    """
    Проверяет, что количество последовательностей одинаковых битов соответствует ожидаемому
    :param sequence: Передаваемая последовательность (бит)
    :return: P-значение
    """
    n = len(sequence)
    ones = sequence.count('1')
    zeros = sequence.count('0')

    prop = ones / n #Доля единиц в seq
    tau = 2 / (n ** 0.5)
    if abs(prop - 0.5) >= tau:
        return 0.0

    runs = 1 #Знакоперемены
    for i in range(1, n):
        if sequence[i] != sequence[i - 1]:
            runs += 1

    p_value = math.erfc(abs(runs - 2 * n * prop * (1 - prop)) /
                        (2 * (2 * n)** 0.5 * prop * (1 - prop)) )
    return p_value


