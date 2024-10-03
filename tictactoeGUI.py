import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.turn = 'X'
        self.board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                      'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                      'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
        self.buttons = {}
        self.create_buttons()
        
    def create_buttons(self):
        for position in self.board.keys():
            button = tk.Button(self.master, text=' ', font=('Arial', 40), width=5, height=2,
                               command=lambda pos=position: self.make_move(pos))
            button.grid(row=self.get_row(position), column=self.get_col(position))
            self.buttons[position] = button

    def get_row(self, position):
        return {'top-L': 0, 'top-M': 0, 'top-R': 0,
                'mid-L': 1, 'mid-M': 1, 'mid-R': 1,
                'low-L': 2, 'low-M': 2, 'low-R': 2}[position]

    def get_col(self, position):
        return {'top-L': 0, 'top-M': 1, 'top-R': 2,
                'mid-L': 0, 'mid-M': 1, 'mid-R': 2,
                'low-L': 0, 'low-M': 1, 'low-R': 2}[position]

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.turn
            self.buttons[position].config(text=self.turn)
            if self.check_winner(self.turn):
                messagebox.showinfo("Ganador", f"Ganó {self.turn}!")
                self.reset_game()
            if self.tableroLleno():
                messagebox.showinfo("Empate", "Empate!")
                self.reset_game
            self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self, ficha):
        winning_combinations = [
            ("top-L", "top-M", "top-R"),
            ("mid-L", "mid-M", "mid-R"),
            ("low-L", "low-M", "low-R"),
            ("top-L", "mid-L", "low-L"),
            ("top-M", "mid-M", "low-M"),
            ("top-R", "mid-R", "low-R"),
            ("top-L", "mid-M", "low-R"),
            ("top-R", "mid-M", "low-L"),
        ]
        return any(all(self.board[pos] == ficha for pos in combo) for combo in winning_combinations)

    def reset_game(self):
        for position in self.board.keys():
            self.board[position] = ' '
            self.buttons[position].config(text=' ')
        self.turn = 'X'
    
    def tableroLleno(self):
        return all(space != ' ' for space in self.board.values())

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
