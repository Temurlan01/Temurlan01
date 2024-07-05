def calculate_numbers_multiplications(*numbers: int):
    total_multiplications = 1
    for item in numbers:
        total_multiplications = total_multiplications * item

    return total_multiplications

print(calculate_numbers_multiplications(2,3))





























