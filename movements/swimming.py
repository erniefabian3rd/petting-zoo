class Swimming:
    """Parent class to define swimming movement"""
    def __init__(self):
        self.swim_speed = 0
        self.maximum_depth = 0

    def swim(self):
        print("The animal swims")