#------------------------------------------------------------------------
# ipcat: control.py
#------------------------------------------------------------------------

from .model import AppData

class Controller:
    def __init__(self):
        self.appData = AppData()
        pass

    def openFileDir(self):
        return self.appData.openFileDir
    

    
