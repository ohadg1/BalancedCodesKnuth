import math


def number_to_base(n, b, log):
    if n == 0:
        return "0" * log
    digits = ""
    while n:
        digits += (str(n % b))
        n //= b
    return "0" * (log - len(digits)) + digits[::-1]


def count_chars(string, alphabet_size):
    count = [0] * alphabet_size
    for c in string:
        count[int(c)] = count[int(c)] + 1
    return count


def count_sigma(string, sigma):
    return len([s for s in string if s == sigma])


def balance_string(string, alphabet_size):
    string = [int(c) for c in string]
    res = []
    for i in range(alphabet_size):
        res += ["".join([str((c + i) % alphabet_size) for c in string])]
    return "".join(res)


def encode_knuth(string, alphabet_size):
    if len(string) <= alphabet_size * math.ceil(math.log(len(string), alphabet_size)):
        return balance_string(string, alphabet_size)

    string = [int(c) for c in string]
    appearance_goal = len(string) // alphabet_size
    addition_string = []
    for sigma in range(alphabet_size - 1, -1, -1):
        sigma_count = count_sigma(string, sigma)

        for idx, char in enumerate(string):
            if sigma_count == appearance_goal:
                addition_string += number_to_base(idx, alphabet_size, math.ceil(math.log(len(string), alphabet_size)))
                break
            if char <= sigma:
                string[idx] = sigma - char
                if char == sigma:
                    sigma_count -= 1
                if char == 0:
                    sigma_count += 1
    string = [str(c) for c in string]
    return "".join(string) + encode_knuth("".join(addition_string), alphabet_size)


def calc_indexes(alphabet_size, orig_length):
    indexes = [orig_length]
    while indexes[-1] > alphabet_size * math.ceil(math.log(indexes[-1], alphabet_size)):
        indexes += [math.ceil(math.log(indexes[-1], alphabet_size)) * alphabet_size]

    return indexes


def split_string(string, alphabet_size, orig_length):
    indexes = calc_indexes(alphabet_size, orig_length)
    strings = []
    for ind in indexes:
        strings += [string[:ind]]
        string = string[ind:]
    return strings + [string]


def sub_decode(encoded_str, index_str, alphabet_size):
    index_str = index_str[:-(len(index_str) // alphabet_size)]
    encoded_list = [int(c) for c in encoded_str]
    for sigma in range(1, alphabet_size):
        index = int(index_str[-(len(index_str) // (alphabet_size - sigma)):],
                    base=alphabet_size)
        for i in range(index):
            if encoded_list[i] <= sigma:
                encoded_list[i] = sigma - encoded_list[i]
        index_str = index_str[:-(len(index_str) // (alphabet_size - sigma))]

    return "".join([str(c) for c in encoded_list])


def decode_knuth(string, alphabet_size, orig_length):
    strings = split_string(string, alphabet_size, orig_length)
    strings = strings[:-1] # = strings[-1][:(len(strings[-1]) // alphabet_size)]

    for i in range(len(strings) - 1, 0, -1):
        strings[i - 1] = sub_decode(strings[i - 1], strings[i], alphabet_size)

    return strings[0]
