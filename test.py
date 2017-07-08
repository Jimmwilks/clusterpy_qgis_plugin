from qgis.core import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import workers
from user import home
from qgis.utils import iface

# supply path to qgis install location
QgsApplication.setPrefixPath("/usr", True)

# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI
qgs = QgsApplication([], False)

# load providers
qgs.initQgis()
# Write your code here to load some layers, use processing algorithms, etc.
layer = QgsVectorLayer("/home/jamie/EssexCluster.shp", "test-input", "ogr")

if not layer:
  print "Layer failed to load!"
  
info = {
    'attrname' : "population",
    'thresholdattr' : "population",
    'threshold' : 30000,
    'maxit' : 2,
    'tabumax' : 5,
    'tabusize' : 5,
    'output_path' : home,
    'layer' : layer
}
worker = workers.MaxPWorker(info)
worker.run()
            
# When your script is complete, call exitQgis() to remove the provider and
# layer registries from memory
qgs.exitQgis()