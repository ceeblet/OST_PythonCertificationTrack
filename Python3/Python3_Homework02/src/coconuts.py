"""
Inventory class that tracks different types of coconuts from around the world.
"""

class Coconut():
    pass
        
class SouthAsian(Coconut):
    """
    class defines a South Asian Coconut.
    """
    weight = 3
    
class MiddleEastern(Coconut):
    """
    class defines a Middle Eastern Coconut.
    """
    weight = 2.5
    
class American(Coconut):
    """
    class defines an American Coconut.
    """
    weight = 3.5
    
class Inventory():
    def __init__(self):
        self.coconuts = []
        #self.totalWeight = 0
        
    def add_coconut(self, co):
        """
        Add a coconut object to the inventory.
            co is the coconut object to be added
            raise an error if the item being added is not a coconut.
        """
        if isinstance(co, Coconut):
            self.coconuts.append(co)
            #self.totalWeight += co.weight
        else:
            raise AttributeError("Item being added is not a coconut object")
        
    def total_weight(self):
        """
        Return the total weight of all coconuts in the inventory.
        """
        self.totalWeight = 0
        for coconut in self.coconuts:
            self.totalWeight += coconut.weight
        
        return self.totalWeight
    