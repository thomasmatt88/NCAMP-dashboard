from sqlalchemy import create_engine
import pandas as pd

#db_connection_str = 'mysql+pymysql://root:root@localhost:3306/NCAMP'
#db_connection = create_engine(db_connection_str)

#material_df = pd.read_sql('SELECT * FROM material', con=db_connection)
material_df = pd.read_pickle('material.pickle')
#df1 = pd.read_sql('SELECT * FROM material_properties', con=db_connection)
df1 = pd.read_pickle('material_properties.pickle')
#df2 = pd.read_sql('SELECT * FROM test_conditions', con=db_connection)
df2 = pd.read_pickle('test_conditions.pickle')
df3 = pd.merge(df1, df2, how = 'inner', left_on = 'test_conditions_id', right_on = 'id')
df4 = pd.merge(material_df, df3, how = 'inner', left_on = 'id', right_on = 'material_id')
df5 = df4

#df preprocessing
#join material and material properties by material 'id'
#drop unneccessary columns 
property_df = pd.merge(material_df[['id', 'Material']], df1, how = 'inner', left_on = 'id', right_on = 'material_id')
property_df = property_df.drop(columns = ['id_x', 'id_y'])

#join property_df and test_conditions by test_conditions_id
property_df = pd.merge(df2, property_df, how = 'inner', left_on = 'id', right_on = 'test_conditions_id')
property_df = property_df.drop(columns = ['id'])
#move 'Material' to the first column
temp = property_df['Material']
property_df = property_df.drop(columns = ['Material'])
property_df.insert(0, 'Material', temp)

# add units header to df and property_df
material_df = material_df.rename(columns = {"MOT": "MOT (°F)", "Tg": "Tg (°F)", "WetTg" :"WetTg(°F)", "FAW": "FAW (g/m^2)"})
property_df = property_df.rename(columns  = {"F1tu": "F1tu (ksi)", "F2tu": "F2tu (ksi)", "E1t": "E1t (msi)", \
    "F1cu": "F1cu (ksi)", "F2cu": "F2cu (ksi)", "F12su": "F12su (ksi)", "F31sbs": "F31sbs (ksi)", \
        "CPT": "CPT (in/ply)", "temperature": "Test Temperature (°F)", "environment": "Test Environment"})