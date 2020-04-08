from sqlalchemy import create_engine
import pandas as pd

from models.Dataframe import PropertyDF, MaterialDF
from data import material_links, process_spec_links, material_spec_links

#import pymysql
#db_connection_str = 'mysql+pymysql://root:root@localhost:3306/NCAMP'
#db_connection = create_engine(db_connection_str)

#mdf = pd.read_sql('SELECT * FROM material', con=db_connection)
mdf = pd.read_pickle('data/material.pickle').drop(columns = ["Form"])
#df1 = pd.read_sql('SELECT * FROM material_properties', con=db_connection)
df1 = pd.read_pickle('data/material_properties.pickle') #####
df1_impute = pd.read_pickle('data/material_properties_impute.pickle')

#round dfs
mdf = mdf.round(0)
df1["F1tu"] = df1["F1tu"].round(2)
df1_impute["F1tu"] = df1_impute["F1tu"].round(2)
df1["F2tu"] = df1["F2tu"].round(2)
df1_impute["F2tu"] = df1_impute["F2tu"].round(2)
df1["E1t"] = df1["E1t"].round(2)
df1_impute["E1t"] = df1_impute["E1t"].round(2)
df1["F1cu"] = df1["F1cu"].round(2)
df1_impute["F1cu"] = df1_impute["F1cu"].round(2)
df1["F2cu"] = df1["F2cu"].round(2)
df1_impute["F2cu"] = df1_impute["F2cu"].round(2)
df1["F12su"] = df1["F12su"].round(2)
df1_impute["F12su"] = df1_impute["F12su"].round(2)
df1["F31sbs"] = df1["F31sbs"].round(2)
df1_impute["F31sbs"] = df1_impute["F31sbs"].round(2)
df1["CPT"] = df1["CPT"].round(4)
df1_impute["CPT"] = df1_impute["CPT"].round(4)

#df2 = pd.read_sql('SELECT * FROM test_conditions', con=db_connection)
df2 = pd.read_pickle('data/test_conditions.pickle')
df3 = pd.merge(df1, df2, how = 'inner', left_on = 'test_conditions_id', right_on = 'id')
df4 = pd.merge(mdf, df3, how = 'inner', left_on = 'id', right_on = 'material_id')
df5 = df4

#df preprocessing
#join material and material properties by material 'id'
#drop unneccessary columns 
pdf = pd.merge(mdf[['id', 'Material']], df1, how = 'inner', left_on = 'id', right_on = 'material_id')
pdf = pdf.drop(columns = ['id_x', 'id_y'])
pdf_impute = pd.merge(mdf[['id', 'Material']], df1_impute, how = 'inner', left_on = 'id', right_on = 'material_id')
pdf_impute = pdf_impute.drop(columns = ['id_x', 'id_y'])

#join pdf and test_conditions by test_conditions_id
pdf = pd.merge(df2, pdf, how = 'inner', left_on = 'id', right_on = 'test_conditions_id')
pdf = pdf.drop(columns = ['id'])
pdf_impute = pd.merge(df2, pdf_impute, how = 'inner', left_on = 'id', right_on = 'test_conditions_id')
pdf_impute = pdf_impute.drop(columns = ['id'])
#move 'Material' to the first column
temp = pdf['Material']
pdf = pdf.drop(columns = ['Material'])
pdf.insert(0, 'Material', temp)
temp_impute = pdf_impute['Material']
pdf_impute = pdf_impute.drop(columns = ['Material'])
pdf_impute.insert(0, 'Material', temp_impute)

pdf = pdf.rename(columns  = {"F1tu": PropertyDF.PROPERTIES[1], "F2tu": PropertyDF.PROPERTIES[2], \
                            "E1t": PropertyDF.PROPERTIES[3], "F1cu": PropertyDF.PROPERTIES[4], \
                            "F2cu": PropertyDF.PROPERTIES[5], "F12su": PropertyDF.PROPERTIES[6], \
                            "F31sbs": PropertyDF.PROPERTIES[7], "CPT": PropertyDF.PROPERTIES[8], \
                            "temperature": "Test Temperature", "environment": "Test Environment"})
pdf_impute = pdf_impute.rename(columns  = {"F1tu": PropertyDF.PROPERTIES[1], "F2tu": PropertyDF.PROPERTIES[2], \
                            "E1t": PropertyDF.PROPERTIES[3], "F1cu": PropertyDF.PROPERTIES[4], \
                            "F2cu": PropertyDF.PROPERTIES[5], "F12su": PropertyDF.PROPERTIES[6], \
                            "F31sbs": PropertyDF.PROPERTIES[7], "CPT": PropertyDF.PROPERTIES[8], \
                            "temperature": "Test Temperature", "environment": "Test Environment"})

# add markdown links to Material column of property df
pdf['Material'] = pdf['Material'].map(material_links.link_map)
pdf_impute['Material'] = pdf_impute['Material'].map(material_links.link_map)
# add markdown links to ProcessSpec column of material df
mdf['ProcessSpec'] = mdf['ProcessSpec'].map(process_spec_links.link_map)
# add markdown links to MaterialSpec column of material df
mdf['MaterialSpec'] = mdf['MaterialSpec'].map(material_spec_links.link_map)

# create deep copy of mdf and add markdown links for comparison to pdf
mdf_links = pd.DataFrame.copy(mdf)
# add markdown links to Material column of mdf_links
mdf_links['Material'] = mdf_links['Material'].map(material_links.link_map)


#export these dataframes
test_conditions_df = df2.set_index('id')
property_df = PropertyDF(pdf)
property_df_impute = PropertyDF(pdf_impute)
material_df = MaterialDF(mdf)
material_df_links = MaterialDF(mdf_links)
mdf = mdf.set_index("id")
