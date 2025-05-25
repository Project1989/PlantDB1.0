from tkinter import Toplevel, Button, Label

class ConfirmRemovalView(Toplevel):
    
    def __init__(self, parent, element):
        super().__init__(parent)
        self.remove_element_state=False
        # Toplevel Titel
        self.title("Enferen von " + str(element) )
        #Label Wirklich entfernen
        label_ask_removel=Label(self, text="Wollen sie "+str(element)+" wirklich entfernen?")
        label_ask_removel.grid(column=0, row=0, columnspan=2)
        # Button Ja
        button_yes=Button(self, text="Ja", command=self._confirm_with_yes)
        button_yes.grid(column=0 ,row=1)
        # Button Nein
        button_no=Button(self, text="Nein", command=self._confirm_with_no)
        button_no.grid(column=1, row=1)
        
    def _confirm_with_yes(self):
        self.remove_element_state=True
        self.destroy()
            
    def _confirm_with_no(self):
        self.remove_element_state=False
        self.destroy()
    
    def get_confirmation_state(self)->bool:
        self.wait_window(self)
        return self.remove_element_state