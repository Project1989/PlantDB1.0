from PlantModel import PlantModel
from DTO import DTO
class PlantController():
    def __init__(self, model, view) -> None:
        self._model=model
        self.view=view
    
    def get_model(self):
        return self._model
    
    def add_plant(self, plant_dto : DTO):
        self._model.add_plant_to_model(plant_dto)
    
    def remove_plant(self, plant_to_be_removed : str):
        self._model.remove_plant_from_model(plant_to_be_removed)
    
    def update_plant(self,plant_to_update :str, plant_dto : DTO):
        self._model.update_plant_in_model(plant_to_update, plant_dto)
        
    def update_beds(self, bed_data : list):
        self._model.update_beds(bed_data)