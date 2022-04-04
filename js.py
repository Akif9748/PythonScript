from cmath import isfinite, isnan
import os
import math as Math
import json
from datetime import datetime as Date

Number = float
String = str
isNaN = isnan
isFinite = isfinite
false = False
true = True

class JSON:
    stringify = json.loads
    parse = json.dumps


class console:
    debug = warn = dir = info = error = log = print

    def clear():
        os.system("cls")
