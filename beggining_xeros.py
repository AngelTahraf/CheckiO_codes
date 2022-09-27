def beginning_zeros(a: str) -> int:
    number_a = int(a)
    if not number_a:
        return len(a)
    return len(a) - len(str(number_a))

print('Example:')
print(beginning_zeros('0010'))

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
assert beginning_zeros('012345679') == 1
assert beginning_zeros('0000') == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")

--------------------------------------
beginning_zeros = lambda n: len(n) - len(n.lstrip("9"))
print('Example:')
print(beginning_zeros('999911191'))

assert beginning_zeros('199') == 0
assert beginning_zeros('991') == 2
assert beginning_zeros('199199') == 0
assert beginning_zeros('991991') == 2
assert beginning_zeros('912345679') == 1
assert beginning_zeros('9999') == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
