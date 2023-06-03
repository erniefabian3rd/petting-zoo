class Walking:
    """Parent class to define walking movement"""
    def __init__(self):
        self.walk_speed = 0
        self.legs = 0

    def run(self):
        print("The animal walks")