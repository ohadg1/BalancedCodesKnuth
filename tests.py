import random
from knuth import *

random.seed(42)


def test_count_chars():
    """
    test for function count_chars
    """
    res = True
    string = "1111112222"
    count = count_chars(string, 3)
    res = res and (count == [0, 6, 4])

    string = "11001122223"
    count = count_chars(string, 4)
    res = res and (count == [2, 4, 4, 1])

    string = "10200400103"
    count = count_chars(string, 5)
    res = res and (count == [6, 2, 1, 1, 1])

    return res


def test_count_sigma():
    """
    test for function count_sigma
    """
    res = True
    string = "1111112222"
    count = count_sigma(string, "1")
    res = res and (count == 6)

    count = count_sigma(string, "3")
    res = res and (count == 0)

    count = count_sigma(string, "2")
    res = res and (count == 4)

    return res


def test_number_to_base():
    """
    test for function number_to_base
    """
    x = 17
    res = (number_to_base(x, 2, 7) == "0010001")
    res = res and (number_to_base(x, 3, 7) == "0000122")
    res = res and (number_to_base(x, 4, 7) == "0000101")
    res = res and (number_to_base(x, 5, 7) == "0000032")
    res = res and (number_to_base(0, 5, 7) == "0000000")

    return res


def test_encode_knuth():
    """
    test for function encode_knuth
    """
    res = (encode_knuth("002202011",3) == 102202011000111122220)

    return True


def test_calculate_output_length():
    """
    test for function calculate_output_length
    """
    res = (len(encode_knuth("002202011", 3)) == calculate_output_length(9, 3))
    res = res and (len(encode_knuth("002202011000222120110110100101020201020111001", 3)) == calculate_output_length(45, 3))

    return res


def test_calc_indexes():
    """
    test for function calc_indexes
    """
    res = (calc_indexes(2, 326) == [326, 20])
    res = res and (calc_indexes(2, 16) == [16])
    return res


def test_split_string():
    """
    test for function split_string
    """
    res = (split_string("0010001101010111110110001010000101110111111100000001000000001011111111", 2, 16) ==
           ['0010001101010111', '110110001010000101110111111100000001000000001011111111'])
    return res


def test_sub_decode():
    """
    test for function sub_encode
    """
    res = (sub_decode("102202011", "000100", 3) == "002202011")
    return res


def test_decode_knuth():
    """
    test for function decode_knuth
    """
    res = (decode_knuth(encode_knuth("001000110", 3), 3, 9) == "001000110")

    res = res and (decode_knuth(encode_knuth("0123402014", 5), 5, 10) == "0123402014")

    res = res and (decode_knuth(encode_knuth("021000110", 3), 3, 9) == "021000110")

    res = res and (decode_knuth(encode_knuth("010101111010101110101011010000101110010000000000000000000000000000101010", 2), 2, 72) == "010101111010101110101011010000101110010000000000000000000000000000101010")

    res = res and (decode_knuth(encode_knuth("012012012012021121201201200010101010222", 3), 3, 39) == "012012012012021121201201200010101010222")

    return res


def test_stress():
    """
    checks that encoding and decoding work well on random vectors, and that the output is balanced
    """
    for i in range(1000):
        num = random.randint(0, 2 ** 1000 - 1)
        for base in [2, 3, 4, 5, 6, 7, 8, 9, 10]:  # , 3, 4, 5, 8
            length = math.ceil(math.log(num+base, base))
            length += (base - (length % base))
            assert length % base == 0

            vec = number_to_base(num, base, length)
            count_c = count_chars(encode_knuth(vec, base), base)
            if max(count_c) != min(count_c):
                print(f"vec {vec} \n enc {encode_knuth(vec, base)} \n count {count_c}")
                return False
            if decode_knuth(encode_knuth(vec, base), base, length) != vec:
                print(f"error: {vec} not encoded/decoded correctly for base {base}, length {length}")
                return False

    return True


if __name__ == "__main__":
    print("Testing\n")
    print(f"test_count_chars {test_count_chars()}")
    print(f"test_count_sigma {test_count_sigma()}")
    print(f"test_number_to_base {test_number_to_base()}")

    print(f"test_calc_indexes {test_calc_indexes()}")
    print(f"test_split_string {test_split_string()}")
    print(f"test_sub_decode {test_sub_decode()}")
    print(f"test_calculate_output_length {test_calculate_output_length()}")

    print(f"test_encode_knuth {test_encode_knuth()}")
    print(f"test_decode_knuth {test_decode_knuth()}")

    print(f"test_stress {test_stress()}")
    print("\nDONE!")
