def count_even(values: list[int]) -> int:
    count: int = 0

    for value in values:
        if value % 2 == 0:
            count += 1
    return count