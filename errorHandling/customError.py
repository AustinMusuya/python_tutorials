
class ValueTooHighError(Exception):

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Sorry but {self.number} is too high"
