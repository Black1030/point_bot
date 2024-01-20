from exceptions import (
    UsernameSoShort,
    UsernameWhithOutWhiteSpace,
    PasswordSoShort,
    PasswordFewDigits,
    PasswordFewLetters,
    PasswordFewSymbol,
    There_is_username_already
)
from constants import (
    MIN_LENGTH_USERNAME,
    MIN_LENGTH_PASSWORD,
    MIN_DIGITS_PASSWORD,
    MIN_LETTER_PASSWORD,
    MIN_SYMBOL_PASSWORD
)


def valid_user_register(username: str, password: str):
    if len(username) < MIN_LENGTH_USERNAME:
        return UsernameSoShort()
    if ' ' in username:
        return UsernameWhithOutWhiteSpace()

    if len(password) < MIN_LENGTH_PASSWORD:
        return PasswordSoShort()

    digits, letter, symbol = 0, 0, 0
    for let in password:
        if let.isalpha():
            letter += 1
        elif let.isdigit():
            digits += 1
        else:
            symbol += 1

    if digits < MIN_DIGITS_PASSWORD:
        return PasswordFewDigits()
    elif letter < MIN_LETTER_PASSWORD:
        return PasswordFewLetters()
    elif symbol < MIN_SYMBOL_PASSWORD:
        return PasswordFewSymbol()
