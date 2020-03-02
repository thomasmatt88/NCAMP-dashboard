import pandas as pd 

class PropertyDF(pd.DataFrame):
    PROPERTIES = {1: 'F1tu', 2: 'F2tu', 3: 'E1t', 4: 'F1cu', 5: 'F2cu', 6: 'F12su', 7: 'F31sbs'}

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
    
    def filter_by_property(self, prop, prop_range):
        dff = self[
                (prop_range[0] < self[PropertyDF.PROPERTIES[prop]]) & \
                    (self[PropertyDF.PROPERTIES[prop]] < prop_range[1])
            ]
        
        return dff