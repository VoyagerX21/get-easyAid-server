class AppError(Exception):

    def __init__(self, message, code):
        self.msg = message,
        self.code = code