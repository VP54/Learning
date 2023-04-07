import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
from general_plot import Plot

@dataclass
class PairPlot(Plot):
    data: pd.DataFrame
    fig: int
    ax: int
    
    def plot(self) -> None:
        f, ax = plt.subplots(figsize=(self.fig, self.ax))
        g = sns.pairplot(self.data, diag_kind="kde")
    
    def save_plot(self, save_file_path: str) -> None:
        f, ax = plt.subplots(figsize=(self.fig, self.ax))
        g = sns.pairplot(self.data, diag_kind="kde")
        g.savefig("test.png")
