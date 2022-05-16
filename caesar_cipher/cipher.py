from caesar_cipher.corpus_loader import word_list, name_list
import re

word_list = word_list.lower()
name_list = name_list.lower()

def encrypt(text, shift):
    l_text = text.lower()
    a_to_z = 'abcdefghijklmnopqrstuvwxyz'
    shift_a_to_z = a_to_z[shift:] + a_to_z[:shift]
    shifted_text = l_text.translate(str.maketrans(a_to_z, shift_a_to_z))
    return shifted_text


def decrypt(text, shift):
    decrypted_message = encrypt(text, -shift)
    return decrypted_message


def crack(text):
    a_to_z = 'abcdefghijklmnopqrstuvwxyz'
    content = 0
    shift = 0

    for char in a_to_z:
        shift += 1
        decrypted_message = decrypt(text, shift)
        message_list = decrypted_message.split(' ')
        confirmed = 0
        for element in message_list:
            item = re.sub(r'[^a-z]+','', element)
            if item in word_list or item in name_list:
                confirmed += 1
        list_length = len(message_list)
        content = int(confirmed // list_length)
        if content >= .5:
            return decrypted_message
        else:
            return None
