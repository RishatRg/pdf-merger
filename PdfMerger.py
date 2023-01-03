#!/usr/local/bin/python

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from PyPDF2 import PdfMerger

# from tkinter import ttk
window = Tk()

def click():
    window.destroy()


# Скрываем главное окно за ненадобностью
window.withdraw()
         
pdfs = list()
counter = 0
while True:
    selected_pdfs = filedialog.askopenfilenames(title=f"PDF merge, {counter} file(s) were selected",
                                                   filetypes=[("PDF files", '.pdf')]) 
    if not selected_pdfs:
        break

    pdfs.extend(selected_pdfs)
    # Увеличиваем счётчик на количество файлов выбранных в текущей итерации
    counter += len(selected_pdfs)

with PdfMerger() as merger:
    for pdf in pdfs:
        merger.append(pdf)

    filename_to_save = filedialog.asksaveasfilename(
                            title=f"Merge {counter} pdfs to: ",
                            defaultextension=('.pdf'),
                            filetypes=[("PDF files", '.pdf')])

    if filename_to_save:
        merger.write(filename_to_save)

        window.title(f"Done!")
        window.geometry("150x40")

        btn = ttk.Button(text="OK", command=click)
        btn.pack(anchor=CENTER, padx=6, pady=6)
        
        window.eval('tk::PlaceWindow . center')
        window.deiconify()
        window.mainloop()
