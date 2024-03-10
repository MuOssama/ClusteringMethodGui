import tkinter as tk
table = 0
class ToggleTable(tk.Frame):
    def __init__(self, parent, rows=5, columns=5):
        tk.Frame.__init__(self, parent)

        self.rows = rows
        self.columns = columns

        self.cells = [[0 for _ in range(columns)] for _ in range(rows)]
        self.labels = [[None for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                label = tk.Label(self, text=self.cells[i][j], borderwidth=1, relief="solid", width=5, height=2)
                label.grid(row=i, column=j)
                label.bind("<Button-1>", lambda event, i=i, j=j: self.toggle_cell(i, j))
                self.labels[i][j] = label

        self.update_button = tk.Button(self, text="Update", command=self.get_table)
        self.update_button.grid(row=rows, columns=columns)
        print(self.cells)

    def toggle_cell(self, row, col):
        self.cells[row][col] = 1 - self.cells[row][col]
        self.update_table()

    def update_table(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.labels[i][j].config(text=self.cells[i][j])

    def get_table(self):
        global table
        print(self.cells)
        table=self.cells

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Toggle Table")
    table = ToggleTable(root, rows=5, columns=5)
    table.pack(pady=10, padx=10)
    print(table)
    root.mainloop()
