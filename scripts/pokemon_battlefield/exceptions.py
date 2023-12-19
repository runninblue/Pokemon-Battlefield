class PokemonNamesException(Exception):
    def __init__(self):
        self.message = "Pokemon names not found!"
        super().__init__(self.message)

class PokemonValidationException(Exception):
    def __init__(self):
        self.message = "Pokemon validation failed!"
        super().__init__(self.message)

class PokemonSelectionException(Exception):
    def __init__(self):
        self.message = "Pokemon selection failed!"
        super().__init__(self.message)