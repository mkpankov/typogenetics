import bases
import aminoacid

class NotInSet(ValueError):
    pass

class NotAString(TypeError):
    pass

class InvalidBinding(ValueError):
    pass

class Binding:
    """It's a preference of enzyme to attach to some particular base"""
    def __init__(self, source):
        try:
            self.binding = frozenset(source)
            if not self.binding.issubset(bases.bases):
                raise ValueError
        except (ValueError, TypeError):
            raise InvalidBinding

class Enzyme:
    """It's a machine operating on strands by means of instructions--Amino Acids"""
    def __init__(self, commands, binding):
        try:
            for item in commands:
                if not isinstance(item, str):
                    raise NotAString
                else:
                    if item not in aminoacid.aminoacids:
                        raise NotInSet
        except TypeError:
            raise
        self.commands = commands
        self.binding = Binding(binding)

def translate(enzyme, strand, locus_string):
    pass