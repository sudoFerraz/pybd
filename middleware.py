import structures

main = structures.Directory()

def movereg():
    """Move a rid from a page to another."""

def createrelation(name, directory):
    """Create a new relation on the system."""
    if len(main.ridindex) == 0 and len(main.pagesindex) == 0:
        newrid = structures.Rid(name, main)
    else:
        newrid = structures.Rid(name, main)


def createreg(relation):
    """Create a new tuple of a relation."""
    newreg = structures.Reg(relation)

def delrelation():
    """Delete a relation present on the system."""

def delreg():
    """Delete a tuple of a relation."""

def searchrelation():
    """Search for a given relation present in the system."""

def searchreg():
    """Search for a tuple of a relation present in the system."""

def returnpage():
    """Return a page that cointains certain rid."""
