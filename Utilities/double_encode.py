import urllib.parse, codecs
""" 
10/20/2019
This script is to double encode URL components to bypass filtering.
"""
def char_single_encode(chars):
    encoded_str = ""

    for c in chars:
        if c in ['%', '<', '>', '.', '/']:
            encoded_str += '%' + str(codecs.encode(c.encode('UTF-8'), 'hex_codec')).split('b')[1].split('\'')[1].upper()
        else:
            encoded_str += c

    return encoded_str

def char_double_encode(chars):
    return char_single_encode(char_single_encode(chars))
