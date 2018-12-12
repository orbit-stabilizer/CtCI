

# Time Complexity: O(n)
# Space Complexity: O(n)
def URLify(s: str) -> str:
    """
    Note:
        This is slightly different from the CtCI question.
    Returns:
        A string stripped of all leading and trailing spaces, with all
        non-leading and non-trailing spaces replaced with '%20'.
    """

    return '%20'.join(s.strip().split(' '))


class TestURLify():

    def test_empty_string(self) -> None:
        mt_str = ''

        assert URLify(mt_str) == ''

    def test_blank_string(self) -> None:
        blank_str = ' '

        assert URLify(blank_str) == ''

    def test_regular_string(self) -> None:
        s = 'Dr John Wayne'
        s_urlified = 'Dr%20John%20Wayne'

        assert URLify(s) == s_urlified

    def test_leading_trailing_spaces(self) -> None:
        s = '    This Is Great   '
        s_urlified = 'This%20Is%20Great'

        assert URLify(s) == s_urlified

    def test_multiple_non_trailing_spaces(self) -> None:
        s = 'This   Is    Great'
        s_urlified = 'This%20%20%20Is%20%20%20%20Great'

        assert URLify(s) == s_urlified
