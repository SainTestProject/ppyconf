__author__ = 'Administrator'

from parseIni import *
from parseIniFile import *

def test0():
    f = open("0.ini","rb")
    print getValue(f,"global","port");

def test1():
    f = open("1.ini","rb")
    strFileContent = f.read()
    f.close()
    vardict = {}

    var1 = getPlatformMap(strFileContent)

    for k,v in var1.items():
        var2 = getSectionMap(v)
        dict3 = {}
        for k2,v2 in var2.items():
            var3 = getValueMap(v2)
            dict3[k2] = var3
        vardict[k] = dict3

    print vardict["part2"]["global"]["ip"]

test0();
test1();