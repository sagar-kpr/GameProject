from tkinter import Frame, Label, CENTER

import Logics
import cons as c


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        self.commands = {c.key_up: Logics.move_up, c.key_down: Logics.move_down,
                         c.key_left: Logics.move_left, c.key_right: Logics.move_right
                         }

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.background_of_game,
                           width=c.size, height=c.size)
        background.grid()

        for i in range(c.grid_len):
            grid_row = []
            for j in range(c.grid_len):
                cell = Frame(background, bg=c.background_empty_cell,
                             width=c.size / c.grid_len,
                             height=c.size / c.grid_len)
                cell.grid(row=i, column=j, padx=c.padding,
                          pady=c.padding)
                t = Label(master=cell, text="",
                          bg=c.background_empty_cell,
                          justify=CENTER, font=c.font, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = Logics.start_game()
        Logics.add_nbr(self.matrix)
        Logics.add_nbr(self.matrix)

    def update_grid_cells(self):
        for i in range(c.grid_len):
            for j in range(c.grid_len):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.background_empty_cell)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.background_color_cell[new_number],
                        fg=c.text_color[new_number])
        self.update_idletasks()

    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                Logics.add_nbr(self.matrix)
                self.update_grid_cells()
                changed = False
                if Logics.status_of_game(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.background_empty_cell)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.background_empty_cell)

                if Logics.status_of_game(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.background_empty_cell)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.background_empty_cell)


gamegrid = Game2048()
