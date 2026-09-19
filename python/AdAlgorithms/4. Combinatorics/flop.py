def count_even(values: list[int]) -> int:
    count: int = 0

    for value in values:
        if value % 2 == 0:
            count += 1

    return count

print(count_even([]))
print(count_even([1, 3, 5]))
print(count_even([0, 2, 4]))

