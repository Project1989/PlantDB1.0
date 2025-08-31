from tkinter import Label, Button, Listbox, LabelFrame, Entry,Frame, END
from tkinter.messagebox import askyesno
from PlantFrame import PlantFrame

class EditBedView (Frame, PlantFrame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self._master=master
        self.controller=None
        self.bed_data=self.controller.get_model().get_bed_data()
        label_function_description=Label(self, text="Entfernen und hinzufügen von Beeten")
        label_function_description.grid(column=0, row=0, columnspan=4)
        
        # Listbox list of beds
        self.list_beds=Listbox(self)
        self.list_beds.grid(column=0, row=1, pady=10)
        self.list_beds.insert("end", *self.bed_data)
        # LabelFrame Frame edit list
        self.label_frame_edit_list=LabelFrame(self, text="test")
        self.label_frame_edit_list.grid(column=1, row=1, padx=10, pady=10)
        # Label new bed
        self.label_new_bed=Label(self.label_frame_edit_list, text="Neues Beet")
        self.label_new_bed.grid(column=0,row=0, columnspan=2)
        # Button add to list
        self.button_add_to_list=Button(self.label_frame_edit_list, text="<-- Hinzufügen", command=self._add_to_list)
        self.button_add_to_list.grid(column=0, row=1)
        # Entry new bed
        self.entry_new_bed=Entry(self.label_frame_edit_list)
        self.entry_new_bed.grid(column=1, row=1, padx=10)
        # Label Delete bed
        label_delete_bed=Label(self.label_frame_edit_list, text="Entferne ausgewähltes Beet:")
        label_delete_bed.grid(column=0 , row=2, pady=20)
        # Button delete selected bed from list 
        self.button_delete_from_list=Button(self.label_frame_edit_list, text="Entfernen", command=self._remove_from_list)
        self.button_delete_from_list.grid(column=1 , row=2, pady=20)
               
        button_confirm = Button(self, text="Datenbank aktualisieren", command = self._confirm_edit_bed)
        button_confirm.grid(column=0, row=2, pady=10, padx=10)
        button_cancel = Button(self, text="Abbrechen", command = self._confirm_closing_window_without_saving)
        button_cancel.grid(column=1, row=2, pady=10, padx=10)
        
    def _confirm_closing_window_without_saving(self):
        answer = askyesno(title="Zur Hauptansicht zurückkehren?", message="Wollen Sie ohne zu speichern zur Hauptansicht zurückkehren?")
        if (answer):
            self.master.switch_frame("PlantDBMainView") 
        else:
            self.focus()
        
    def _confirm_edit_bed(self):
        self.controller.update_beds(list(self.list_beds.get(0, END)))
        self.master.switch_frame("PlantDBMainView")
        
    def _add_to_list(self):
        if (self.entry_new_bed.get()!=""):
            self.list_beds.insert( END, self.entry_new_bed.get())
            self.entry_new_bed.delete(0, END)
    
    def _remove_from_list(self):
        #confirm_removal_inst=ConfirmRemovalView(self, self.list_beds.get(self.list_beds.curselection()))
        bed_name=self.list_beds.get(self.list_beds.curselection())
        confirm_removal=askyesno(title="Beet entfernen?", message=f"Wollen Sie das Beet \"{bed_name}\" wirklich enfernen?")
        if (confirm_removal):
            self.list_beds.delete(self.list_beds.curselection())
        
        self.focus()
        
        