from PlantModel import PlantModel
from PlantController import PlantController
from tkinter import Tk
from tkinter.messagebox import askyesno
from AddPlantView import AddPlantWindow
from PlantDBMainView import PlantDBMainView
from EditBedView import EditBedView
from EditPlantView import EditPlantWindow

class PlantDBApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.data_base = "PlantModel/PlantDB.json"
        self.title("Pflanzendatenbank")
        self.protocol("WM_DELETE_WINDOW",self._confirm_closing_main_window)
        self.view_dict = {
            "PlantDBMainView" : PlantDBMainView,
            "EditPlantView" : EditPlantWindow,
            "EditBedView" : EditBedView,
            "AddPlantView" : AddPlantWindow
        }
        self.switch_frame("PlantDBMainView")
        self.mainloop()

    def switch_frame(self, view_name : str):
        """Destroys current frame and replaces it with a new one."""
        frame_class = self.view_dict[view_name]
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0, sticky="nwse")
        
    def add_plant_to_db(self, new_plant):
        p_controller=PlantController()
        p_controller.add_plant(self.data_base, new_plant)  
        
    def update_bed_data(self, bed_data : list):
        p_controller=PlantController()
        self.plant_db_model.plant_model_data["Beete"] = bed_data
        p_controller.update_beds(self.data_base, bed_data)
         
    def _confirm_closing_main_window(self):
        answer = askyesno(title="Programm schließen?", message="Wollen Sie das Programm wirklich schließen?")
        if (answer):
            self.destroy()
    
    def fetch_newest_model_for_views(self):
        self.plant_db_model=PlantModel(self.data_base)
        
        
if __name__ == '__main__':
    PlantDBApp()
    