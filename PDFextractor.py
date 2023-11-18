import tkinter as tk
from tkinter import filedialog
import PyPDF2

root = tk.Tk()
root.title("PDF text extractor")

filename_label = tk.Label(root, text="No File Selected")
filename_label.pack()
outputfile_text = tk.Text(root)
outputfile_text.pack()

# functions

def openFile():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    filename_label.configure(text=filename)
    outputfile_text.delete("1.0", tk.END)

    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)): # loop through a number of pages
        current_text = reader.pages[i].extract_text()
        outputfile_text.insert(tk.END, current_text)


# buttons

openfile_button = tk.Button(root, text="Open PDF file", command=openFile)
openfile_button.pack()
filename_label.pack()

root.mainloop()