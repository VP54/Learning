from typing import Dict, Tuple
from dataclasses import dataclass
import pandas as pd

@dataclass
class CreateFeatures:
    """ Class that will create additional descriptive features for football matches """
    data: pd.DataFrame
    
    def __combine_overall_aggreagates(self, feature_tuples: Dict[str, Tuple[str]]) -> pd.DataFrame:
        for new_col_name, feature_tuple in feature_tuples.items():
            self.data[new_col_name] = self.data[feature_tuple[0]] + self.data[feature_tuple[1]]
        return self.data
    
    def create_features(self, feature_tuples: Dict[str, Tuple[str]]) -> pd.DataFrame:
        return self.__combine_overall_aggreagates(feature_tuples)
