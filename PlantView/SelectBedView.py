from tkinter import Toplevel, Label, Button, Listbox, END
class SelectBedWindow():
    def __init__(self, update_selected_beds, bed_data):
        self.select_bed_window=Toplevel()
        self.select_bed_window.title("Beetauswahl")
        self.update_selected_beds=update_selected_beds
        self.bed_data=bed_data
        self.bed_list=[]
        
        
        label_info=Label(self.select_bed_window, text="Auswahl des Beets.")
        label_info.grid(row=0)
        
        self.full_list_of_beds=Listbox(self.select_bed_window)
        self.full_list_of_beds.grid(column=0, row=1)
        self.full_list_of_beds.insert("end", *self.bed_data)
        self.add_bed_button_to_list=Button(self.select_bed_window, text="  -->  ", command=self._press_add_bed_button_to_list )
        self.add_bed_button_to_list.grid(column=1, row=1)
        self.list_of_selected_beds=Listbox(self.select_bed_window)
        self.list_of_selected_beds.grid(column=2, row=1)
        
        button_confirm=Button(self.select_bed_window, text="Auswählen", command=self._press_button_bed_selected)
        button_confirm.grid(row=13,column=0, sticky="W")
        button_cancel=Button(self.select_bed_window, text="Abbrechen", command=self.select_bed_window.destroy)
        button_cancel.grid(row=13,column=1, sticky="W")
        
    def _press_add_bed_button_to_list(self):
        selected_list_element_index= self.full_list_of_beds.curselection()[0]
        selected_bed=self.full_list_of_beds.get(selected_list_element_index)
        self.list_of_selected_beds.insert("end",selected_bed )
        self.full_list_of_beds.delete(selected_list_element_index)
    
    def _press_button_bed_selected(self):
        self.update_selected_beds(list(self.list_of_selected_beds.get(0, END )))
        self.select_bed_window.destroy()
        
      