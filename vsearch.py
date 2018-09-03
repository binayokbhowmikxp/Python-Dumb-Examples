def search4vowels(word):
    """Return any vowel found in a supplied word""" 
    vowels = set('aeiou')
    #found = vowels.intersection(set(word))
    """ for vowel in found:
        print(vowel)"""
    #return bool(found)
    return vowels.intersection(set(word))
