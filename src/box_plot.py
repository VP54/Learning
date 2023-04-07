from typing import List, Dict, Tuple
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
from general_plot import Plot

@dataclass
class BoxPlot(Plot):
    fig: int
    ax: int
    data: pd.DataFrame
    
    def __plot(self, x: str, y: str) -> None:
        plt.clf()
        fig, ax = plt.subplots(figsize = (self.fig, self.ax))
        return sns.boxplot(x=x, y=y, data = self.data , orient="h", palette = 'magma')
    
    def plot(self, to_vizualize: List[Tuple[str]]) -> None:
        for pair in to_vizualize:
            x = pair[0]
            y = pair[1]
            self.__plot(x, y)
            
    def save_plot(self, to_vizualize: List[Tuple[str]], save_path: str) -> None:
        for pair in to_vizualize:
            x = pair[0]
            y = pair[1]
            self.__plot(x, y).get_figure().savefig(f"{save_path}/{x}_{y}.png")
