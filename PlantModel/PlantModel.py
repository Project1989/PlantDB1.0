from JsonFileHandler import JsonFileHandler as JFileHandler

class PlantModel():
    def __init__(self):
        self.db_file="PlantModel/PlantDB.json"
        self.json_file_handel=JFileHandler()
        self.plant_model_data = self.json_file_handel.read_json_file(self.db_file)
        self.list_of_plants = self._get_plants_as_list()
    
    def _get_plants_as_list(self):
        return list(self.plant_model_data["pflanze"])
    
    def _update_list_of_plants(self):
        self.list_of_plants = self._get_plants_as_list()
    
    def get_list_of_plants(self):
        return self.list_of_plants
    
    def get_bed_data(self):
        return self.plant_model_data["Beete"]
    
    def get_plant_data(self, plant_name):
        return self.plant_model_data["pflanze"][plant_name]
    
    def add_plant_to_model(self, plant_dto):
        json_dict=self.__convert_dto_to_json_dict(plant_dto)
        self.plant_model_data["pflanze"].setdefault(plant_dto.name, json_dict)
        self._update_list_of_plants()
        self.json_file_handel.update_json_file(self.db_file,self.plant_model_data)
        
    def remove_plant_from_model(self, plant_to_be_removed):
        self.plant_model_data["pflanze"].pop(plant_to_be_removed, None)
        self._update_list_of_plants()
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
               
    def update_plant_in_model(self, plant_to_update, plant_dto):
        json_dict=self.__convert_dto_to_json_dict(plant_dto)
        self.plant_model_data["pflanze"][plant_to_update]=json_dict
        self.json_file_handel.update_json_file(self.db_file,self.plant_model_data)
        if plant_dto.name !=plant_to_update:  
            self.plant_model_data["pflanze"][plant_dto.name] = self.plant_model_data["pflanze"][plant_to_update]
            del self.plant_model_data["pflanze"][plant_to_update]
        self._update_list_of_plants()
        
    def update_beds(self, bed_data : list):
        self.plant_model_data["Beete"] = bed_data
        for plant in self.plant_model_data["pflanze"]:
            local_plant=self.plant_model_data["pflanze"][plant]["pflanzort"][:]
            for bed in local_plant:
                if bed not in self.plant_model_data["Beete"]:
                    self.plant_model_data["pflanze"][plant]["pflanzort"].remove(bed) 
                    
        self.json_file_handel.update_json_file(self.db_file,self.plant_model_data)
        
    