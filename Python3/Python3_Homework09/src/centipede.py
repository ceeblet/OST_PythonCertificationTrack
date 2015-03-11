class Centipede:
    def __init__(self):
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []

    def __setattr__(self, key, value):
        if key in ['legs', 'stomach']:
            raise AttributeError("{0} is for internal use only".format(key))
        self.__dict__[key] = value
        if key not in ['legs', 'stomach']:
            self.__dict__['legs'].append(key)
    
    def __call__(self, *args, **kwargs):
        for arg in args:
            self.__dict__['stomach'].append(arg)
            
    def __str__(self):
        return ','.join(self.__dict__['stomach'])
    
    def __repr__(self):
        return ','.join(self.__dict__['legs'])

