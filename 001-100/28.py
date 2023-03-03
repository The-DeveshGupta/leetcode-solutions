class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_pointer = 0
        n_pointer = 0
        while h_pointer != len(haystack) and n_pointer != len(needle):
            if haystack[h_pointer] == needle[n_pointer]:
                h_pointer += 1
                n_pointer += 1
            else:
                h_pointer = h_pointer - n_pointer + 1
                n_pointer = 0
        else:
            if n_pointer == len(needle):
                return h_pointer - n_pointer
            else:
                return -1
