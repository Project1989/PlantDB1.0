import PlantModel.JsonFileHandler as JFileHandler

class PlantModel():
    def __init__(self, db_file):
        self.db_file=db_file
        self.json_file_handel=JFileHandler.JsonFileHandler()
        self.plant_model_data = self.json_file_handel.read_json_file(self.db_file)
        self.list_of_plants = self._get_plants_as_list()
    
    def _get_plants_as_list(self):
        return list(self.plant_model_data["pflanze"])
    
    def get_list_of_plants(self):
        return self.list_of_plants
    
    def get_patch_data(self):
        return self.plant_model_data["Beete"]
    
    def get_plant_data(self, plant_name):
        return self.plant_model_data["pflanze"][plant_name]
    
    def add_plant_to_model(self, plant_dto):
        json_dict=self.__convert_dto_to_json_dict(plant_dto)
        self.plant_model_data["pflanze"].setdefault(plant_dto.name, json_dict)
        self.json_file_handel.update_json_file(self.db_file,self.plant_model_data)
        
    def remove_plant_from_model(self, plant_to_be_removed):
        self.plant_model_data["pflanze"].pop(plant_to_be_removed, None)
        self.json_file_handel.update_json_file(self.db_file,self.plant_model_data)
        
        
    def __convert_dto_to_json_dict(self, plant_dto):
        return {
            "lat-name": plant_dto.lat_name,
            "Pflanzen-typ": plant_dto.plant_type,
            "wasserverbrauch": plant_dto.waterconsumption,
            "standort": plant_dto.prefered_location,
            "pflanzort": plant_dto.location,
            "rückschnitt-zeitpunkt": plant_dto.pruning_time,
            "rückschnitt-art": plant_dto.pruning_type,
            "giftig-katze": plant_dto.toxic_cat,
            "giftig-mensch": plant_dto.toxic_human,
            "bemerkungen": plant_dto.comment
            }
               
    def update_plant_in_model(self, plant_dto):
        json_dict=self.__convert_dto_to_json_dict(plant_dto)
        self.plant_model_data["pflanze"][plant_dto.name]=json_dict
        self.json_file_handel.update_json_file(self.db_file,self.plant_model_data)
        
    
        
        
    