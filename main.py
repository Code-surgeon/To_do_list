import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("My To-Do List by")

def add_task():
    task = entries.get()
    if task != "":
        lbTasks.insert(tkinter.END, task)
        entries.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Enter a task.")

def delete_task():
    try:
        task_index =  lbTasks.curselection()[0]
        lbTasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Select a task.")



def save_tasks():
    tasks =  lbTasks.get(0,  lbTasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
    
    
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        lbTasks.delete(0, tkinter.END)
        for task in tasks:
            lbTasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")
        
def help_user():
    lbTasks.delete(0, tkinter.END)
    with open("program summary.txt", "rb") as f:
       for line in f:
        # add the line to the list box
        lbTasks.insert(tkinter.END, line.strip())
        
def reset():
    lbTasks.delete(0, tkinter.END)
            
        
        
   
    
        

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

#creates listbox
lbTasks = tkinter.Listbox(frame_tasks, height=10, width=90)
lbTasks.pack(side=tkinter.LEFT)

scroll = tkinter.Scrollbar(frame_tasks)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#creates a vertical scroll bar
lbTasks.config(yscrollcommand=scroll.set)
scroll.config(command= lbTasks.yview)

lbTasks.config(xscrollcommand=scroll.set)
scroll.config(command= lbTasks.xview)

#descriptive label
description= tkinter.Label(root, text="Enter task in this field")
description.pack()

#text field on which user can enter task
entries = tkinter.Entry(root, width=50)
entries.pack()

#the respective buttons are created
btnAdd = tkinter.Button(root, text="Add task", width=15, command=add_task)
btnAdd.pack()

btnDelete = tkinter.Button(root, text="Delete task", width=15, command=delete_task)
btnDelete.pack()

btnLoad = tkinter.Button(root, text="Load tasks", width=15, command=load_tasks)
btnLoad.pack()

btnSave = tkinter.Button(root, text="Save tasks", width=15, command=save_tasks)
btnSave.pack()

btnHelp =tkinter.Button(root, text="help", width=15, command= help_user)
btnHelp.pack()

btnReset=tkinter.Button(root, text="reset", width= 15, command= reset)
btnReset.pack()


root.mainloop()