from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Grafico(FigureCanvasQTAgg):

    def __init__(self):

        self.fig = Figure()

        super().__init__(self.fig)
        
        self.ax = self.fig.add_subplot(111)


    def plotar(self,x,y):

        self.ax.clear()
        self.ax.scatter(x,y)
        self.ax.set_xlabel("Qa (nL/min)")
        self.ax.set_ylabel("FPN")
        self.ax.grid()

        self.draw()