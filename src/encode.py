from typing import Dict
from datetime import datetime
from dataclasses import dataclass
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

@dataclass
class DataEncoder:
    """ Class to handle basic data encoding """
    data: pd.DataFrame

    def get_date_diff(self, date: datetime, start: datetime) -> int:
        return (date - start).days
    
    def encode_dates(self) -> pd.DataFrame:
        start = pd.to_datetime(self.data['date'].min())
        self.data['date_enc'] = self.data.apply(lambda x: self.get_date_diff(pd.to_datetime(x['date']), start), axis = 1)
        return self.data

    def one_hot_encode(self, column: str) -> pd.DataFrame:
        """ One hot encoder """
        column = [column]
        enc = OneHotEncoder(sparse_output=False)
        encoded_array = enc.fit_transform(self.data.loc[:, column])
        df_encoded = pd.DataFrame(encoded_array, columns=enc.get_feature_names_out())
        self.data = pd.concat([self.data, df_encoded], axis=1)
        self.data.drop(labels = column, axis=1, inplace=True)
        return self.data
    
    def label_encode(self, column: str) -> pd.DataFrame:
        """ Label encoder """
        enc = LabelEncoder()
        self.data[f"{column}_enc"] = enc.fit_transform(self.data[column])
        return self.data
    
    def encode(self, col_type_dict: Dict[str, str]) -> pd.DataFrame:
        """ Basic encoding initialiser """
        for k, v in col_type_dict.items():
            if v.lower() in ['one_hot', "one_hot_encoder"]:
                self.data = self.one_hot_encode(k)
            elif v.lower() in ["label", "dummy", "lable_encoder", "dummy_encoder"]:
                self.data = self.label_encode(k)
        self.data = self.encode_dates()
        return self.data