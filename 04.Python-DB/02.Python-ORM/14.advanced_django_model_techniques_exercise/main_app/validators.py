from django.core.exceptions import ValidationError


class NameValidator:

    def __init__(self, message: str):
        self.message = message

    def __call__(self, value):
        for char in value:
            # if not char.isalpha() and not char.isspace():
            if not (char.isalpha() or char.isspace()):
                raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.NameValidator', (self.message, ), {}
        )
