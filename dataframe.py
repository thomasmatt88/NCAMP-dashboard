from sqlalchemy import create_engine
import pandas as pd
from models.Dataframe import PropertyDF

#import pymysql
#db_connection_str = 'mysql+pymysql://root:root@localhost:3306/NCAMP'
#db_connection = create_engine(db_connection_str)

#material_df = pd.read_sql('SELECT * FROM material', con=db_connection)
material_df = pd.read_pickle('data/material.pickle')
#df1 = pd.read_sql('SELECT * FROM material_properties', con=db_connection)
df1 = pd.read_pickle('data/material_properties.pickle')
#df2 = pd.read_sql('SELECT * FROM test_conditions', con=db_connection)
df2 = pd.read_pickle('data/test_conditions.pickle')
df3 = pd.merge(df1, df2, how = 'inner', left_on = 'test_conditions_id', right_on = 'id')
df4 = pd.merge(material_df, df3, how = 'inner', left_on = 'id', right_on = 'material_id')
df5 = df4

#df preprocessing
#join material and material properties by material 'id'
#drop unneccessary columns 
pdf = pd.merge(material_df[['id', 'Material']], df1, how = 'inner', left_on = 'id', right_on = 'material_id')
pdf = pdf.drop(columns = ['id_x', 'id_y'])

#join pdf and test_conditions by test_conditions_id
pdf = pd.merge(df2, pdf, how = 'inner', left_on = 'id', right_on = 'test_conditions_id')
pdf = pdf.drop(columns = ['id'])
#move 'Material' to the first column
temp = pdf['Material']
pdf = pdf.drop(columns = ['Material'])
pdf.insert(0, 'Material', temp)

# add units header to df and pdf
#material_df = material_df.rename(columns = {"MOT": "MOT (°F)", "Tg": "Tg (°F)", "WetTg" :"WetTg(°F)", "FAW": "FAW (g/m^2)"})
"""
pdf = pdf.rename(columns  = {"F1tu": "F1tu (ksi)", "F2tu": "F2tu (ksi)", "E1t": "E1t (msi)", \
    "F1cu": "F1cu (ksi)", "F2cu": "F2cu (ksi)", "F12su": "F12su (ksi)", "F31sbs": "F31sbs (ksi)", \
        "CPT": "CPT (in/ply)", "temperature": "Test Temperature (°F)", "environment": "Test Environment"})
"""
pdf = pdf.rename(columns  = {"F1cu": PropertyDF.PROPERTIES[4], "temperature": "Test Temperature", \
                            "environment": "Test Environment"})

property_df = PropertyDF(pdf)