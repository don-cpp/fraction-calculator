import operator
from fractions import Fraction

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}


def convert_to_improper(integer, fraction):
    numerator, denominator = get_numerator_and_denominator(fraction)
    new_numerator = (int(denominator) * int(integer)) + int(numerator)
    return '{}/{}'.format(str(new_numerator), str(denominator))


def get_operands(character):
    mixed_number_first_operand = ''
    improper_fraction_first_operand = ''
    for i in character:
        if i == '_':
            break
        mixed_number_first_operand += i
    for j in reversed(character):
        if j == '_':
            break
        improper_fraction_first_operand += j
    improper_fraction_first_operand = improper_fraction_first_operand[::-1]
    return convert_to_improper(mixed_number_first_operand, improper_fraction_first_operand)


def calculate(operation: str):
    split_operation = operation.split()
    first_operand = split_operation[0]
    given_operator = split_operation[1]
    second_operand = split_operation[2]
    if '_' in first_operand and '_' in second_operand:
        first_improper_operand = get_operands(first_operand)
        second_improper_operand = get_operands(second_operand)
        final_result = operators[given_operator](float(eval(first_improper_operand)),float(eval(second_improper_operand)))
        return format_result(str(Fraction(final_result).limit_denominator()))

    elif '_' in first_operand and '_' not in second_operand:
        first_improper_operand = get_operands(first_operand)
        final_result = operators[given_operator](float(eval(first_improper_operand)),
                                                 float(eval(second_operand)))
        return format_result(str(Fraction(final_result).limit_denominator()))

    elif '_' in second_operand and '_' not in first_operand:
        second_improper_operand = get_operands(second_operand)
        final_result = operators[given_operator](float(eval(first_operand)),
                                                 float(eval(second_improper_operand)))
        return format_result(str(Fraction(final_result).limit_denominator()))


def get_numerator_and_denominator(given_string):
    numerator = ''
    denominator = ''
    for i in given_string:
        if i == '/':
            break
        numerator += i
    for j in reversed(given_string):
        if j == '/':
            break
        denominator += j
        denominator = denominator[::-1]
    return numerator, denominator


def format_result(result):
    numerator, denominator = (get_numerator_and_denominator(result))
    if int(numerator) > int(denominator):
        a = int(numerator) // int(denominator)
        b = int(numerator) % int(denominator)
        return '{}_{}/{}'.format(str(a), str(b), str(denominator))
    return '{}/{}'.format(str(numerator), str(denominator))


if __name__ == '__main__':
    print(calculate('1/2 * 3_3/4'))
    print(calculate('2_3/8 + 9/8'))
