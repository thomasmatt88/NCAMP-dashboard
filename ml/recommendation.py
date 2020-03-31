import pandas as pd
import numpy as np

df = pd.read_pickle('data/material.pickle').drop(columns = ["Form"])
form_df = pd.read_pickle('data/material.pickle').set_index("Material")["Form"]
df1 = pd.read_pickle('data/material_properties.pickle')
df2 = pd.read_pickle('data/test_conditions.pickle')

df3 = pd.merge(df, df1, how = 'inner', left_on = 'id', right_on = 'material_id')
df3 = df3.drop(columns = ["Fiber", "Resin", "MOT", "MaterialSpec", "ProcessSpec", "id_x", "id_y", "material_id"])

#mean normalization
normalize_columns = ["Tg", "WetTg", "FAW", "F1tu", "F2tu", "E1t", "F1cu", "F2cu", "F12su", "F31sbs", "CPT"]
for col in normalize_columns:
    df3[col] = (df3[col]-df3[col].mean())/df3[col].std()

temp_df = df3[["Material", "Tg", "WetTg", "FAW"]].set_index("Material").drop_duplicates()
df4 = df3.drop(columns = ["Tg", "WetTg", "FAW"]).pivot(index = "Material", columns = "test_conditions_id")
df5 = pd.merge(df4, temp_df, how = 'inner', left_on = 'Material', right_on = 'Material')

def similar_material(material):
    """
    You may also be interested in 'X'
    'X' is chosen based off of minimum Euclidean Distance (ED). 
    """
    global df5 
    df = df5
    df["Euclidean Distance"] = np.nan

    print(df5.loc[material].dropna())
    print(df5.loc[material].dropna().index)
    print(df[df5.loc[material].dropna().index])

    # remove columns of df5 with empty values for 'material'
    df5 = df5[df5.loc[material].dropna().index]
    for index in df.index:
        # np.lingalg.norm calculates l2 norm/ED by default
        # default 'ord' is 2
        df["Euclidean Distance"][index] = np.linalg.norm(df5.loc[material, :].values -
                                          # fill empty cells with zero
                                          df5.fillna(0).loc[index, :].values)
    
    
    # only recommend materials of the same 'form'
    global form_df
    final_df = pd.merge(df, form_df, how = 'inner', left_on = 'Material', right_on = 'Material')
    
    # sort df by ED and choose index
    # corresponding to min ED other that material
    similar_material = final_df.sort_values(by = ["Euclidean Distance"]).index[1]
    return similar_material

#print(similar_material("6781 S-2/MTM45-1 8-harness satin weave fabric"))