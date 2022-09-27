def end_zeros(a: int) -> int:
    text =  str(a)
    text_lenght = len(text)
    text_withoutzeros = text.strip("0")
    text_lenght_withoutzeros = len(text_withoutzeros)
    return text_lenght - text_lenght_withoutzeros

print('Example:')
print(end_zeros(1001000))

assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
