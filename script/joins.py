import pandas as pd

class DataAggregator:
    def __init__(self, id_column, column_names, data, merge_data):
     
        self.id_column = id_column
        self.column_names = column_names
        self.data = data
        self.merge_data = merge_data

    def agg_and_merge(self):
      
        agg_dict = {}

        
        for column_name in self.column_names:
            if self.data[column_name].dtype == 'object':
                agg_dict[f"{column_name}_count"] = (column_name, 'count')
            else:
                agg_dict[f"{column_name}_mean"] = (column_name, 'mean')
                agg_dict[f"{column_name}_count"] = (column_name, 'count')
                agg_dict[f"{column_name}_max"] = (column_name, 'max')
                agg_dict[f"{column_name}_min"] = (column_name, 'min')


        dataagg = self.data.groupby(self.id_column).agg(**agg_dict).reset_index()

        merged_df = self.merge_data.merge(dataagg, how='inner', on=self.id_column, suffixes=('', '_agg'))
        return merged_df
