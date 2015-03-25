class Item(object):
    def __init__(self, finerate, odtime, title, idnum, checkout):
        self.finerate = finerate
        self.odtime = odtime
        self.title = title
        self.idnum = idnum
        self.checkout = checkout
        
    def isoverdue(self, date):
        return True
        
    def getid(self):
        return self.idnum
        
        
class Journal(Item(finerate=1,odtime=2, title, idnum, checkout)):
    def setfine_od(self):
        self.finerate=1
        self.odtime=4
