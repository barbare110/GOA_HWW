def positive_or_negative(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

result = positive_or_negative(-2)
print(result)

result = positive_or_negative(5)
print(result)

result = positive_or_negative(0)
print(result)