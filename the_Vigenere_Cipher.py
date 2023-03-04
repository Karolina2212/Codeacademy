'''
Example:
              message:    b  a  r  r  y    i  s    t  h  e    s  p  y
       keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d
resulting place value:    24 12 11 14 10   2  15   5  1  1    4  9  21
             solution:      ymlok cp fbb ejv

Message to decode:

message:    txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!
keyword:    friends
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decoding_poly(sentence, key_word):
    offset_values = []
    mark_count = 0
    for index, letter in enumerate(list(sentence)):
        if letter not in alphabet:
            offset_values.append(letter)
            mark_count += 1
        else:
            # to decode/encode message from example change "+" to "-"
            value = alphabet.index(letter) + alphabet.index(key_word[(index - mark_count) % len(list(key_word))])
            offset_values.append(value % len(alphabet))

    decoded_list = []
    for index, letter in enumerate(list(sentence)):
        if letter not in alphabet:
            decoded_list.append(letter)
        else:
            decoded_list.append(alphabet[offset_values[index] % len(alphabet)])

    return "".join(decoded_list)


# message from example (first change mark in the code):
# print(decoding_poly('barry is the spy','dog'))

print(decoding_poly('txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!',
                    'friends'))
