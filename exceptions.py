class UsernameSoShort(Exception):
    def __str__(self):
        return """
|-------------- USERNAME ERROR ---------------|
|The length of the USERNAME should be longer 4|
|----------------- TRY AGAIN -----------------|
"""


class UsernameWhithOutWhiteSpace(Exception):
    def __str__(self):
        return """
|--------- USERNAME ERROR ---------|
|The USERNAME cannot contain spaces|
|----------- TRY AGAIN ------------|
"""


class PasswordSoShort(Exception):
    def __str__(self):
        return """
|-------------- PASSWORD ERROR ---------------|
|The length of the PASSWORD should be longer 8|
|----------------- TRY AGAIN -----------------|
"""

class PasswordFewDigits(Exception):
    def __str__(self):
        return """
|----------- PASSWORD ERROR -----------|
|The number of DIGITS must be greater 2|
|------------- TRY AGAIN --------------|
"""


class PasswordFewLetters(Exception):
    def __str__(self):
        return """
|------------ PASSWORD ERROR -----------|
|The number of LETTERS must be greater 2|
|-------------- TRY AGAIN --------------|
"""


class PasswordFewSymbol(Exception):
    def __str__(self):
        return """
|----------- PASSWORD ERROR -----------|
|The number of SYMBOL must be greater 1|
|------------- TRY AGAIN --------------|
"""

class There_is_username_already(Exception):
    def __str__(self):
        return """
|----------- PASSWORD ERROR -----------|
|  There_has_already_been_such_a_name  |
|------------- TRY AGAIN --------------|
"""


