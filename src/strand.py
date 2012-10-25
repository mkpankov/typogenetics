bases = frozenset(['A', 'C', 'G', 'T'])

class IncorrectString(ValueError):
    pass

class NotAString(TypeError):
    pass

class Strand:
    def __init__(self, string):
        if isinstance(string, str):
            if frozenset(string) != bases:
                raise IncorrectString
        else:
            raise NotAString

        self.contents = string

    def __repr__(self):
        return 'Strand("{0}")'.format(self.contents)

    def __str__(self):
        return 'Strand("{0}")'.format(self.contents)
