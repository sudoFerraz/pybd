import uuid


class Page():
    """Pages that will be stored."""

    def __init__(self, size, directory):
        self.uid = str(uuid.uuid4().hex)
        self.size = size
        self.nreg = 0
        self.regindex = []
        self.nextpage = 0
        self.directory = directory

    def addreg(self, reg):
        if len(self.regindex) <= size:
            self.regindex.append(reg)
            self.nreg = self.nreg + 1
            self.directory.ridindex[reg.rid.uid] = self.uid
        else:
            newpage = Page()
            self.nextpage = newpage
            newpage.size = self.size
            newpage.nreg = 1
            newpage.regindex.append(reg)
            self.directory.pagesindex.append(newpage)
            self.directory.ridindex[reg.rid.uid] = newpage.uid

    def delreg(self, reg):
        if self.nreg == 1 and len(self.regindex) == 1:
            del self.directory.ridindex[reg.rid.uid]
            del self
        else:
            del self.regindex[reg.rid.uid]
            self.nreg = self.nreg - 1
            del self.directory.ridindex[reg.rid.uid]


class Data():
    """Data that will be stored inside entries."""

    def __init__(self, size, data):
        self.data = data
        self.flag = 0


class Directory():
    """Pages and rid location directory."""

    def __init__(self):
        self.hash = str(uuid.uuid4().hex)
        self.list = []
        self.ridindex = {}
        self.ridlist = []

class Rid():
    """Relations present in the database."""

    def __init__(self, name, directory):
        self.uid = str(uuid.uuid4().hex)
        self.regindex = []
        self.name = name
        self.directory = directory
        self.directory.ridlist.append(self.uid)


class Reg():
    """Entries of the system."""

    def __init__(self, relation):
        self.index = {}
        self.uid = str(uuid.uuid4().hex)
        self.rid = relation

    def addfield(self, attr, data):
        datanew = Data()
        datanew.data = data
        datanew.flag = 1
        self.index[attr] = datanew
        return self.index

    def delfield(self, attr):
        del self.index[attr]
        return self.index
