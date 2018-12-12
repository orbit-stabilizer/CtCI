

# Time Complexity: O(n)
# Space Complexity: O(n)
def palindrome_permutation(string: str) -> bool:
    """
    Assumptions:
        Case matters, ie. 'A' is different from 'a'.
        Whitespace matters, ie. 'A  ' and 'A ' are not palindromes.
    Note:
        This is slightly different from the CtCI question.
    Returns:
        True if string is a permutation of a palindrome, False otherwise.
    """

    # KEY INSIGHT:
    #   string is a permutation of a palindrome
    #   <=>
    #   ∀c∈string, |c| % 2 = 0 ∨∃! c∈string s.t. |c| % 2 = 1

    chars: dict = dict()

    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    count_odds: int = 0

    for char in chars:
        if chars[char] % 2 != 0:
            count_odds += 1

    return count_odds <= 1


class TestPalindromePermutation():

    def test_empty_string(self) -> None:
        mt_str = ''

        assert palindrome_permutation(mt_str) is True

    def test_blank_string(self) -> None:
        blank_str = ' '

        assert palindrome_permutation(blank_str) is True

    def test_two_blank_spaces_string(self) -> None:
        two_blank_spaces_str = '  '

        assert palindrome_permutation(two_blank_spaces_str) is True

    def test_racecar(self) -> None:
        s = 'rraacce'

        assert palindrome_permutation(s) is True

    def test_not_palindrome(self) -> None:
        s = 'testing'

        assert palindrome_permutation(s) is False
