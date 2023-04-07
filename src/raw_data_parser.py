import os
from datetime import datetime
from typing import List
import pandas as pd
from dataclasses import dataclass

@dataclass
class ParseInputs:
    data_path: str
    def __list_files(self) -> List[str]:
        return os.listdir(f"{self.data_path}/")
    
    def __read_files(self) -> pd.DataFrame:
        df=pd.DataFrame()
        for dataframe in self.dataframes_path:
            temp_df = pd.read_csv(f"{self.data_path}/{dataframe}")
            df = pd.concat([df, temp_df])
        return df

    def __normalize_column_names(self) -> pd.DataFrame:
        normalized_columns = [col.lower() for col in self.data.columns]
        self.data.columns = normalized_columns
        return self.data

    def __convert_dates(self) -> pd.DataFrame:
        self.data['date'] = self.data['date'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y"))
        return self.data

    def parse_data(self) -> pd.DataFrame:
        self.dataframes_path = self.__list_files()
        self.data = self.__read_files()
        self.data = self.__normalize_column_names()
        return self.__convert_dates()
    
