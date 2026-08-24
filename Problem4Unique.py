# Symone Mitchell
# August 23, 2026
# Problem 4: Return a list of unique elements

def uniqueList(numbers):
    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique

numbers = [1, 3, 3, 3, 6, 2, 3, 5]

result = uniqueList(numbers)

print(result)
