from abc import ABC, abstractmethod

class Plot(ABC):
    @abstractmethod
    def plot():
        raise NotImplementedError("Plotting has to have function that does the plotting")
    
    @abstractmethod
    def save_plot():
        raise NotImplementedError("Plotting has to have function that does the plotting")