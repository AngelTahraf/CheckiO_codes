#You should return a given string in reverse order.
#Input: A string.
#Output: A string.
#Example:
#assert backward_string("val") == "lav"
#assert backward_string("") == ""
#assert backward_string("ohho") == "ohho"
#assert backward_string("123456789") == "987654321"

def backward_string(val: str) -> str:
    back_text = val[::-1]
    return back_text


print("Example:")
print(backward_string("erromotor"))

assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")
