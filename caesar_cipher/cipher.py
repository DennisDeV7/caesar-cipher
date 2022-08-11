
from .is_english_word import find_phrase


def encrypt(plain, shift):
    encrypted = ""
    for letter in plain:
        if letter.isupper() or letter.islower():
            num = ord(letter)
            shifted_num = (num + shift)
            if shifted_num > ord('z'):
                shifted_num -= 26
            return_to_chr = chr(shifted_num)
            encrypted += str(return_to_chr)
        else:
            encrypted += letter
    return encrypted


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)


def crack(cipher):
    for shift in range(1, 26):
        cipher_list = []
        potential_phrase = encrypt(cipher, shift)
        cipher_list.append(potential_phrase)
        phrase = find_phrase(cipher_list)
        if phrase:
            return phrase


if __name__ == "__main__":
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    cracked = crack(encrypted)
    print(cracked)

