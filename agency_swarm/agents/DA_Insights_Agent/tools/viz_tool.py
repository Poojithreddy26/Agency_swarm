from agency_swarm.tools import BaseTool
import pandas as pd
import matplotlib.pyplot as plt

class VisualizationTool(BaseTool):
    def run(self, data: pd.DataFrame, chart_type: str, x: str, y: str):
        if chart_type == "line":
            data.plot(x=x, y=y, kind='line')
        elif chart_type == "bar":
            data.groupby(x)[y].sum().plot(kind='bar')
        plt.show()
