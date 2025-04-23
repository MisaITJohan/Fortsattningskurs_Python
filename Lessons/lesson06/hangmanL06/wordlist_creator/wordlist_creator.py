from random import sample
from WORDLIST import *
import pprint


def generate_wordlist(enumerated=False):
    current_list = []


    def _fetch_words(_enumerated):
        nonlocal current_list
        if _enumerated:
            current_list = enumerate(sorted(sample(WORDLIST, length)), start=1)
        else:
            current_list = sorted(sample(WORDLIST, length))


    def _build_wordlist():
        if isinstance(current_list[0], tuple):
            return f"{"\n".join(f"{": ".join([str(x), y])}" for x, y in current_list)}"
        else:
            return f"{"\n".join(current_list)}"


    while input(
            f"{
            f"\nCurrent wordlist: \n{_build_wordlist()}\n\n"
            f"Type 'quit' to save this list or press return to generate a new list: "
            if current_list
            else "Press return to generate a wordlist."
            }"
            ).casefold() != "quit".casefold():
        length = int(input("Type the desired length of the created list (leave blank "
                           "for a length of 1000): ") or 1000)
        _fetch_words(enumerated)

    else:
        with open("wordlist.txt", "w+") as file:
            for line in current_list:
                file.write(f"{line}\n")


if __name__ == '__main__':
    generate_wordlist()
