from tkinter import Toplevel, Label, LabelFrame, Button, Entry, ttk, scrolledtext, Frame, END
from tkinter.messagebox import askyesno, showinfo
from PlantFrame import PlantFrame
from PlantDBSelectMonthView import SelectMonthWindow
from SelectBedView import SelectBedWindow
from DTO import DTO

class AddPlantFrame (Frame, PlantFrame):
    def __init__(self, master):
        Frame.__init__(self, master)
        PlantFrame.__init__(self)
        self.pruning_time_dict={}
        self.predefined_plant_species_list=["Baum", "Strauch", "Staude", "Zwiebelpflanze", "Bodendecker", "Gemüse", "Obst", "Gräser"]
        self.predefined_water_consumption_list=["wenig","mittel","hoch"]
        self.predefined_prefered_location_list=["Schatten","Halbschatten","Sonne"]
        self.predefined_toxic_list=["ja","nein"]
        self.list_of_beds = master.plant_db_model.get_bed_data()
        self.list_of_selected_beds= []
        self.master=master
      
                
        # Description Label
        self.label_function_description=Label(self, text="Bitte füllen Sie die Felder aus.")
        self.label_function_description.grid(column=0, row=0, columnspan=4)
        # Label Frame
        atribute_labelframe = LabelFrame(self)
        atribute_labelframe.columnconfigure([1,3], minsize=200)
        atribute_labelframe.grid(column=1, row=1, columnspan=5,padx=10 , pady=10)
        # Name
        label_name_text=Label(atribute_labelframe, text="Pflanzen-Name:")
        label_name_text.grid(column=0, row=0)
        self.entry_name_value=Entry(atribute_labelframe)
        self.entry_name_value.grid(column=1, row=0)
        # Latin name
        label_lat_name_text=Label(atribute_labelframe, text="Lateinischer Name:")
        label_lat_name_text.grid(column=0, row=1)
        self.entry_lat_name_value=Entry(atribute_labelframe)
        self.entry_lat_name_value.grid(column=1, row=1)
        # Plant type
        label_plant_type_text= Label(atribute_labelframe, text="Pflanzenart:")
        label_plant_type_text.grid(column=0, row=2)
        self.cbox_plant_type_value= ttk.Combobox(atribute_labelframe, state="readonly", values=self.predefined_plant_species_list)
        self.cbox_plant_type_value.grid(column=1, row=2)
        # Waterconsumption
        label_water_consumption_text= Label(atribute_labelframe, text="Wasserverbrauch:")
        label_water_consumption_text.grid(column=0, row=3)
        self.cbox_water_consumption_value= ttk.Combobox(atribute_labelframe, state="readonly", values=self.predefined_water_consumption_list)
        self.cbox_water_consumption_value.grid(column=1, row=3)
        # Prefered location
        label_prefered_location_text= Label(atribute_labelframe, text="Bevorzugter Standort:")
        label_prefered_location_text.grid(column=0, row=4)
        self.cbox_prefered_location_value= ttk.Combobox(atribute_labelframe,state="readonly", values=self.predefined_prefered_location_list)
        self.cbox_prefered_location_value.grid(column=1, row=4)
        # Comment
        label_comment_text= Label(atribute_labelframe, text="Bemerkung:")
        label_comment_text.grid(column=0, row=5)
        self.sctext_comment_value= scrolledtext.ScrolledText(atribute_labelframe, width=60, height=4)
        self.sctext_comment_value.grid(column=1, row=5,columnspan=3, pady=5, padx=5)
        # Bed location
        label_bed_location_text= Label(atribute_labelframe, text="Pflanzort" )
        label_bed_location_text.grid(column=2, row=0)
        bed_location_labelframe= LabelFrame(atribute_labelframe)
        bed_location_labelframe.grid(column=3,row=0, padx=10, pady=10)
        button_open_bed_location_selection_window= Button(bed_location_labelframe, text="Pflanzort wählen", command=self.open_select_bed_location_window)
        button_open_bed_location_selection_window.grid(column=0, row=0, padx=5, pady=5)
        self.label_bed_location_selected= Label(bed_location_labelframe,text="empty")
        self.label_bed_location_selected.grid(column=1, row=0, padx=5, pady=5)
        # Pruning back type
        label_pruning_back_type_text= Label(atribute_labelframe, text="Art des Rückschnitts:")
        label_pruning_back_type_text.grid(column=2, row=1)
        self.label_pruning_back_type_value= scrolledtext.ScrolledText(atribute_labelframe, width=30, height=3)
        self.label_pruning_back_type_value.grid(column=3, row=1)
        # Pruning back time
        label_pruning_back_time_text= Label(atribute_labelframe, text="Zeit für Rückschnitt:")
        label_pruning_back_time_text.grid(column=2, row=2)
        pruning_time_labelframe = LabelFrame(atribute_labelframe)
        pruning_time_labelframe.grid(column=3, row=2,padx=10 , pady=10)
        button_open_pruning_time_window=Button(pruning_time_labelframe,text="Rückschnittzeit" ,command=self.open_pruning_time_window)
        button_open_pruning_time_window.grid(column=0, row=0, padx=5, pady=5)
        self.label_pruning_back_time_selected=Label(pruning_time_labelframe, text=str([value for value in self.pruning_time_dict.values()]))
        self.label_pruning_back_time_selected.grid(column=1, row=0, padx=5, pady=5)
        # Toxic cat
        label_toxic_cat_text= Label(atribute_labelframe, text="Giftig (Katze):")
        label_toxic_cat_text.grid(column=2, row=3)
        self.cbox_toxic_cat_value= ttk.Combobox(atribute_labelframe, state="readonly",values=self.predefined_toxic_list)
        self.cbox_toxic_cat_value.grid(column=3, row=3)
        # Toxic human
        label_toxic_human_text= Label(atribute_labelframe, text="Giftig (Mensch):")
        label_toxic_human_text.grid(column=2, row=4)
        self.cbox_toxic_human_value= ttk.Combobox(atribute_labelframe, state="readonly", values=self.predefined_toxic_list)
        self.cbox_toxic_human_value.grid(column=3, row=4)
        
        
        self.button_confirm = Button(self, text="Hinzufügen", command= self.confirm_add_plant)
        self.button_confirm.grid(column=0, row=2, padx=10, pady=10)
        button_cancel = Button(self, text="Abbrechen", command= self._confirm_closing_window_without_saving)
        button_cancel.grid(column=1, row=2, padx=10, pady=10)
    
    def refresh_view(self):
        pass
        
    def confirm_add_plant(self):
        if self._is_entry_valid(): 
            dto = DTO(name = self.entry_name_value.get(), lat_name=self.entry_lat_name_value.get(), plant_type = self.cbox_plant_type_value.get(), waterconsumption = self.cbox_water_consumption_value.get(),
                      prefered_location = self.cbox_prefered_location_value.get(), location = self.list_of_selected_beds, pruning_time = self.pruning_time_dict,
                      pruning_type = self.label_pruning_back_type_value.get("1.0", END ), toxic_cat = self.cbox_toxic_cat_value.get(), toxic_human = self.cbox_toxic_human_value.get(),
                      comment = self.sctext_comment_value.get("1.0", END))
            self.controller.add_plant(dto)
            self.master.switch_frame("PlantDBMainView")
        else: 
            showinfo("Fehlender Eintrag", "Bitten füllen Sie den Pflanzennamen aus")

    def _confirm_closing_window_without_saving(self):
        answer = askyesno(title="Zur Hauptansicht zurückkehren?", message="Wollen Sie ohne zu speichern zur Hauptansicht zurückkehren?")
        if (answer):
            self.master.switch_frame("PlantDBMainView") 
        else:
            self.focus()

    def _is_entry_valid(self) -> bool:
        if self.entry_name_value.get() == None or self.entry_name_value.get().isspace():
            print(self.entry_name_value.get() == None)
            print(self.entry_name_value.get().isspace())
            return False
        else: 
            return True 

    def open_pruning_time_window(self):
        SelectMonthWindow(self.update_pruning_month) 

    def update_pruning_month(self,pruning_time_dict):
        self.pruning_time_dict=pruning_time_dict
        self.label_pruning_back_time_selected.config(text=str([k for k in self.pruning_time_dict if self.pruning_time_dict[k] == 1])) 

    def open_select_bed_location_window(self):
          SelectBedWindow(self.update_selected_beds, self.list_of_beds)
          
    def update_selected_beds(self, list_of_beds):
        self.list_of_selected_beds=list_of_beds
        self.label_bed_location_selected.config(text=list_of_beds)
