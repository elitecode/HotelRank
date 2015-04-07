from Tkinter import *
import ttk
import os,json 
root = Tk()
root.geometry("1000x700")
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

tree = ttk.Treeview(root)
tree["columns"]=("one","two","three")
tree.column("one", width=200 )
tree.column("two", width=200)
tree.column("three", width=200)

tree.heading("one", text="hotelRating")
tree.heading("two", text="tripAdvisorRating")
tree.heading("three",text="SentimentRating")

filePath=os.getcwd()+'/final.json'
fi=open(filePath)
js=json.load(fi)

for i in range(len(js)):
	tree.insert("" , 0,    text=js[i]['name'], values=(js[i]['hotelRating'],js[i]['tripAdvisorRating'],js[i]['rating']))
 
tree.pack(side = LEFT, fill = BOTH )
tree.config(yscrollcommand=scrollbar.set)
scrollbar.config( command = tree.yview )
root.mainloop()