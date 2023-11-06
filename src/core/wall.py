class Wall:
    def __init__(self):
        self.__exists = True

    def _create(self):
        self.__exists = True

    def _break(self):
        self.__exists = False

    @property
    def exists(self):
        return self.__exists

    def __str__(self):
        exists_str = "exists" if self.exists else "does not exists"
        return f"wall exists {exists_str}"
