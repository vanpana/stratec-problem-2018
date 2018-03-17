class Route:
    def __init__(self, index, start_x, start_y, start_z, destination_x, destination_y, destination_z):
        self.index = int(index)
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.start_z = int(start_z)
        self.destination_x = int(destination_x)
        self.destination_y = int(destination_y)
        self.destination_z = int(destination_z)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "#{0} from {1},{2},{3} to {4},{5},{6}"\
            .format(self.index, self.start_x, self.start_y, self.start_z,
                    self.destination_x, self.destination_y, self.destination_z)
