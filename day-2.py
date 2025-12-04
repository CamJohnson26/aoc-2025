inputs = []
with open('inputs/day-2-a.txt', 'r') as f:
    line = f.read()
    inputs = [prod_id.split('-') for prod_id in line.split(',')]

def leading_zeros_for_n(n):
    return (10**n) // 10

def count_invalid_ids_for_digits(n):
    if n % 2 == 1:
        return 0
    prefix_length = n // 2
    total_possible = 10**prefix_length
    return total_possible - leading_zeros_for_n(n//2)

def get_invalid_ids_for_digits(n):
    invalids = []
    if n % 2 == 1:
        return []
    prefix_length = n // 2
    upper_bound = int('9' * prefix_length)
    lower_bound = int('1'+'0'*(prefix_length - 1))
    for i in range(lower_bound, upper_bound + 1):
        invalids.append(str(i) + str(i))
    return invalids

def count_invalid_ids(start_id, end_id):
    max_len = len(end_id)
    min_len = len(start_id)

    if max_len == min_len:
        if max_len % 2 == 1:
            return 0
        else:
            half_len = max_len // 2
            start_half = int(start_id[:half_len])
            end_half = int(end_id[:half_len])

            difference = end_half - start_half - 1 # exclude the ends
            start_candidate = int(str(start_half)+str(start_half))
            end_candidate = int(str(end_half)+str(end_half))

            start_modifier = 1 if start_candidate >= int(start_id) else 0
            end_modifier = 1 if end_candidate <= int(end_id) else 0

            return difference + start_modifier + end_modifier
    else:
        range_possibilities = 0
        for i in range(min_len + 1, max_len - 1):
            if i % 2 == 1:
                continue
            range_possibilities += count_invalid_ids_for_digits(i)

        start_modifier = 0
        if (len(start_id) % 2) == 0:
            half_len = len(start_id) // 2
            start_half = int(start_id[:half_len])
            start_candidate = int(str(start_half) + str(start_half))
            start_modifier = 1 if start_candidate >= int(start_id) else 0
            start_upper_bound = int('9'*half_len)
            start_modifier += start_upper_bound - start_half

        end_modifier = 0
        if (len(end_id) % 2) == 0:
            half_len = len(end_id) // 2
            end_half = int(end_id[:half_len])
            end_candidate = int(str(end_half) + str(end_half))
            end_modifier = 1 if end_candidate <= int(end_id) else 0

            end_lower_bound = int('1' + '0'*(half_len - 1))
            end_modifier += end_half - end_lower_bound

        return range_possibilities + start_modifier + end_modifier

def get_invalid_ids(start_id, end_id):
    invalids = []
    max_len = len(end_id)
    min_len = len(start_id)

    if max_len == min_len:
        if max_len % 2 == 1:
            return []
        else:
            half_len = max_len // 2
            start_half = int(start_id[:half_len])
            end_half = int(end_id[:half_len])

            for i in range(start_half + 1, end_half):
                invalids.append(str(i)+str(i))

            start_candidate = int(str(start_half)+str(start_half))
            end_candidate = int(str(end_half)+str(end_half))

            start_modifier = 1 if start_candidate >= int(start_id) and start_candidate < int(end_id) else 0
            end_modifier = 1 if end_candidate <= int(end_id) else 0

            if start_modifier:
                invalids.append(str(start_candidate))

            if end_modifier and end_candidate != start_candidate:
                invalids.append(str(end_candidate))
            return sorted(invalids)
    else:
        range_possibilities = 0
        for i in range(min_len + 1, max_len - 1):
            if i % 2 == 1:
                continue
            range_possibilities += count_invalid_ids_for_digits(i)
            invalids.extend(get_invalid_ids_for_digits(i))

        if (len(start_id) % 2) == 0:
            half_len = len(start_id) // 2
            start_half = int(start_id[:half_len])
            start_upper_bound = int('9'*half_len)
            for i in range(start_half, start_upper_bound + 1):
                candidate = str(i) + str(i)
                if int(candidate) >= int(start_id):
                    invalids.append(candidate)

        if (len(end_id) % 2) == 0:
            half_len = len(end_id) // 2
            end_half = int(end_id[:half_len])
            end_candidate = int(str(end_half) + str(end_half))
            end_modifier = 1 if end_candidate <= int(end_id) else 0

            end_lower_bound = int('1' + '0'*(half_len - 1))
            end_modifier += end_half - end_lower_bound
            for i in range(end_lower_bound, end_half + 1):
                candidate = str(i) + str(i)
                if int(candidate) <= int(end_id):
                    invalids.append(candidate)

        return sorted(invalids)

"""
Test Cases:
11-22237445

7777-9999

Same length inputs:
if odd, no matches
if even:
Cut both in half. take the difference for how many prefixes there are (minus 1)
Subtract 1 to exclude the ends
for the ends, if the start half duplicated is greater than the start, or
if the end half duplicated is less than the end, add 1 for each
Total possibilities is difference + start + end

If arbitrary:
Get the difference, exclude start and end
Make a range excluding odds
For each element in the range, add all possible invalid
For start and end one possible possibility (half twice.) Check if in range

But also have all the possibilities counting up to 999.. or down to 10...
So take the half and for start [9]*n - [start_half]*2 - 1
For end 1 & [0]*(n-1) - [end_half]*2 - 1
The minus 1 excludes the ends

Calculate all possible invalid:
Take n/2. That's the number of possible, but need to exclude leading zeros.

Calculate leading zeros for n:
10**n / 10

"""

def tests():
    assert get_invalid_ids_for_digits(2) == ['11', '22', '33', '44', '55', '66', '77', '88', '99']
    assert get_invalid_ids('1', '1010') == ['1010', '11', '22', '33', '44', '55', '66', '77', '88', '99']
    assert get_invalid_ids('11', '22') == ['11', '22']
    assert get_invalid_ids('95', '99') == ['99']
    assert get_invalid_ids('95', '115') == ['99']
    assert get_invalid_ids('77', '99') == ['77', '88', '99']
    # assert get_invalid_ids('95', '115') == ['99']
    assert count_invalid_ids('22', '1111') == 10
    assert count_invalid_ids('95', '115') == 1
    assert count_invalid_ids('11', '22') == 2
    assert count_invalid_ids('77', '99') == 3
    assert count_invalid_ids('78', '99') == 2
    assert count_invalid_ids('78', '98') == 1
    assert count_invalid_ids('78', '79') == 0
    assert count_invalid_ids('777', '999') == 0
    assert count_invalid_ids('7777', '9999') == 23
    assert count_invalid_ids('7777', '9998') == 22
    assert count_invalid_ids('7778', '9999') == 22
    assert count_invalid_ids('7778', '9998') == 21
    assert count_invalid_ids_for_digits(4) == 90
    assert count_invalid_ids_for_digits(3) == 0
    assert count_invalid_ids_for_digits(8) == 9000
    assert count_invalid_ids('1', '1010') == 10
    assert count_invalid_ids('1', '1111') == 11
    assert count_invalid_ids('1698522', '1698528') == 0

# tests()

sum = 0
for [start_id, end_id] in inputs:
    new_invalids = get_invalid_ids(start_id, end_id)
    count = count_invalid_ids(start_id, end_id)

    for i in new_invalids:
        print(i, start_id, end_id)
        sum += int(i)
print(sum)