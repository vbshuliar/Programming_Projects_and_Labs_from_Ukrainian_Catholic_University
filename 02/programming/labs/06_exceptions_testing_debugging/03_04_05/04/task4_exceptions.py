"""Task 4 exceptions."""


class BasicException(Exception):
    def __init__(self, message):
        super().__init__(message)


class WrongRoot(BasicException):
    pass


class WrongCursor(BasicException):
    pass


class WrongHome(BasicException):
    pass


class WrongInput(BasicException):
    pass
