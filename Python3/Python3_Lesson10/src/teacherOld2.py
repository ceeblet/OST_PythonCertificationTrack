"""
Demonstrate simple attribute management
"""
class Teacher(object):
    
    grades = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth"}
    def __init__(self, first_name, last_name, age, classes, grade):
        self._first_name = first_name # internal data attributes are set
        self._last_name = last_name
        self._age = age
        self._classes = classes
        self._grade = grade
    
    def first_name(self):
        return self._first_name.capitalize()
    first_name = property(first_name)
    
    def last_name(self):
        return self._last_name.capitalize()
    last_name = property(last_name)
    
    def age(self):
        return int(self._age)
    age = property(age)
    
    def classes(self):
        return sorted(self._classes)
    classes = property(classes)
    
    def grade(self):
        return self.grades[self._grade]
    grade = property(grade)
    