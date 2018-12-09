from typing import List
import pytest

# Time Complexity: O(n)
# Space Complexity: O(n)
def string_compression(s: str) -> str:
    """
    Assumptions:
        Case matters, ie. 'A' is different from 'a'.
        Input string s has only uppercase and lowercase letters (a-z).
    Returns:
        A compressed string, eg. 'aaabbbaae' -> 'a3b2a2e1', if compressed
        string is shorter than input string, else returns input string.
    """

    count: int = 1
    output: List[str] = []

    for i in range(len(s)):
        if i < len(s) - 1:
            if s[i] == s[i+1]:
                count += 1
            else:
                output.append(s[i])
                output.append(str(count))
                count = 1
        else:
            output.append(s[i])
            output.append(str(count))
    
    return ''.join(output) if len(output) < len(s) else s


class TestStringCompression():

    def test_compress_long_str(self) -> None:
        long_str = 'aaaaaaaabbbbbbbbiiiiiiiillllllllalskdjf'
        compressed_str = 'a8b8i8l8a1l1s1k1d1j1f1'

        assert string_compression(long_str) == compressed_str
    
    def test_return_original_str(self) -> None:
        orig_str = 'abcdefgh'

        assert string_compression(orig_str) == orig_str
    
    def test_uppercase_return_orignal_str(self) -> None:
        orig_str = 'ABCabcABCabc'

        assert string_compression(orig_str) == orig_str

    def test_uppercase_compress_long_str(self) -> None:
        long_str = 'PPPNNNMMMPPP'
        compressed_str = 'P3N3M3P3'

        assert string_compression(long_str) == compressed_str

    def test_mixed_upper_lower_compress_long_str(self) -> None:
        long_str = 'HHHHHHhhhhhhiou'
        compressed_str = 'H6h6i1o1u1'

        assert string_compression(long_str) == compressed_str