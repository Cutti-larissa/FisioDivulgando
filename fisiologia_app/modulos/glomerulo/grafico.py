from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Grafico(FigureCanvasQTAgg):

    def __init__(self):

        self.fig = Figure()
        self.fig.patch.set_facecolor("#FFFFFF")

        super().__init__(self.fig)

        self.ax = self.fig.add_subplot(111)

    def plotar(self, x, y):

        self.ax.clear()
        self.ax.scatter(x, y, color="#4361EE", s=60, zorder=3)
        self.ax.plot(x, y, color="#4361EE", alpha=0.25, zorder=2)
        self.ax.set_xlabel("Qa (nL/min)")
        self.ax.set_ylabel("FPN")
        self.ax.grid(True, alpha=0.3)

        self.draw()
