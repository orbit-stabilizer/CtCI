import pytest

# Time Complexity: O(n)
# Space Complexity: O(n)
def is_unique_a(string: str) -> bool:
    """
    Assumptions:
        Case matters, ie. 'A' and 'a' are different characters.
        Whitespace matters, ie. 'A  ' and 'A ' are different.
    Returns:
        True if given string contains all unique characters, else False.
    """
    chars:dict = dict()

    for char in string:
        if char in chars:
            return False
        else:
            chars[char] = 1
    
    return True


class TestIsUniqueA():
    
    def test_empty_string(self) -> None:
        mt_str = ''

        assert is_unique_a(mt_str) is True

    def test_blank_space_string(self) -> None:
        blank_str = ' '

        assert is_unique_a(blank_str) is True

    def test_two_blank_spaces_string(self) -> None:
        two_blanks_str = '  '

        assert is_unique_a(two_blanks_str) is False

    def test_unique_string(self) -> None:
        string = 'False'

        assert is_unique_a(string) is True

    def test_not_unique_string(self) -> None:
        string = 'Falsee'

        assert is_unique_a(string) is False


# Time Complexity: O(n*log(n)) due to sorted function
# Space Complexity: O(n) due to creating new string
# Some may argue that we are using an additional data structure since sorted
# returns a list
# To those people, I'd say have fun with your O(n^2) algorithm
def is_unique_b(string: str) -> bool:
    """
    Returns True if given string contains all unique characters, else False.
    We assume that case matters, ie. 'A' and 'a' are different characters.
    """

    sorted_string = ''.join(sorted(string))

    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    
    return True

class TestIsUniqueB():
    def test_empty_string(self) -> None:
        mt_str = ''

        assert is_unique_b(mt_str) is True

    def test_blank_space_string(self) -> None:
        blank_str = ' '

        assert is_unique_b(blank_str) is True

    def test_two_blank_spaces_string(self) -> None:
        two_blanks_str = '  '

        assert is_unique_b(two_blanks_str) is False

    def test_unique_string(self) -> None:
        string = 'False'

        assert is_unique_b(string) is True

    def test_not_unique_string(self) -> None:
        string = 'Falsee'

        assert is_unique_b(string) is False