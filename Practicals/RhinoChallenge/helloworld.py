import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)

import time
import itertools
import requests
import numpy as np
from dronekit import connect, VehicleMode, LocationGlobalRelative

import param as PARAM
from dataTypes import geoLoc, geoCircle

print("Hello World!\nAll you libraries have been imported successfully ;)")