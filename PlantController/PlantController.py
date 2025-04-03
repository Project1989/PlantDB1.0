from PlantModel.PlantModel import PlantModel
class PlantController ():
    
    def add_plant(self, database, plant_dto):
        plant_model=PlantModel(database)
        plant_model.add_plant_to_model(plant_dto)
    
    def remove_plant(self, database, plant_to_be_removed):
        plant_model=PlantModel(database)
        plant_model.remove_plant_from_model(plant_to_be_removed)
    
    def update_plant(self,database, plant_dto):
        plant_model=PlantModel(database)
        plant_model.update_plant_in_model(plant_dto)