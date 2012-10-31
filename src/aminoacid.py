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
    'int':'l', # insert T to the right of this unit
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
    'GT':'int',
    'TA':'rpy',
    'TC':'rpu',
    'TG':'lpy',
    'TT':'lpu',
}

def spa():
    pass

def cut():
    pass

def dlt():
    pass

def swi():
    pass

def mvr():
    pass

def mvl():
    pass

def cop():
    pass

def off():
    pass

def ina():
    pass

def inc():
    pass

def ing():
    pass

def int():
    pass

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
