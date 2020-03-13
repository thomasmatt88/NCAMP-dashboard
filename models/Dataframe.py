import pandas as pd 
#http://devanla.com/case-for-inheriting-from-pandas-dataframe.html

class PropertyDF(pd.DataFrame):
    PROPERTIES = {1: 'F1tu', 2: 'F2tu', 3: 'E1t', 4: 'F1cu', \
                  5: 'F2cu', 6: 'F12su', 7: 'F31sbs', 8: 'CPT'}

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
                (prop_range[0] <= self[PropertyDF.PROPERTIES[prop]]) & \
                    (self[PropertyDF.PROPERTIES[prop]] <= prop_range[1])
            ]
        
        return dff

class MaterialDF(pd.DataFrame):
    
    PROPERTIES = {1: 'MOT', 2: 'Tg', 3: 'WetTg', 4: 'FAW'}

    @property
    def _constructor(self):
        return MaterialDF
    
    # def filter_by_Tg(self, Tg_range):
    #     dff = self[
    #             (Tg_range[0] <= self['Tg']) & \
    #                 (self['Tg'] <= Tg_range[1])
    #         ]
    #     return dff

    def filter_by_physical_property(self, prop, prop_range):
        dff = self[
                (prop_range[0] <= self[MaterialDF.PROPERTIES[prop]]) & \
                    (self[MaterialDF.PROPERTIES[prop]] <= prop_range[1])
            ]
    
        return dff