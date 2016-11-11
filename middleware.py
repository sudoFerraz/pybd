import structures

main = structures.Directory()

def createrelation(name, directory):
    """Create a new relation on the system."""
    if len(directory.ridindex) == 0 and len(directory.pagesindex) == 0:
        newrid = structures.Rid(name, main)
    else:
        newrid = structures.Rid(name, main)


def createreg(relation, attr, data):
    """Create a new tuple of a relation."""
    newreg = structures.Reg(relation)
    newreg.addfield(attr, data)
    if relation.directory.pagesindex[:-1].nreg == relation.directory[:-1].size:
        newpage = structures.Page(80, relation.directory)
        newpage.addreg(newreg)
        relation.regindex.append(newreg)
    else:
        relation.directory.pagesindex[:-1].addreg(newreg)
        relation.regindex.append(newreg)

def delrelation(rid, directory):
    """Delete a relation present on the system."""
    del rid.directory.ridlist[rid.uid]
    for key, value in directory.ridindex.iteritems():
        if directory.ridindex[key] == rid.uid:
            for i, reg in enumerate(directory.ridindex[key].regindex):
                if reg.rid.uid == rid.uid:
                    del directory.ridindex[key].regindex[i]
            del directory.ridindex[key]



def delreg():
    """Delete a tuple of a relation."""
    


def searchrelation():
    """Search for a given relation present in the system."""

def searchreg():
    """Search for a tuple of a relation present in the system."""

def returnpage():
    """Return a page that cointains certain rid."""
