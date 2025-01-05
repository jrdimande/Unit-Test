def sort_n(numbers):
    for i  in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                aux = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = aux

    return numbers