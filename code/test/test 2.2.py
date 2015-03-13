class Queue(object):

    def __init__(self):
        """ create an empty set of intergers"""
        self.vals = []
        
    def insert(self, e):
         if not e in self.vals:
             self.vals.append(e)
             
    def remove(self):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            e = self.vals[0]
            self.vals.remove(e)
            return e
        except:
            raise ValueError()

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
