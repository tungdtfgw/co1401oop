from tkinter import *   
from tkinter import messagebox as mb

from gui_base import GUIBase
import csv

class StudentListApp(GUIBase):
    def __init__(self):
        super().__init__(title="Student List", width=555, height=450)

    def _create_widgets(self):
        lbl_title = Label(self._window, text="Student List")
        lbl_title.grid(row=0, column=0, padx=5, pady=5, columnspan=6, sticky=EW)

        lbl_search = Label(self._window, text="Search:")
        lbl_search.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        txt_search = Entry(self._window)
        txt_search.grid(row=1, column=1, padx=5, pady=5, sticky=E)

        lst_students = Listbox(self._window, width=30, height=15)
        lst_students.grid(row=2, column=0, columnspan=2, rowspan=4, padx=5, pady=5, sticky=W)

        btn_import = Button(self._window, text="Import")
        btn_import.grid(row=6, column=0, padx=5, pady=5, sticky=W)

        btn_export = Button(self._window, text="Export")
        btn_export.grid(row=6, column=1, padx=5, pady=5, sticky=E)

        lbl_id = Label(self._window, text="ID:")
        lbl_id.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        txt_id = Entry(self._window)
        txt_id.grid(row=2, column=3, padx=5, pady=5, columnspan=3, sticky=E)

        lbl_name = Label(self._window, text="Name:")
        lbl_name.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        txt_name = Entry(self._window)
        txt_name.grid(row=3, column=3, padx=5, pady=5, columnspan=3, sticky=E)

        lbl_age = Label(self._window, text="Age:")
        lbl_age.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        txt_age = Entry(self._window)
        txt_age.grid(row=4, column=3, padx=5, pady=5, columnspan=3, sticky=E)

        lbl_gpa = Label(self._window, text="GPA:")
        lbl_gpa.grid(row=5, column=2, padx=5, pady=5, sticky=W)

        txt_gpa = Entry(self._window)
        txt_gpa.grid(row=5, column=3, padx=5, pady=5, columnspan=3, sticky=E)

        btn_add = Button(self._window, text="Add")
        btn_add.grid(row=6, column=3, padx=5, pady=5, sticky=W)

        btn_save = Button(self._window, text="Save")
        btn_save.grid(row=6, column=4, padx=5, pady=5, sticky=E)

        btn_del = Button(self._window, text="Del")
        btn_del.grid(row=6, column=5, padx=5, pady=5, sticky=E)



if __name__ == "__main__":
    app = StudentListApp()
    app.run()