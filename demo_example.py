

class Demo:

    def __init__(self, gameBoard):
        self.demo_data = gameBoard

    # this is a demo example with specific board values & the maximum coins picked is 5
    def demo(self):
        self.demo_data[0][4] = 1
        self.demo_data[1][1] = 1
        self.demo_data[1][3] = 1
        self.demo_data[2][3] = 1
        self.demo_data[2][5] = 1
        self.demo_data[3][2] = 1
        self.demo_data[3][5] = 1
        self.demo_data[4][0] = 1
        self.demo_data[4][4] = 1
        return self.demo_data
