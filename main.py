"""
Take the following test in the language you prefer:

Given a dictionary/word map, which can be of any length, and taking an input word find all the sections (sub strings) that are contained in the dictionary.

Example, Dictionary : a, aa, aaa (is a list of keywords)
Input word : aaabaa (is a string of any length with no spaces)

The output should be: a, a, a, aa, aa, aaa, a, a, aa.
"""


def check_sub_strings(keywords, word):
    result = []

    # idx is used to know in which position of the word I am  
    idx = 0

    # last_break is a dictionary in which it will contain the keys of our list with a value of 0, to register our breaks
    last_breaks = {}
    for k in keywords:
        last_breaks[k] = 0

    # KwIndx is used to know what keyword is being searched for
    kwIdx = 0

    while True:
        while True:
            keyword = keywords[kwIdx]

            # The search is resumed from the last break
            idx = last_breaks[keyword]
            sub_string = word[idx : idx + len(keyword)]

            # We save the starting point for the next search
            last_breaks[keyword] = idx + 1

            # If it is not a match, the search stops
            if keyword not in sub_string:
                break

            # The result is saved and the search is advanced
            result.append(keyword)
            idx += 1

        kwIdx += 1

        if kwIdx == len(keywords):
            kwIdx = 0

        # A list is created to verify that the keywords were verified in the whole word
        allDone = []
        for last_break in last_breaks.values():
            allDone.append(last_break >= len(word))

        if all(allDone):
            break

    return result


if __name__ == "__main__":
    keywords = ["a", "aa", "aaa"]
    word = "aaabaa"

    result = check_sub_strings(keywords, word)
    print(f"{result=}")
