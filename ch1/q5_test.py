import pytest

# Time Complexity: O(n)
# Space Complexity: O(1)
def one_away(s1: str, s2: str) -> bool:
    """
    Assumptions:
        Case matters, ie. 'A' and 'a' are different characters.
        Whitespace matters, ie. 'A  ' and 'A ' are different.
    Returns:
        True if s1 is at most one edit away from s2, else False.
    """
    if abs(len(s1) - len(s2)) > 1:
        return False

    elif len(s1) == len(s2):
        diffs: int = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs += 1
                if diffs > 1:
                    return False
        return True

    elif len(s1) < len(s2):
        return one_away_helper(shorter_str=s1, longer_str=s2)
    
    else:
        return one_away_helper(shorter_str=s2, longer_str=s1)

def one_away_helper(shorter_str: str, longer_str: str) -> bool:
    """
    Helper function for one_away.
    """
    seen_diff: bool = False

    i: int = 0
    while i < len(shorter_str):
        j = i
        if seen_diff:
            j = i + 1

        if shorter_str[i] != longer_str[j]:
            if seen_diff:
                return False
            seen_diff = True
            continue
        
        i += 1
    
    return True


class TestOneAway():

    def test_empty_strs(self) -> None:
        s1 = ''
        s2 = ''

        assert one_away(s1, s2) is True

    def test_different_lengths_one_away(self) -> None:
        s1 = 'dinosaur'
        s2 = 'inosaur'

        assert one_away(s1, s2) is True
    
    def test_different_lengths_two_away(self) -> None:
        s1 = 'boxen'
        s2 = 'box'

        assert one_away(s1, s2) is False
    
    def test_same_lengths_one_away(self) -> None:
        s1 = 'length'
        s2 = 'lemgth'

        assert one_away(s1, s2) is True

    def test_same_lengths_two_away(self) -> None:
        s1 = 'asdfjkl;'
        s2 = 'asdfjk;l'

        assert one_away(s1, s2) is False
    