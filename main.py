numbers_sequence = [12, 345, 2, 6, 7896, 2, 10, 15, 25, 234]
even_numbers = len([number for index, number in enumerate(numbers_sequence) if len(str(number)) % 2 == 0])
