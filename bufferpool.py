#/usr/env/python2.7
import time
import structures
import middleware
import subpolitics

class bufferpool():
    """Armazenamento de paginas na memoria."""

    def __init__(self, size):
        """Buffer pool structure."""
        self.frameindex = []
        self.size = size

    def pageregretrieve(self, tuple):
        """Create a new frame from a page by its reg."""
        newpage = middleware.searchreg(tuple)
        newframe = Frame(newpage)
        if len(self.frameindex) == self.size:
            subpolitics.refresh(self, newframe)
        else:
            self.frameindex.append(newframe)


class Frame():

    def __init__(self, page):
        """Defining frame structure."""
        self.dirtybit = 0
        self.page = page
        self.lastused = int(time.time())
        self.active = 0

