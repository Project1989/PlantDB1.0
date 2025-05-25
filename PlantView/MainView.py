from PlantModel import PlantModel
from PlantController import PlantController
from tkinter import Tk, Label,Listbox, LabelFrame, Button
from tkinter.messagebox import askyesno
from tkinter.scrolledtext import ScrolledText
from AddPlantView import AddPlantWindow
from EditBedView import EditBedView

class PlantDBView:
    def __init__(self):
        self.data_base="PlantModel/PlantDB.json"
        self.root = Tk()
        self.root.title("Pflanzendatenbank")
        self.label_mainwindow_caption = Label(self.root, text= "Pflanzendatenbank", font=('times', 25, 'bold')) 
        self.label_mainwindow_caption.grid(column=0,row=0, columnspan=6)
        self.plant_db_model=PlantModel(self.data_base)
        self.__add_atribute_frame_to_mainview()
        self.__add_initial_list_to_mainview()
        self.__add_buttons_to_mainview()
        self.root.protocol("WM_DELETE_WINDOW",self._confirm_closing_main_window)
        self.list_plants.selection_set(0)
        self.update_atribut_label()
        self.root.mainloop()   
        
     
    def _confirm_closing_main_window(self):
        answer = askyesno(title="Programm schließen?", message="Wollen Sie das Programm wirklich schließen?")
        if (answer):
            self.root.destroy()
      
    def __add_initial_list_to_mainview(self):
        self.list_plants=Listbox(self.root)
        self.list_plants.grid(column=0, row=1, padx=10)
        self.list_plants.insert("end", *self.plant_db_model.get_list_of_plants())
        self.list_plants.bind("<<ListboxSelect>>", self.plant_list_box_on_select)
        
    def plant_list_box_on_select(self, event):
        self.update_atribut_label()
        
        
    def __add_buttons_to_mainview(self):
        BUTTON_ROW=2
        BUTTON_COL=0
        BUTTON_PAD=5
        self.button_add_plant = Button(self.root, text="Hinzufügen", command=self.add_plant_button_press)
        self.button_add_plant.grid(column=BUTTON_COL, row=BUTTON_ROW, padx=BUTTON_PAD, pady=BUTTON_PAD)
        self.button_remove_plant = Button(self.root, text="Entfernen")
        self.button_remove_plant.grid(column=BUTTON_COL+1, row=BUTTON_ROW, padx=BUTTON_PAD, pady=BUTTON_PAD)
        self.button_edit_plant = Button(self.root, text="Bearbeiten")
        self.button_edit_plant.grid(column=BUTTON_COL+2, row=BUTTON_ROW, padx=BUTTON_PAD, pady=BUTTON_PAD) 
        self.button_search_plant = Button(self.root, text="Suchen")
        self.button_search_plant.grid(column=BUTTON_COL+3, row=BUTTON_ROW, padx=BUTTON_PAD, pady=BUTTON_PAD)
        self.button_filter_plant = Button(self.root, text="Nach Atribut filtern")
        self.button_filter_plant.grid(column=BUTTON_COL+4, row=BUTTON_ROW, padx=BUTTON_PAD, pady=BUTTON_PAD) 
        self.button_remove_filter = Button(self.root, text="Filter entfernen")
        self.button_remove_filter.grid(column=BUTTON_COL+5, row=BUTTON_ROW, padx=BUTTON_PAD, pady=BUTTON_PAD)
        self.button_edit_bed = Button(self.root, text="Beete Bearbeiten", command=self.edit_bed_button_press)
        self.button_edit_bed.grid(column=BUTTON_COL, row=BUTTON_ROW + 1, padx=BUTTON_PAD, pady=BUTTON_PAD)
        
    def __add_atribute_frame_to_mainview(self):
        # Labelframe
        self.atribute_labelframe = LabelFrame(self.root, text="Pflanze")
        self.atribute_labelframe.columnconfigure([1,3], minsize=200)
        self.atribute_labelframe.grid(column=1, row=1, columnspan=5,padx=10 , pady=10)
        # Lat. Name
        self.label_lat_name_text=Label(self.atribute_labelframe, text="Lateinischer Name:")
        self.label_lat_name_text.grid(column=0, row=0)
        self.label_lat_name_value=Label(self.atribute_labelframe)
        self.label_lat_name_value.grid(column=1, row=0)
        # Plant Type
        self.label_plant_type_text= Label(self.atribute_labelframe, text="Pflanzenart:")
        self.label_plant_type_text.grid(column=0, row=1)
        self.label_plant_type_value= Label(self.atribute_labelframe)
        self.label_plant_type_value.grid(column=1, row=1)
        # water consumption
        self.label_water_consumption_text= Label(self.atribute_labelframe, text="Wasserverbrauch:")
        self.label_water_consumption_text.grid(column=0, row=2)
        self.label_water_consumption_value= Label(self.atribute_labelframe)
        self.label_water_consumption_value.grid(column=1, row=2)
        # Pruning back time
        self.label_pruning_back_time_text= Label(self.atribute_labelframe, text="Zeit für Rückschnitt:")
        self.label_pruning_back_time_text.grid(column=0, row=3)
        self.label_pruning_back_time_value= Label(self.atribute_labelframe)
        self.label_pruning_back_time_value.grid(column=1, row=3)
        # pruning back type
        self.label_pruning_back_type_text= Label(self.atribute_labelframe, text="Art des Rückschnitts:")
        self.label_pruning_back_type_text.grid(column=0, row=4)
        self.text_pruning_back_type_value= ScrolledText(self.atribute_labelframe, state="disabled", width=30, height=6)
        self.text_pruning_back_type_value.grid(column=1, row=4, pady=10)
        # Prefered Location
        self.label_prefered_location_text= Label(self.atribute_labelframe, text="Bevorzugter Standort:")
        self.label_prefered_location_text.grid(column=2, row=0)
        self.label_prefered_location_value= Label(self.atribute_labelframe)
        self.label_prefered_location_value.grid(column=3, row=0)
        # Bed location
        self.label_bed_location_text= Label(self.atribute_labelframe, text="Gepflanzt in Beet:")
        self.label_bed_location_text.grid(column=2, row=1)
        self.label_bed_location_value= Label(self.atribute_labelframe)
        self.label_bed_location_value.grid(column=3, row=1)
        # Toxic cat 
        self.label_toxic_cat_text= Label(self.atribute_labelframe, text="Giftig (Katze):")
        self.label_toxic_cat_text.grid(column=2, row=2)
        self.label_toxic_cat_value= Label(self.atribute_labelframe)
        self.label_toxic_cat_value.grid(column=3, row=2)
        # Toxic
        self.label_toxic_human_text= Label(self.atribute_labelframe, text="Giftig (Mensch):")
        self.label_toxic_human_text.grid(column=2, row=3)
        self.label_toxic_human_value= Label(self.atribute_labelframe)
        self.label_toxic_human_value.grid(column=3, row=3)
        # Comment
        self.label_comment_text= Label(self.atribute_labelframe, text="Bemerkung:")
        self.label_comment_text.grid(column=2, row=4)
        self.text_comment_value= ScrolledText(self.atribute_labelframe, state="disabled", width=30, height=6)
        self.text_comment_value.grid(column=3, row=4, pady=10)
    
    def add_plant_button_press(self):
        AddPlantWindow(self.add_plant_to_db, self.plant_db_model.get_bed_data()) 
            
    def update_atribut_label(self):
        selected_plant=self.plant_db_model.get_plant_data( self.list_plants.get(self.list_plants.curselection()))
        self.atribute_labelframe.config(text= self.list_plants.get(self.list_plants.curselection()))
        self.label_lat_name_value.config(text= selected_plant["lat-name"])
        self.label_plant_type_value.config(text=selected_plant["Pflanzen-typ"])
        self.label_water_consumption_value.config(text=selected_plant["wasserverbrauch"])
        self.label_prefered_location_value.config(text=selected_plant["standort"])
        self.label_bed_location_value.config(text=str(selected_plant["pflanzort"])[1:-1].replace("'", ""))      
        pruning_back_time_string=str([month for month in selected_plant["rückschnitt-zeitpunkt"] if selected_plant["rückschnitt-zeitpunkt"][month]])[1:-1]
        self.label_pruning_back_time_value.config(text=pruning_back_time_string.replace("'", ""))
        self.text_pruning_back_type_value.config(state="normal") 
        self.text_pruning_back_type_value.delete("1.0", "end")
        self.text_pruning_back_type_value.insert(index="1.0", chars=selected_plant["rückschnitt-art"])
        self.text_pruning_back_type_value.config(state="disabled")
        self.label_toxic_cat_value.config(text=selected_plant["giftig-katze"])
        self.label_toxic_human_value.config(text=selected_plant["giftig-mensch"])
        self.text_comment_value.config(state="normal") 
        self.text_comment_value.delete("1.0", "end")
        self.text_comment_value.insert(index="1.0", chars=selected_plant["bemerkungen"])
        self.text_comment_value.config(state="disabled")
     
    def add_plant_to_db(self, new_plant):
        p_controller=PlantController()
        p_controller.add_plant(self.data_base, new_plant)  
        

    def edit_bed_button_press(self):
        EditBedView(self.update_bed_data, self.plant_db_model.get_bed_data())
        
    def update_bed_data(self, bed_data : list):
        p_controller=PlantController()
        self.plant_db_model.plant_model_data["Beete"] = bed_data
        p_controller.update_beds(self.data_base, bed_data)
        self._update_mainview()
        
    def _update_mainview(self):
        self.plant_db_model=PlantModel(self.data_base)
        
        
        
if __name__ == '__main__':
    PlantDBView()