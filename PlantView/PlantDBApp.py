from PlantModel import PlantModel
from PlantController import PlantController
from AddPlantView import AddPlantFrame
from PlantDBMainView import PlantDBMainView
from EditBedView import EditBedView
from EditPlantView import EditPlantFrame
from FilterFrame import FilterFrame
from tkinter import Tk
from tkinter.messagebox import askyesno

class PlantDBApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.title("Pflanzendatenbank")
        self.protocol("WM_DELETE_WINDOW",self._confirm_closing_main_window)
        self.view_dict = {
            "PlantDBMainView" : PlantDBMainView,
            "EditPlantView" : EditPlantFrame,
            "EditBedView" : EditBedView,
            "AddPlantView" : AddPlantFrame,
            "FilterView" : FilterFrame
        }
        self.frame=None
        
        self.switch_frame("PlantDBMainView")
        self.plant_db_model= PlantModel()
        self.p_controller=PlantController(self.plant_db_model, self.frame)
        self.frame.set_controller(self.p_controller)
        self.frame.refresh_view()
        
    def switch_frame(self, view_name : str, plant_to_edit = None):
        """Destroys current frame and replaces it with a new one."""
        frame_class = self.view_dict[view_name]
        if (plant_to_edit == None):
            new_frame = frame_class(self)
        else:    
            new_frame = frame_class(self, plant_to_edit)
        
        if self.frame is not None:
            self.frame.destroy()
            new_frame.set_controller(self.p_controller)
            new_frame.refresh_view()            
            
        self.frame = new_frame
        self.frame.grid(row=0, column=0, sticky="nwse") 
        
         
    def _confirm_closing_main_window(self):
        answer = askyesno(title="Programm schließen?", message="Wollen Sie das Programm wirklich schließen?")
        if (answer):
            self.destroy()
          
if __name__ == '__main__':
    app=PlantDBApp()
    app.mainloop()
    