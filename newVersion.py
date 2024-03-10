import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


table = 0
update = 0
r = 10
c = 10
hor1stFlag = 1
next_button = None  # Define next_button as a global variable

class ToggleTable(tk.Frame):
    def __init__(self, parent, title, rows, columns):
        tk.Frame.__init__(self, parent)

        self.rows = rows 
        self.columns = columns 

        # Create the header row with fixed labels
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for j in range(1, columns + 1):  # Start from 1 and use correct index for letters
            label = tk.Label(self, text=letters[j - 1], borderwidth=1, relief="solid", width=3, height=1)
            label.grid(row=0, column=j)

        # Create the first column with fixed labels
        for i in range(rows):
            label = tk.Label(self, text=str(i + 1), borderwidth=1, relief="solid", width=3, height=1)
            label.grid(row=i + 1, column=0)

        # Create the rest of the table with toggling labels
        self.cells = [[0 for _ in range(columns)] for _ in range(rows)]
        self.labels = [[None for _ in range(columns)] for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                label = tk.Label(self, text=self.cells[i][j], borderwidth=1, relief="solid", width=3, height=1)
                label.grid(row=i + 1, column=j + 1)  # Offset by 1 to skip the fixed labels
                label.bind("<Button-1>", lambda event, i=i, j=j: self.toggle_cell(i, j))
                self.labels[i][j] = label

        self.update_button = tk.Button(self, text="Update", command=self.get_table, bg='green')
        self.update_button.grid(row=rows+1, columnspan=columns+1)  # Offset row by 1 for the button

    def toggle_cell(self, row, col):
        self.cells[row][col] = 1 - self.cells[row][col]
        self.update_table()

    def update_table(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.labels[i][j].config(text=self.cells[i][j])

    def get_table(self):
        global table
        global update
        table_data = [[''] + [chr(ord('A') + j) for j in range(self.columns)]]
        for i in range(self.rows):
            row_data = [str(i + 1)] + [str(self.cells[i][j]) for j in range(self.columns)]
            table_data.append(row_data)
        table = table_data
        update = 1
        self.update_button.config(state="disabled")  # Disable the button
        
class Table(tk.Frame):
    def __init__(self, parent, data, text_above_table="", rows=r, columns=c):
        tk.Frame.__init__(self, parent)
        global table



        # Create a list to hold the labels
        mat = list()
        self.cells = [[None for _ in range(columns+1)] for _ in range(rows+1)]
        for i in range(rows+1):
            line = list()
            for j in range(columns+1):
                if i==rows or j==columns:
                    txt=" "
                else:
                    txt = data[i][j]  
                line.append(txt)
            mat.append(line)
        #adding sum the list
        for i in range(1,rows):
            lineSum = 0
            for j in range(1,columns):   
                lineSum = int(lineSum) + int(mat[i][j])*pow(2,columns-j-1)     
            mat[i][columns] = lineSum 

            #arrange the list
        for i in range(1,rows-1):
            for j in range(1,columns-1):  
                if int(mat[j][columns]) < int(mat[j+1][columns]):      
                    temp = mat[j]
                    mat[j] = mat[j+1]
                    mat[j+1] = temp

            #pack the table
        for i in range(r+2):
            for j in range(c+2):
                label = tk.Label(root, text=str(mat[i][j]), borderwidth=1, relief="solid", width=3, height=1)
                label.place(x=285+j*25, y=240+i*18)
        table = mat
     
     

     
           
def check_update():
    global hor1stFlag
    global update
    global next_button
    if update:
        t1 = Table(root, table, "parts",r+1,c+1)
        t1.pack()
        update = 0
        next_button.pack(side=tk.RIGHT, anchor=tk.S, padx=10, pady=50)
        hor1stFlag +=1
        # Add text above the table
        label_above_table = tk.Label(root, text="Parts",bg='yellow')
        label_above_table.place(x=310,y=220)
        #add Notes
        NoteLabel = tk.Label(root, text="Row Sorting",bg="light blue",font=("Helvetica", 18))
        NoteLabel.place(x=50,y=325)

    if hor1stFlag ==2:
        next_button.config(command=firstHoz)
        hor1stFlag +=1
        print(hor1stFlag)

    root.after(1000, check_update)

def firstHoz():
    global hor1stFlag
    global next_button

    #remove the most right 
    for i in range(1,r+1):
        table[i+1][c+1] = ' '

    #put sum of colums
    line = [' ']
    for i in range(1,c):
        lineSum = 0
        for j in range(1,r-1):   
            lineSum = int(lineSum) + int(table[j][i])*pow(2,r-j-1)     
        line.append(lineSum) 
    table[r+1] = line

    #sort every col
    for k in range(1,c):
        for i in range(1,c):        

            for j in range(1,r+2):  
                if int(table[c][i]) < int(table[c][i+1]):      
                    temp = table[j-1][i]
                    table[j-1][i] = table[j-1][i+1]
                    table[j-1][i+1] = temp
            print(table[i])

    print("jiioj")
    for k in range(1,r+3):
            print(k,table[k-1])
    #pack the array
    """
    pack the array of label
    """
    for i in range(1,r+3):
        for j in range(c):
            label = tk.Label(root, text=str(table[i-1][j]), borderwidth=1, relief="solid", width=3, height=1)
            label.place(x=800+j*25, y=240+(i-1)*18)
            
    # put the title of the table
    tLabel = tk.Label(root, text="Parts",bg='yellow')
    tLabel.place(x=820,y=220)
    #add Notes
    NoteLabel = tk.Label(root, text="Column Sorting",bg="light blue",font=("Helvetica", 18))
    NoteLabel.place(x=600,y=325)
    #goto next function
    if hor1stFlag ==3:
        hor1stFlag += 1
        next_button.config(command=firstVert)
        print("Before config:", next_button.cget("command"))
        print(hor1stFlag)
    root.after(10, check_update)    

def firstVert():
    global hor1stFlag, next_button
    #remove the most bottom row 
    for i in range(1,c):
        table[r][i] = ' '
        
    #put sum of colums
    for i in range(1,r):
        lineSum = 0
        for j in range(1,c):   
            lineSum = int(lineSum) + int(table[i][j])*pow(2,c-j-1)     
        table[i][c] = lineSum 

    
     #arrange the list
    for i in range(1,r-1):
        for j in range(1,c-1):  
            if int(table[j][c]) < int(table[j+1][c]):      
                temp = table[j]
                table[j] = table[j+1]
                table[j+1] = temp

    """
    pack the array of label
    """
    for i in range(r):
        for j in range(c):
            label = tk.Label(root, text=str(table[i][j]), borderwidth=1, relief="solid", width=3, height=1)
            label.place(x=283+j*25, y=470+i*18)
        print(table[i])

    if hor1stFlag ==4:
        hor1stFlag += 1
        next_button.config(command=secondHor)
        print("After config:", next_button.cget("command"))
        print(hor1stFlag)
        
        
    #add Notes
    NoteLabel = tk.Label(root, text="Row Sorting",bg="light blue",font=("Helvetica", 18))
    NoteLabel.place(x=50,y=550)
    
    
    # put the title of the table
    tLabel = tk.Label(root, text="Parts",bg='yellow')
    tLabel.place(x=305,y=450)
    root.after(10, check_update)   

def secondHor():
    print("hello") 
    global hor1stFlag
    global next_button

    #remove the most right 
    for i in range(1,r):
        table[i][c] = ' '
        
    #put sum of colums
    line = [' ']
    for i in range(1,c):
        lineSum = 0
        for j in range(1,r-1):   
            lineSum = int(lineSum) + int(table[j][i])*pow(2,r-j-1)     
        line.append(lineSum) 
    table[r] = line
    
    #sort every col
    for k in range(1,c-1):
        for i in range(1,c-1):        

            for j in range(1,r+2):  
                if int(table[c][i]) < int(table[c][i+1]):      
                    temp = table[j-1][i]
                    table[j-1][i] = table[j-1][i+1]
                    table[j-1][i+1] = temp


    #pack the array
    """
    pack the array of label
    """
    for i in range(r+1):
        for j in range(c):
            label = tk.Label(root, text=str(table[i][j]), borderwidth=1, relief="solid", width=3, height=1)
            label.place(x=800+j*25, y=470+i*18)
            
    # put the title of the table
    tLabel = tk.Label(root, text="Parts",bg='yellow')
    tLabel.place(x=820,y=450)
    
    
    #add Notes
    NoteLabel = tk.Label(root, text="Coulmn Sorting",bg="light blue",font=("Helvetica", 18))
    NoteLabel.place(x=600,y=550)
    
    
    root.after(10, check_update)    


"""
************************
************************
**  main starts here  **
************************
************************
"""
root = tk.Tk()
root.title("Tkinter Table")
root.geometry("1280x800")
root.resizable(False, False)  # Disable resizing
messagebox.showinfo("Help", "Fill the table, then click update.\n the next button shows you the answer steps")

# Load the background image
image = Image.open("bg.jpg")
background_image = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0)



inLabel = tk.Label(root, text="Parts",bg='yellow')
inLabel.pack()
table = ToggleTable(root,"parts",r, c)
table.pack()    
next_button = tk.Button(root, text="Next", command=firstHoz, width=20, height=2, bg='green')



check_update()
root.mainloop()
