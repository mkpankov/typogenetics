import utility
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
    'swi':'ast',
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
    return [strand[:locus],strand[locus:]]
assert cut(list('ABCD'),2) == [list('AB'), list('CD')]

def dlt(strands, locus, copy=False, active=0):
    del strands[active][locus]
    return strands, locus
assert dlt([list('ABCDBCA')],4) == ([list('ABCDCA')],4)
assert dlt([list('ACA')],0) == ([list('CA')],0)

def swi(active):
    return int(not active)
assert swi(1) == 0
assert swi(0) == 1

def mvr(strands, locus, copy=False, active=0):
    if copy:
        ensure_complement(strands, locus, locus+2, active)
    return locus + 1

def mvl(strands, locus, copy=False, active=0):
    if copy:
        ensure_complement(strands, locus-1, locus+1, active)
    return locus - 1

def cop(mode):
    return True

def off(mode):
    return False

def general_in(base, strands, locus, copy=False, active=0):
    strands[active].insert(locus+1, base)
    if copy:
        other = swi(active)
        strands[other].insert(locus+1, base)
    return strands, locus+1

def ina(strands, locus, copy=False, active=0):
    return general_in('A', strands, locus, copy, active)
assert ina([list('ABCDEFP')],3) == ([list('ABCDAEFP')], 4)
assert ina([list('ABCDEFP')],6) == ([list('ABCDEFPA')], 7)

def inc(strands, locus, copy=False, active=0):
    return general_in('C', strands, locus, copy, active)
assert inc([list('ABCDEFP')],3) == ([list('ABCDCEFP')], 4)

def ing(strands, locus, copy=False, active=0):
    return general_in('G', strands, locus, copy, active)
assert ing([list('ABCDEFP')],3) == ([list('ABCDGEFP')], 4)

def itt(strands, locus, copy=False, active=0):
    return general_in('T', strands, locus, copy, active)
assert itt([list('ABCDEFP')],3) == ([list('ABCDTEFP')], 4)

def rpy(strands, locus, copy=False, active=0):
    end = min(utility.find_fail_max(strands[active],'C',locus+1), 
              utility.find_fail_max(strands[active],'T',locus+1))
    if copy:
        ensure_complement(strands,locus,end+1)
    return end
assert rpy(list(['ACGTAGTC']), 2) == 3

def rpu(strands, locus, copy=False, active=0):
    end = min(utility.find_fail_max(strands[active],'A',locus+1), 
              utility.find_fail_max(strands[active],'G',locus+1))
    if copy:
        ensure_complement(strands,locus,end+1)
    return end
assert rpu(list(['ACGTAGTC']), 3) == 4

def lpy(strands, locus, copy=False, active=0):
    string = ''.join(strands[active])
    beg = max(string.find('C',0,locus),
              string.find('T',0,locus))
    if copy:
        ensure_complement(strands,beg,locus)
    return beg
assert lpy(list(['ACGTAGTC']), 2) == 1

def lpu(strands, locus, copy=False, active=0):
    string = ''.join(strands[active])
    beg = max(string.find('A',0,locus),
              string.find('G',0,locus))
    if copy:
        ensure_complement(strands,beg,locus)
    return beg
assert lpu(list(['ACGTAGTC']), 4) == 2

class InvalidBase(ValueError):
    pass

def elementary_complement(base):
    if base == 'A':
        comp = 'T'
    elif base == 'C':
        comp = 'G'
    elif base == 'G':
        comp = 'C'
    elif base == 'T':
        comp = 'A'
    else:
        raise InvalidBase
    return comp
assert elementary_complement('A') == 'T'
assert elementary_complement('C') == 'G'

def complement(strand_list, start=0, stop=None):
    if stop is None:
        stop = len(strand_list)
    c = [' '] * len(strand_list)
    c[start:stop] = map(elementary_complement,strand_list[start:stop])
    return c
assert complement(list('ACGT')) == list('TGCA')
assert complement(list('AACC'),1,2) == list(' T  ')
assert complement(list('AACC'),1,3) == list(' TG ')
assert complement(list('AACC'),1,4) == list(' TGG')

def ensure_complement(strands, start=0, stop=None, active=0):
    if stop is None:
        stop = len(strands[active])
    other = swi(active)
    try:
        strands[other].extend([' '] * (len(strands[active]) - len(strands[other])))
        strands[other][start:stop] = complement(strands[active],start,stop)[start:stop]
    except IndexError:
        strands.append(complement(strands[active],start,stop))

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
