class Furnishing(object):
    def __init__(self, room):
        self.room = room
        
class Sofa(Furnishing):
    name = "Sofa"

class Bookshelf(Furnishing):
    name = "Bookshelf"
        
class Bed(Furnishing):
    name = "Bed"

class Table(Furnishing):
    name = "Table"

def map_the_home(home):
    home_map = {}
    for item in home:
        if item.room in home_map:
            items = home_map[item.room]
            items.append(item)
            home_map[item.room] = items
        else:
            home_map[item.room] = [item]
    return home_map

def counter(home):
    item_count = {}
    for item in Furnishing.__subclasses__():
        item_count[item.__name__] = 0
        
    for item in home:
        if item.name in item_count:
            item_count[item.name] = item_count[item.name] + 1
        else:
            item_count[item.name] = 1
            
    for item in item_count:
        print("{0} = {1}".format(item, item_count[item]))

if __name__ == "__main__":
    home_items = [Bed("Bedroom"), Sofa("Living Room")]
    print(map_the_home(home_items))
    counter(home_items)