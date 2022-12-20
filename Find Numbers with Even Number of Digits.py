def find_numbers_with_even_number_of_digits(sequence: list[int]) -> int:
    return len([number for index, number in enumerate(sequence) if len(str(number)) % 2 == 0])


