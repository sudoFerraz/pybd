import uuid

class Page():
    """Pages that will be stored."""

    def __init__(self, size):
        self.uid = str(uuid.uuid4().hex)
        self.size = size
        self.nreg = 0
        self.regindex = []
        self.nextpage = 0

    def addreg(self, reg):
        if len(self.regindex) > size:
            self.regindex.append(reg)
            self.nreg = self.nreg + 1
        else:
            newpage = Page()
            self.nextpage = newpage
            newpage.uid = str(uuid.uuid4().hex)
            newpage.size = self.size
            newpage.nreg = 1
            newpage.regindex.append(reg)



class Data():
    """Data that will be stored inside entries."""

    def __init__(self, size, data):
        self.data = data
        self.flag = 0


class Directory():
    """Pages and rid location directory."""

    def __init__(self):
        self.hash = str(uuid.uuid4().hex)
        self.pagesindex = []
        self.ridindex = {}

class Reg():
    """Entries of the system."""

    def __init__(self, relation):
        self.index = {}
        self.uid = str(uuid.uuid4().hex)
        self.name = relation

    def addfield(self, attr, data):
        datanew = Data()
        datanew.data = data
        datanew.flag = 1
        self.index[attr] = datanew
        return self.index

    def delfield(self, attr):
        del self.index[attr]
        return self.index
