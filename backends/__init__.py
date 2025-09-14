# imgconvert/backends/__init__.py
from . import raster, vector, raw, misc

READERS = {}
WRITERS = {}

# merge all backends' mappings (modules define READERS and WRITERS)
for module in (raster, vector, raw, misc):
    r = getattr(module, "READERS", None)
    w = getattr(module, "WRITERS", None)
    if r:
        READERS.update(r)
    if w:
        WRITERS.update(w)
