import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
from general_plot import Plot

@dataclass
class CorrelationPlot(Plot):
    data: pd.DataFrame
    fig: int
    ax: int
    
    def __get_correlation(self) -> pd.DataFrame:
        return self.data.corr()
    
    def __get_plot_params(self):
        corr = self.__get_correlation()
        f, ax = plt.subplots(figsize=(self.fig, self.ax))
        cmap = sns.diverging_palette(230, 20, as_cmap=True)
        return corr, f, ax, cmap
        
    def save_plot(self, save_path: str) -> None:
        corr, f, ax, cmap = self.__get_plot_params()
        sns.heatmap(corr, cmap=cmap, vmax=1, vmin=-1, annot=True, center=0,
            linewidths=.5, cbar_kws={"shrink": .5})
        plt.savefig(save_path)
        
    
    def plot(self) -> None:
        corr, f, ax, cmap = self.__get_plot_params()
        sns.heatmap(corr, cmap=cmap, vmax=1, vmin=-1, annot=True, center=0,
            linewidths=.5, cbar_kws={"shrink": .5})
