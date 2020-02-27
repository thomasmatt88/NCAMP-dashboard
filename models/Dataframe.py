import pandas as pd 

class PropertyDF(pd.DataFrame):
    #def __init__(self, *args, **kw):
        #super(PropertyDF, self).__init__(*args, **kw)
    @property
    def _constructor(self):
        return PropertyDF
    
    def filter_by_material(self, material_choice):
        if material_choice is None:
            self = self[self['material_id'] == material_choice].drop(columns = ['material_id']) #one value at a time
        else:
            self = self[self['material_id'].isin(material_choice)].drop(columns = ['material_id'])
        return self
    
    def sort_dataframe(self, sort_by):
        if len(sort_by):
            dff = self.sort_values(
                sort_by[0]['column_id'],
                ascending=sort_by[0]['direction'] == 'asc',
                inplace=False
            )
        else:
            # No sort is applied
            dff = self
        
        return dff