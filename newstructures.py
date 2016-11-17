import uid

class Directory(object):
    """Table with databases."""

    def __init__(self, size):
        self.dbindex = []
        self.size = size

    def add_db(self, dbname, dbsize):
        newdb = Database(dbname, dbsize)
        self.dbindex.append(newdb)


class Database(object):
    """A database that contains several relations."""
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.uid = uid.uuid4.hexdigest()
        self.syscat = None
        self.index = {}

class SystemCatalog(object):
    """A catalog that contains information about the database."""

    def __init__(self):
        pass

class Relation(object):
    """A relation that contains several tuples."""

    def __init__(self):
        pass

class Tuple():
    """A tuple from a relation."""

    def __init__(self):
        pass
    

