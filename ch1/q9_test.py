import pytest

# Time Complexity: O(n) - Depends on implementation of in
# Space Complexity: O(n) - Depends of implementation of in
def string_rotation(s1: str, s2: str) -> bool:
    """
    Assumptions:
        Both strings are non-empty.
        There are no spaces.
    Returns:
        True if s1 is a rotation of s2, else False
    """
    if len(s1) != len(s2):
        return False

    s1_modified: str = s1 + s1

    return s2 in s1_modified


class TestStringRotation():

    def test_is_rotation(self) -> None:
        s1 = 'rotation'
        s2 = 'tationro'

        assert string_rotation(s1, s2) is True
    
    def test_is_not_rotation(self) -> None:
        s1 = 'rotation'
        s2 = 'tationor'

        assert string_rotation(s1, s2) is False
    
    def test_is_rotation_2(self) -> None:
        s1 = 'lyhigh'
        s2 = 'highly'

        assert string_rotation(s1, s2) is True
    
    def test_is_not_rotation_2(self) -> None:
        s1 = 'noooooo'
        s2 = 'nooooo'

        assert string_rotation(s1, s2) is False
    
    def test_is_rotation_numbers(self) -> None:
        s1 = '1234567890'
        s2 = '4567890123'

        assert string_rotation(s1, s2) is True