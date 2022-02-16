# Write a code that checks if two given strings are anagrams

TRUE = "Yes"
FALSE = "No"

def get_character_frequency(word):
    mp  = {}
    for ch in word:
        mp[ch] = mp.get(ch, 0) + 1
    return mp


def anagram_check(word_one, word_two):
    word_one_character_frequency = get_character_frequency(word_one)
    word_two_character_frequency = get_character_frequency(word_two)
    for ch, frequency in word_one_character_frequency.items():
        if not word_two_character_frequency.get(ch) == frequency:
            return FALSE
    return TRUE 
    
    

assert anagram_check('mary', 'army') == TRUE 

assert anagram_check('maryi', 'army') == FALSE

assert anagram_check('arya', 'army') == FALSE

assert anagram_check('ijk', 'iijk') == FALSE

assert anagram_check('', '') == TRUE 

assert anagram_check('a', '') == FALSE
