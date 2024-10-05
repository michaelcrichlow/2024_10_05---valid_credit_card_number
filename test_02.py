def valid_credit_card_number(s: str) -> bool:
    # A valid credit card number has 16 digits.
    if "-" in s:
        if len(s) != 19:
            return False
    if "-" not in s:
        if len(s) != 16:
            return False

    # It must start with 4, 5 or 6.
    if s[0] != "4" and s[0] != "5" and s[0] != "6":
        return False

    # It should not contain any characters other than digits.
    test = "0123456789-"
    for val in s:
        if val not in test:
            return False

    # remove hyphens
    test_string = s.replace("-", "")

    # check for 4 or more repeated characters
    local_array = ["0000", "1111", "2222", "3333",
                   "4444", "5555", "6666", "7777",
                   "8888", "9999"]

    for val in local_array:
        if val in test_string:
            return False

    return True


def main() -> None:
    print(valid_credit_card_number('4532-3498-2347-1234'))
    print(valid_credit_card_number('4532-3433-3347-1234'))
    print(valid_credit_card_number('4532349823471234'))
    print(valid_credit_card_number('4532349877777123'))


if __name__ == '__main__':
    main()
