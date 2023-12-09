class Monkey:
    num = 0
    items = None

    def __init__(self):
        self.items = []
        self.oper = None
        self.testy = None
        self.trueTest = None
        self.falseTest = None
        self.inspectionCount = 0

    def testo(self):
        print("corn is yummy")

    def setOper(self, op):
        self.oper = op

    def setTesty(self, t):
        self.testy = t

    def setTrueTest(self, tt):
        self.trueTest = tt

    def setFalseTest(self, ft):
        self.falseTest = ft

    def setDividoness(self, dv):
        self.dividoness = dv

    def setDivido(self, dv):
        self.divido = dv

