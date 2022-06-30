numbers = [3, 5, -4 ,8, 11, 1, -1, 6]
target_sum = 10
sum_to_target = []


def two_number_sum(numbers, target):
    for number in numbers:
        num_to_target = target_sum - number
        if num_to_target in numbers and num_to_target != number:
            return [number, num_to_target]
        sum_to_target.append(number)
    return []


print(two_number_sum(numbers, target_sum))