import unittest
from shutil import copy
import PlantModel.JsonFileHandler as JsonFHandler
import PlantModel.PlantModel as PModel
import filecmp
from tests.JsonTestDict import JsonTestDict
from DataTransferObject.DTO import DTO

class TestJsonAbstraction(unittest.TestCase):
  
    def test_read_json_file(self):
        file_handle=JsonFHandler.JsonFileHandler()
        self.assertDictEqual(JsonTestDict.json_test_dict,file_handle.read_json_file("doc/PlantDB_example.json"))
        
    def test_update_json_file(self):
        open("tests/test_file.json","w").close()
        self.assertNotEqual(True , filecmp.cmp("doc/PlantDB_example.json","tests/test_file.json",shallow=False))
        file_handel=JsonFHandler.JsonFileHandler()
        file_handel.update_json_file("tests/test_file.json", JsonTestDict.json_test_dict)       
        self.assertEqual(True, filecmp.cmp("doc/PlantDB_example.json","tests/test_file.json",shallow=False))
 
class TestPlantModel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPlantModel, self).__init__(*args, **kwargs)
        self.plant_model=PModel.PlantModel("doc/PlantDB_example.json")
        self.test_list_of_plants = ["Pflanze1", "Pflanze2"]
        
    def test_get_list_of_plants(self):
        self.assertEqual(self.test_list_of_plants,self.plant_model.get_list_of_plants())   
        
    def test_get_patch_data(self):
        
        self.assertEqual(["Beet1","Beet2","Beet3"], self.plant_model.get_patch_data())
        
    def test_get_plant_data(self):
        self.assertEqual(JsonTestDict.json_test_dict["pflanze"]["Pflanze1"],self.plant_model.get_plant_data("Pflanze1"))
        self.assertEqual(JsonTestDict.json_test_dict["pflanze"]["Pflanze2"],self.plant_model.get_plant_data("Pflanze2"))
        
    def test_add_plant_to_model(self):
        copy("doc/PlantDB_example.json","doc/PlantDB_example_test_copy.json")
        self.assertEqual(False, filecmp.cmp("doc/PlantDB_example_test_copy.json","doc/PlantDB_test_add_plant.json", shallow=False))
        dto=DTO()
        dto.name="Pflanze3"
        dto.lat_name="planta3"
        dto.plant_type="Blume"
        dto.waterconsumption="mittel"
        dto.prefered_location="sonnig"
        dto.location=["Beet1"]
        dto.pruning_time=["Januar","Februar"]
        dto.pruning_type="Rückschnitt bis zu 40cm"
        dto.toxic_cat="nein"
        dto.toxic_human="nein"
        dto.comment="Bienenfreundlich"
        plant_model = PModel.PlantModel("doc/PlantDB_example_test_copy.json")
        plant_model.add_plant_to_model(dto)
        self.assertEqual(JsonTestDict.json_test_add_plant_dict, plant_model.plant_model_data)
        self.assertEqual(True,filecmp.cmp("doc/PlantDB_example_test_copy.json","doc/PlantDB_test_add_plant.json", shallow=False))
        
    def test_remove_plant_from_model(self):
        self.maxDiff=None
        copy("doc/PlantDB_example.json","doc/PlantDB_example_test_copy.json")
        self.assertEqual(False, filecmp.cmp("doc/PlantDB_example_test_copy.json","doc/PlantDB_test_remove_plant.json", shallow=False))
        plant_model=PModel.PlantModel("doc/PlantDB_example_test_copy.json")
        plant_model.remove_plant_from_model("Pflanze1")
        self.assertEqual(JsonTestDict.json_test_remove_plant_dict, plant_model.plant_model_data)
        self.assertEqual(True,filecmp.cmp("doc/PlantDB_example_test_copy.json","doc/PlantDB_test_remove_plant.json", shallow=False))
    
    def test_update_plant_in_model(self):
        copy("doc/PlantDB_example.json","doc/PlantDB_example_test_copy.json")
        self.assertEqual(False, filecmp.cmp("doc/PlantDB_example_test_copy.json","doc/PlantDB_test_update_plant.json", shallow=False))
        dto=DTO()
        dto.name="Pflanze1"
        dto.lat_name="planta1.1"
        dto.plant_type="Strauch"
        dto.waterconsumption="hoch"
        dto.prefered_location="sonnig"
        dto.location=["Beet1", "Beet2"]
        dto.pruning_time=["März","April"]
        dto.pruning_type=""
        dto.toxic_cat="nein"
        dto.toxic_human="ja"
        dto.comment="Insektenfreundlich"
        plant_model=PModel.PlantModel("doc/PlantDB_example_test_copy.json")
        plant_model.update_plant_in_model(dto)
        self.assertEqual(JsonTestDict.json_test_update_dict, plant_model.plant_model_data)    
        
if __name__ == '__main__':
    unittest.main()