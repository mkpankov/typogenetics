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

class NotAttached(RuntimeError):
    pass

class OffStrand(RuntimeError):
    pass

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
        self.status = 'not attached'
        self.copy = False
        self.active_strand = 0
        
    def attach(self, strand, locus):
        try:
            self.strand = strand
            # this extracts number of the character, 
            # which is binding for the enzyme, out of strand, 
            # considering locus as index in list of all such characters
            self.locus = utility.string_chars_indices(strand.units)\
                [get_single_from_frozenset(self.binding.value)][locus]
            self.status = 'attached'
            self.production = [self.strand.units]
        except IndexError:
            raise InvalidLocus

    def translate(self):
        if self.status is None or self.status != 'attached':
            raise NotAttached
        for a in self.commands:
            c = aminoacid.classes[a]
            f = getattr(aminoacid, a)
            if c == 'pun':
                yield self.production
                self.production = ''
            elif c == 'str':
                self.production = f(self.production, self.locus)
            elif c == 'vd-':
                self.production, self.locus = f(self.production, self.locus)
            elif c == 'lcs':
                self.locus = f(self.production,self.locus,self.copy)
            elif c == 'md-':
                old = self.copy
                self.copy = f(self.copy)
                if old == False and self.copy == True:
                    self.production.append(aminoacid.complement(self.production[self.active_strand], self.locus, self.locus+1))
            elif c == 'ast':
                old = self.active_strand
                self.active_strand = f(self.active_strand)
                if old != self.active_strand:
                    self.production[self.active_strand] = self.production[self.active_strand][::-1]
            if self.locus < 0 or self.locus >= len(self.production[self.active_strand]):
                raise OffStrand
        yield self.production
