class PokemonNamesNumberException(Exception):
    def __init__(self, message="Please provide two pokemon names"):
        self.message = message
        super().__init__(self.message)

class PokemonNamesException(Exception):
    def __init__(self, message="Pokemon names not found!"):
        self.message = message
        super().__init__(self.message)

class PokemonValidationException(Exception):
    def __init__(self, message="Pokemon validation failed!"):
        self.message = message
        super().__init__(self.message)

class PokemonSelectionException(Exception):
    def __init__(self, message="Pokemon selection failed!"):
        self.message = message
        super().__init__(self.message)
