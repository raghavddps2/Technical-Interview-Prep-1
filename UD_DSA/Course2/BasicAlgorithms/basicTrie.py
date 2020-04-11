basic_trie = {
    # a and add word.
    'a':{
        'd':{
            'd':{
                'word_end':True
            },
            'word_end':False
        },
        'word_end':True
    },

    'h':{
        'i':{
            'word_end':True
        },
        'word_end':False
    }
}

def is_word(word):

    current_node = basic_trie
    for char in word:
        if char not in current_node:
            return False
        current_node = current_node[char]
    return current_node['word_end']

print("Is 'a' a word {}? ".format(basic_trie['a']['word_end']))
print("Is 'add' a word {}?".format(basic_trie['a']['d']['d']['word_end']))
print("Is ad a word {}?".format(basic_trie['a']['d']['word_end']))

test_words = ['ap', 'add']
for word in test_words:
    if is_word(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))