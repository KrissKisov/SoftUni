def validate_parameter(parameter, message):

    if not parameter.strip():
        raise ValueError(message)
