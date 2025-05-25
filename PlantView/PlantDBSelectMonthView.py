from tkinter import Toplevel, Checkbutton, Label, IntVar, Button, Tk
class SelectMonthWindow():
    def __init__(self, update_pruning_month):
        self.select_month_window=Toplevel()
        self.select_month_window.title("Monatswahl")
        self.update_pruning_month=update_pruning_month
        
        self.jan_checked=IntVar()
        self.feb_checked=IntVar()
        self.mar_checked=IntVar()
        self.apr_checked=IntVar()
        self.may_checked=IntVar()
        self.jun_checked=IntVar()
        self.jul_checked=IntVar()
        self.aug_checked=IntVar()
        self.sep_checked=IntVar()
        self.oct_checked=IntVar()
        self.nov_checked=IntVar()
        self.dec_checked=IntVar()
        
        label_info=Label(self.select_month_window, text="Auswahl der Monate für den Rückschnitt.")
        label_info.grid(row=0)
        cb_jan=Checkbutton(self.select_month_window, text="Januar", variable=self.jan_checked )
        cb_jan.grid(row=1, sticky="W")
        cb_feb=Checkbutton(self.select_month_window, text="Februar", variable=self.feb_checked)
        cb_feb.grid(row=2, sticky="W")
        cb_mar=Checkbutton(self.select_month_window, text="März", variable=self.mar_checked)
        cb_mar.grid(row=3, sticky="W")
        cb_apr=Checkbutton(self.select_month_window, text="April", variable=self.apr_checked)
        cb_apr.grid(row=4, sticky="W")
        cb_may=Checkbutton(self.select_month_window, text="Mai", variable=self.may_checked)
        cb_may.grid(row=5, sticky="W")
        cb_jun=Checkbutton(self.select_month_window, text="Juni", variable=self.jun_checked)
        cb_jun.grid(row=6, sticky="W")
        cb_jul=Checkbutton(self.select_month_window, text="Juli", variable=self.jul_checked)
        cb_jul.grid(row=7, sticky="W")
        cb_aug=Checkbutton(self.select_month_window, text="August", variable=self.aug_checked)
        cb_aug.grid(row=8, sticky="W")
        cb_sep=Checkbutton(self.select_month_window, text="September", variable=self.sep_checked)
        cb_sep.grid(row=9, sticky="W")
        cb_oct=Checkbutton(self.select_month_window, text="Oktober", variable=self.oct_checked)
        cb_oct.grid(row=10, sticky="W")
        cb_nov=Checkbutton(self.select_month_window, text="November", variable=self.nov_checked)
        cb_nov.grid(row=11, sticky="W")
        cb_dec=Checkbutton(self.select_month_window, text="Dezember", variable=self.dec_checked)
        cb_dec.grid(row=12, sticky="W")
        
        button_confirm=Button(self.select_month_window, text="Auswählen", command=self.press_check_button_month)
        button_confirm.grid(row=13,column=0, sticky="W")
        button_cancel=Button(self.select_month_window, text="Abbrechen", command=self.select_month_window.destroy)
        button_cancel.grid(row=13,column=1, sticky="W")
        
    def press_check_button_month(self):
        checked_month_dict={
            "Januar": self.jan_checked.get(),
            "Februar": self.feb_checked.get(),
            "März": self.mar_checked.get(),
            "April": self.apr_checked.get(),
            "Mai": self.may_checked.get(),
            "Juni": self.jun_checked.get(),
            "Juli": self.jul_checked.get(),
            "August": self.aug_checked.get(),
            "September": self.sep_checked.get(),
            "Oktober": self.oct_checked.get(),
            "November": self.nov_checked.get(),
            "Dezember": self.dec_checked.get()
        }
        self.update_pruning_month(checked_month_dict)
        self.select_month_window.destroy()
        
      