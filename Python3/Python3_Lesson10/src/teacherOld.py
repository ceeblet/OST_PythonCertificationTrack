"""
Demonstrate simple attribute management
"""
class Teacher(object):
    
    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}
    def __init__(self, first_name, last_name, age, classes, grade):
        self.__dict__['_attrs'] = {}
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.classes = classes
        self.grade = grade
    
    def __setattr__(self, name, value):
        self._attrs[name] = value
        
    def __getattr__(self, name):
        if name not in self._attrs:
            raise AttributeError("Teacher has no attribute {0!r}".format(name))
        value = self._attrs[name]
        if name in ("first_name", "last_name"):
            return value.capitalize()
        elif name == "age":
            return int(value)
        elif name == "classes":
            return sorted(value)
        elif name == "grade":
            return self.grades[value]
        else:
            return value