def search4vowels(phrase: str) -> set:
    """Return any vowels found in the supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Returns a set of 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))
