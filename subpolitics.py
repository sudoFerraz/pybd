import bufferpool
import structures
import middleware

def refresh(bufferpool, frame):
    """Return a new bufferpool if full in LRU."""
    lastused = 0
    candidate = 0
    for i, badframe in enumerate(bufferpool.frameindex):
        if bufferpool.frameindex[i].lastused > lastused:
            lastused = badframe.lastused
            candidate = i
    del bufferpool.frameindex[i]
    bufferpool.frameindex.append(frame)


