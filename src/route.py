class Route:
    def __init__(self, index, start_x, start_y, destination_x, destination_y):
        self.index = int(index)
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.destination_x = int(destination_x)
        self.destination_y = int(destination_y)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "#{0} from {1},{2} to {3},{4}"\
            .format(self.index, self.start_x, self.start_y, self.destination_x, self.destination_y)
