import pandas as pd 

def filter_by_material(material_choice, df):
    if material_choice is None:
        df = df[df['material_id'] == material_choice].drop(columns = ['material_id']) #one value at a time
    else:
        df = df[df['material_id'].isin(material_choice)].drop(columns = ['material_id'])
    return df

def sort_dataframe(sort_by, df):
    if len(sort_by):
        dff = df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df
    
    return dff
