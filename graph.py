import matplotlib.pyplot as plt

class graph:
    def __init__(self, title, x_label, y_label, objs):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.objs = objs
        self.create_graph()

    def create_graph(self):
        for obj in self.objs:
            plt.plot(obj.get_moistures(), obj.get_days(), label = obj.get_name())
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)

    def show_graph():
        plt.show()