import json

f = open('dictionary.json')

english_dictionary = json.load(f)




def word_lister(word_dict):
    word_list=  []
    for i in word_dict.keys():

        word_list.append(i)
    return word_list

english_list = word_lister(english_dictionary)

# print(english_list)

def word_matcher(scrabble_hand):
    for i in english_list:
        letter_list = []
        for letter in i:
            letter_list.append(letter)
        # print(word_list)
        if all(j in scrabble_hand for j in letter_list):
            print(i)


test1 = ['a', 'r', 'k', 'p', 'b', 'm', 'v']

word_matcher(test1)