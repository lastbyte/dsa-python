'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to
C's strstr() and Java's indexOf().
'''


def strStr(haystack: str, needle: str) -> int:
    haystack_length = len(haystack)
    needle_length = len(needle)

    if needle_length == 0:
        return 0

    elif haystack_length >= needle_length:
        haystack_index = 0
        needle_index = 0

        while haystack_index < haystack_length - needle_length + 1:
            needle_index = 0
            while needle_index < needle_length:
                if haystack[haystack_index +
                            needle_index] != needle[needle_index]:
                    break

                needle_index += 1

            if needle_index == needle_length:
                return haystack_index

            haystack_index = haystack_index + 1
        return -1

    else:
        return -1


if __name__ == "__main__":
    print(strStr("hello", "ll"))
    print(strStr("aaaaa", "bba"))
    print(strStr("a", "a"))
    print(strStr("", "a"))
    print(strStr("", ""))
    print(strStr("abc", "c"))
    print(strStr("mississippi", "issipi"))
