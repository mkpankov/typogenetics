import utility
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
            self.value = frozenset(source)
            if not self.value.issubset(bases.bases):
                raise ValueError
        except (ValueError, TypeError):
            raise InvalidBinding

class InvalidLocus(ValueError):
    pass

def get_single_from_frozenset(fs):
    for i in fs:
        return i
assert get_single_from_frozenset(frozenset('A')) == 'A'

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
        if len(binding) > 1:
            raise NotImplemented
        self.binding = Binding(binding)
    def attach(self, strand, locus):
        try:
            self.strand = strand
            self.locus = utility.string_chars_indices(strand.units)\
                [get_single_from_frozenset(self.binding.value)][locus]
        except IndexError:
            raise InvalidLocus

def translate(enzyme, strand, locus_string):
    pass
