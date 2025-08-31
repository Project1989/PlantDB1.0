from tkinter import Toplevel, Label, LabelFrame, Button, Entry, ttk, scrolledtext, Frame, END
from tkinter.messagebox import askyesno, showinfo
from AddPlantView import AddPlantFrame
from PlantDBSelectMonthView import SelectMonthWindow
from SelectBedView import SelectBedWindow
from PlantFrame import PlantFrame
from DTO import DTO

class EditPlantFrame (AddPlantFrame):
    def __init__(self, master, plant_to_edit):
       AddPlantFrame.__init__(self, master)
       self.plant_to_edit = plant_to_edit
       self.label_function_description.config(text="Editieren Sie die Einträge der Pflanze die Sie ändern möchten.")
       self.plant = master.plant_db_model.get_plant_data(plant_to_edit)
       self.entry_name_value.insert(0, plant_to_edit)
       self.entry_lat_name_value.insert(0, self.plant["lat-name"])
       self.cbox_plant_type_value.set(self.plant["Pflanzen-typ"])
       self.cbox_water_consumption_value.set(self.plant["wasserverbrauch"])
       self.cbox_prefered_location_value.set(self.plant["standort"])
       self.sctext_comment_value.insert(1.0, self.plant["bemerkungen"])
       self.label_bed_location_selected.config(text=self.plant["pflanzort"])
       self.label_pruning_back_type_value.insert(1.0, self.plant["rückschnitt-art"])
       self.label_pruning_back_time_selected.config(text=str([month for month in  self.plant["rückschnitt-zeitpunkt"] if self.plant["rückschnitt-zeitpunkt"][month]])[1:-1])
       self.cbox_toxic_cat_value.set(self.plant["giftig-katze"])
       self.cbox_toxic_human_value.set(self.plant["giftig-mensch"])
      
       self.button_confirm.config(text="Bearbeiten", command = self.confirm_update_plant )
       
    def confirm_update_plant(self):
        if self._is_entry_valid(): 
            dto = DTO(name = self.entry_name_value.get(), lat_name=self.entry_lat_name_value.get(), plant_type = self.cbox_plant_type_value.get(), waterconsumption = self.cbox_water_consumption_value.get(),
                    prefered_location = self.cbox_prefered_location_value.get(), location = self.list_of_selected_beds, pruning_time = self.pruning_time_dict,
                    pruning_type = self.label_pruning_back_type_value.get("1.0", END ), toxic_cat = self.cbox_toxic_cat_value.get(), toxic_human = self.cbox_toxic_human_value.get(),
                    comment = self.sctext_comment_value.get("1.0", END))
            self.controller.update_plant(self.plant_to_edit, dto)
            self.master.switch_frame("PlantDBMainView")
        else: 
            showinfo("Fehlender Eintrag", "Bitten füllen Sie den Pflanzennamen aus")
