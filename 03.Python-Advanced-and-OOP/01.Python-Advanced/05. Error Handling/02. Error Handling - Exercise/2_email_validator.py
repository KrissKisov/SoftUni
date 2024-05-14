class MustContainAtSymbolError(Exception):
    pass


class TooManyAtSymbolsError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MINIMUM_LENGTH_NAME = 4
MAXIMUM_LENGTH_NAME = 64
VALID_DOMAINS = {".com", ".bg", ".org", ".net"}  # used set as can be extended in future with unique domains only

email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if email.count("@") > 1:
        raise TooManyAtSymbolsError("The email can contain only one '@' symbol!")

    if len(email.split("@")[0]) <= MINIMUM_LENGTH_NAME:
        raise NameTooShortError("Name must be more than 4 characters")

    if len(email.split("@")[0]) > MAXIMUM_LENGTH_NAME:
        raise NameTooLongError("Name cannot be more than 64 characters!")

    if not any(email.endswith(x) for x in VALID_DOMAINS):
        # The above line checks if the email ends with any of the elements in VALID_DOMAINS
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")

    print("Email is valid")

    email = input()
