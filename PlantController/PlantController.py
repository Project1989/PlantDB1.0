from PlantModel import PlantModel
from DTO import DTO
class PlantController():
    
    def add_plant(self, database : str, plant_dto : DTO):
        plant_model=PlantModel(database)
        plant_model.add_plant_to_model(plant_dto)
    
    def remove_plant(self, database : str, plant_to_be_removed : str):
        plant_model=PlantModel(database)
        plant_model.remove_plant_from_model(plant_to_be_removed)
    
    def update_plant(self,database : str, plant_dto : DTO):
        plant_model=PlantModel(database)
        plant_model.update_plant_in_model(plant_dto)
        
    def update_beds(self, database : str, bed_data : list):
        plant_model=PlantModel(database)
        plant_model.update_beds(bed_data)