def session_decorator(session, session_autoclose=True):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                session.commit()

                return result

            except Exception as e:
                session.rollback()
                raise e

            finally:
                if session_autoclose:
                    session.close()

        return wrapper
    return decorator
