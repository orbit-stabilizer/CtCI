import pytest

# Time Complexity: O(n)
# Space Complexity: O(n)
def check_permutation(s1: str, s2:str) -> bool:
    """
    Assumptions:
        Case matters, ie. 'A' is different from 'a'.
        Whitespace matters, ie. 'A  ' and 'A ' are different.
    Returns:
        True if s2 is a permutation of s1, else False.
    """
    if len(s1) != len(s2):
        return False

    # KEY INSIGHT: surjective => bijective when |s1| = |s2|
    chars: dict = dict()

    # create dictionary of chars in s1
    for char in s1:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    # check if all chars in s2 are in the dictionary
    for char in s2:
        if char in chars:
            chars[char] -= 1
            if chars[char] < 0: 
                return False
        else:
            return False

    return True

class TestCheckPermutation():

    def test_empty_strings(self) -> None:
        mt_str_1 = ''
        mt_str_2 = ''

        assert check_permutation(mt_str_1, mt_str_2) is True
    
    def test_blank_strings(self) -> None:
        blank_str_1 = ' '
        blank_str_2 = ' '

        assert check_permutation(blank_str_1, blank_str_2) is True
    
    def test_different_strings(self) -> None:
        str_1 = 'This is a random string.'
        str_2 = 'This is another random string.'

        assert check_permutation(str_1, str_2) is False
    
    def test_caps(self) -> None:
        str_1 = 'With caps?'
        str_2 = 'with caps?'

        assert check_permutation(str_1, str_2) is False
    
    def test_permutation(self) -> None:
        str_1 = '!2#4%6&8(0asdf;lkj'
        str_2 = ';lkjfdas0(8&6%4#2!'

        assert check_permutation(str_1, str_2) is True
