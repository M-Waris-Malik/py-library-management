import tkinter as tk
from tkinter import messagebox

class library():
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        
        self.frame1=tk.Frame(self.root)
        self.frame1.pack(side=tk.TOP)
        
        self.frame2=tk.Frame(self.root)
        self.frame2.pack(side=tk.BOTTOM)
        
        self.book=tk.Label(self.frame1, text="Book Name:", font=("Arial",14))
        self.book.grid(row=0, column=0, pady=10)
        self.bookIn=tk.Entry(self.frame1, font=("Arial",14))
        self.bookIn.grid(row=0, column=1, pady=10)
        
        self.rollno=tk.Label(self.frame1, text="RollNo", font=("Arial",14))
        self.rollno.grid(row=0, column=2, pady=10)
        self.rollnoIn=tk.Entry(self.frame1, font=("Arial",14))
        self.rollnoIn.grid(row=0, column=3, pady=10)
        
        self.button=tk.Button(self.frame1, text="Search Book", font=("Arial",14), command=self.searchBook)
        self.button.grid(row=1, column=0, pady=15)
        
        self.list=tk.Listbox(self.frame2,width=80,height=30, font=("Arial",14), background="sky blue")
        self.list.grid(row=0, column=0, padx=10)
        
        self.books=[
            {"Book":"English"},
            {"Book":"Math"},
            {"Book":"Computer"}
        ]
        
        self.students=[
            {"RollNo":"101"},
            {"RollNo":"102"},
            {"RollNo":"103"}
        ]
        
    def searchBook(self):
        bname=self.bookIn.get()
        srn=self.rollnoIn.get() 
        
        bookFound=False
        rollnoFound=False
        for i in self.books:
            if bname==i["Book"]:
                bookFound=True
                self.clear()
                break
        if bookFound:
            for j in self.students:
                if srn==j["RollNo"]:
                    rollnoFound=True
                    allocate=f"Book {bname} allocated for student {srn}"
                    self.list.insert(tk.END,allocate)
                    self.clear()
            if not rollnoFound:
                self.clear() 
                tk.messagebox.showerror("Error", "Invalid Rollno")     
        if not bookFound:
            invalid= "Book Not Found"
            self.list.insert(tk.END,invalid)
            self.clear()
    def clear(self) :
        self.bookIn.delete(0,tk.END) 
        self.rollnoIn.delete(0,tk.END)    
    
root=tk.Tk()  
obj=library(root) 
root.mainloop() 
