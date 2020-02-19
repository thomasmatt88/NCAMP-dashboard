from sqlalchemy import create_engine
import pandas as pd

#db_connection_str = 'mysql+pymysql://root:root@localhost:3306/NCAMP'
#db_connection = create_engine(db_connection_str)

#df = pd.read_sql('SELECT * FROM material', con=db_connection)
df = pd.read_pickle('material.pickle')
#df1 = pd.read_sql('SELECT * FROM material_properties', con=db_connection)
df1 = pd.read_pickle('material_properties.pickle')
#df2 = pd.read_sql('SELECT * FROM test_conditions', con=db_connection)
df2 = pd.read_pickle('test_conditions.pickle')
df3 = pd.merge(df1, df2, how = 'inner', left_on = 'test_conditions_id', right_on = 'id')
df4 = pd.merge(df, df3, how = 'inner', left_on = 'id', right_on = 'material_id')
df5 = df4

#df preprocessing
#join material and material properties by material 'id'
#drop unneccessary columns 
df6 = pd.merge(df[['id', 'Material']], df1, how = 'inner', left_on = 'id', right_on = 'material_id')
df6 = df6.drop(columns = ['id_x', 'id_y'])

#join df6 and test_conditions by test_conditions_id
df6 = pd.merge(df2, df6, how = 'inner', left_on = 'id', right_on = 'test_conditions_id')
df6 = df6.drop(columns = ['id'])
#move 'Material' to the first column
temp = df6['Material']
df6 = df6.drop(columns = ['Material'])
df6.insert(0, 'Material', temp)

# add units header to df and df6
df = df.rename(columns = {"MOT": "MOT (°F)", "Tg": "Tg (°F)", "WetTg" :"WetTg(°F)", "FAW": "FAW (g/m^2)"})
"""
header_tuples = [('Material', None), ('material_id', None), ('test_conditions_id', None), \
    ('F1tu', 'ksi'), ('F2tu', 'ksi'), ('E1t', 'msi'), ('F1cu', 'ksi'), \
        ('F2cu', 'ksi'), ('F12su', 'ksi'), ('F31sbs', 'ksi'), ('CPT', 'in/ply')]
df6.columns = pd.MultiIndex.from_tuples(header_tuples)
"""
df6 = df6.rename(columns  = {"F1tu": "F1tu (ksi)", "F2tu": "F2tu (ksi)", "E1t": "E1t (msi)", \
    "F1cu": "F1cu (ksi)", "F2cu": "F2cu (ksi)", "F12su": "F12su (ksi)", "F31sbs": "F31sbs (ksi)", \
        "CPT": "CPT (in/ply)", "temperature": "Test Temperature (°F)", "environment": "Test Environment"})