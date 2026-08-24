# Symone Mitchell
# August 23, 2026
# Problem 3: Multiply all numbers in a list

def multiplyList(numbers):
    result = 1

    for number in numbers:
        result = result * number

    return result

numbers = [5, 2, 7, -1]

answer = multiplyList(numbers)

print(answer)
