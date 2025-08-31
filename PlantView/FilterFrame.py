from tkinter import Frame, Button
from tkinter.messagebox import askyesno
from PlantFrame import PlantFrame

class FilterFrame(Frame, PlantFrame):
    def __init__(self, master):
        Frame().__init__(self, master)
        self.master= master
        
        self.select_filter_frame=Frame(self, name="Select filter")
        self.select_filter_frame.grid(column=0, row=0, pady=10, padx=10)
        button_apply_filter= Button(self, text="Filter anwenden", command = self.apply_filter_button_press)
        button_apply_filter.grid(column=0, row=1, pady=10, padx=10)
        button_cancel = Button(self, text="Abbrechen", command = self._confirm_closing_window_without_saving)
        button_cancel.grid(column=1, row=1, pady=10, padx=10)
        
    def _confirm_closing_window_without_saving(self):
        answer = askyesno(title="Zur Hauptansicht zurückkehren?", message="Wollen Sie ohne zu speichern zur Hauptansicht zurückkehren?")
        if (answer):
            self.master.switch_frame("PlantDBMainView") 
        else:
            self.focus()
        
    def apply_filter_button_press(self):
        pass