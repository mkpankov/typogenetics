import bases

"""Amino Acids are instructions which are carried on strand by ribosome"""

aminoacids = {
    'cut':'s', # cut strand(s)
    'dlt':'s', # dltete base from strand
    'swi':'r', # switch enzyme to other strand
    'mvr':'s', # move one unit to the right
    'mvl':'s', # move one unit to the left
    'cop':'r', # turn one Copy mode
    'off':'l', # turn off Copy mode
    'ina':'s', # insert A to the right of this unit
    'inc':'r', # insert C to the right of this unit
    'ing':'r', # insert G to the right of this unit
    'itt':'l', # insert T to the right of this unit
    'rpy':'r', # search for the nearest pyrimidine to the right
    'rpu':'l', # search for the nearest purine to the right
    'lpy':'l', # search for the nearest pyrimidine to the left
    'lpu':'l', # search for the nearest purine to the left
}

class NotInSet(ValueError):
    pass

class NotAString(ValueError):
    pass

names = {
    'AA':'spa',
    'AC':'cut',
    'AG':'dlt',
    'AT':'swi',
    'CA':'mvr',
    'CC':'mvl',
    'CG':'cop',
    'CT':'off',
    'GA':'ina',
    'GC':'inc',
    'GG':'ing',
    'GT':'itt',
    'TA':'rpy',
    'TC':'rpu',
    'TG':'lpy',
    'TT':'lpu',
}

# Classes are:
#   1. Punctuation 'pun'
#   2. Strand manipulation 'str'
#   3. Manipulation on strand units with no supposed return value 'vd-'
#       Although it still returns production itself.
#   4. Locus manipulation 'lcs'
#   5. Mode manipulation 'md-'
classes = {
    'spa':'pun',
    'cut':'str',
    'dlt':'vd-',
    'swi':'md-',
    'mvr':'lcs',
    'mvl':'lcs',
    'cop':'md-',
    'off':'md-',
    'ina':'vd-',
    'inc':'vd-',
    'ing':'vd-',
    'itt':'vd-',
    'rpy':'lcs',
    'rpu':'lcs',
    'lpy':'lcs',
    'lpu':'lcs',
}

def spa():
    pass

def cut(strand, locus):
    return frozenset([strand[:locus],strand[locus:]])
assert cut('ABCD',2) == frozenset(['AB', 'CD'])

def dlt(strand, locus):
    return strand[:locus] + strand[locus+1:], locus
assert dlt('ABCDBCA',4) == ('ABCDCA',4)
assert dlt('ACA',0) == ('CA',0)

def swi():
    pass

def mvr(locus):
    return locus + 1

def mvl(locus):
    return locus - 1

def cop():
    pass

def off():
    pass

def ina(strand, locus):
    return strand[:locus+1] + 'A' + strand[locus+1:], locus
assert ina('ABCDEFP',3) == ('ABCDAEFP', 3)

def inc(strand, locus):
    return strand[:locus+1] + 'C' + strand[locus+1:], locus
assert inc('ABCDEFP',3) == ('ABCDCEFP', 3)

def ing(strand, locus):
    return strand[:locus+1] + 'G' + strand[locus+1:], locus
assert ing('ABCDEFP',3) == ('ABCDGEFP', 3)

def itt(strand, locus):
    return strand[:locus+1] + 'T' + strand[locus+1:], locus
assert itt('ABCDEFP',3) == ('ABCDTEFP', 3)

def rpy():
    pass

def rpu():
    pass

def lpy():
    pass

def lpu():
    pass


class Aminoacid:
    def __init__(self, duplet):
        if duplet in names.keys():
            try:
                self.name = names[duplet]
            except KeyError:
                if isinstance(duplet, str):
                    raise NotInSet
                else:
                    raise NotAString
        else:
            name = duplet
            if name in aminoacids.keys():
                self.name = name
            else:
                if isinstance(duplet, str):
                    raise NotInSet
                else:
                    raise NotAString
        self.method = eval(self.name)
