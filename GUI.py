import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from Game_Core import GameCore

class GUI:
    def __init__(self):
        self.Game_obj = None
        self.person = None
        self.computer = None

        self.p1_img = None
        self.p2_img = None

        self.p1_image = None
        self.p1_image = None

        self.welcome()

    def welcome(self):
        def start_pvp():
            root.destroy()
            self.pvp_setup()

        def start_pvc():
            root.destroy()
            self.pvc_setup()

        root = tk.Tk()
        root.title("Connect 4")
        self.center_window(root, 1000, 800)
        root.config(bg="#A64D79")

        tk.Label(root, text="Welcome to Connect 4", fg="#1A1A1D", bg="#A64D79", font = ('Ink Free', 45, 'bold')).pack(pady=(20,70))

        self.person = tk.PhotoImage(file="Person.png")
        self.computer = tk.PhotoImage(file="Computer.png")

        frame_pvp = tk.Frame(root)
        frame_pvp.pack(pady=20)
        frame_pvp.config(bg="#A64D79")

        tk.Label(frame_pvp, bg="#A64D79", image = self.person).grid(row=0, column=0, padx=15)
        tk.Label(frame_pvp, fg="#1A1A1D", bg="#A64D79", text="VS", font = ('Ink Free', 30, 'bold')).grid(row=0, column=1, padx=15)
        tk.Label(frame_pvp, bg="#A64D79", image = self.person).grid(row=0, column=2, padx=15)

        tk.Button(root, bg="#6A1E55", fg="#A64D79", text="Player  vs  Player", font = ('Ink Free', 18, 'bold'), width = 18, command=start_pvp).pack(pady=(10,70))

        frame_pvc = tk.Frame(root)
        frame_pvc.pack(pady=20)
        frame_pvc.config(bg="#A64D79")

        tk.Label(frame_pvc, bg="#A64D79", image = self.person).grid(row=0, column=0, padx=15)
        tk.Label(frame_pvc, fg="#1A1A1D", bg="#A64D79", text="VS", font = ('Ink Free', 30, 'bold')).grid(row=0, column=1, padx=15)
        tk.Label(frame_pvc, bg="#A64D79", image = self.computer).grid(row=0, column=2, padx=15)

        tk.Button(root, bg="#6A1E55", fg="#A64D79", text="Player  vs  Computer", font = ('Ink Free', 18, 'bold'), width = 18, command=start_pvc).pack(pady=10)

        root.mainloop()

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')


    def pvp_setup(self):
        def start_game():
            p1_color = p1_color_var.get()
            p2_color = p2_color_var.get()

            if p1_color == 0 or p2_color == 0:
                error_label.config(text="Choose colors")
            elif p1_color == p2_color:
                error_label.config(text="Players must have different colors")
            else:
                root.destroy()
                if p1_color == 1:
                    p1 = "R"
                    p2 = "Y"
                    self.p1_img = "color2.png"
                    self.p2_img = "color1.png"
                else:
                    p1 = "Y"
                    p2 = "R"
                    self.p1_img = "color1.png"
                    self.p2_img = "color2.png"
                
                self.Game_obj = GameCore(p1, p2, False, None, None, None)
                self.Game(False)

        root = tk.Tk()
        root.title("Connect 4 - PvP")
        self.center_window(root, 1000, 800)
        root.config(bg="#A64D79")

        frame_pvp = tk.Frame(root)
        frame_pvp.pack(pady=60)
        frame_pvp.config(bg="#A64D79")

        self.person = tk.PhotoImage(file="Person.png")

        tk.Label(frame_pvp, bg="#A64D79", image = self.person).grid(row=0, column=0, padx=15)
        tk.Label(frame_pvp, bg="#A64D79", text="VS", font = ('Ink Free', 30, 'bold')).grid(row=0, column=1, padx=15)
        tk.Label(frame_pvp, bg="#A64D79", image = self.person).grid(row=0, column=2, padx=15)

        frame_p1 = tk.Frame(root)
        frame_p1.pack(pady=(80,35))
        frame_p1.config(bg="#A64D79")
        tk.Label(frame_p1, bg="#A64D79", text="Player 1 Color:", font = ('Ink Free', 30, 'bold')).grid(row=0, column=1, padx=15, pady=10)
        p1_color_var = tk.IntVar()
        tk.Radiobutton(frame_p1, bg="#A64D79", text="Red", variable = p1_color_var, value = 1,  font=('Ink Free', 20)).grid(row=0, column=2, padx=15)
        tk.Radiobutton(frame_p1, bg="#A64D79", text="Yellow", variable = p1_color_var, value = 2, font=('Ink Free', 20)).grid(row=0, column=3, padx=15)


        frame_p2 = tk.Frame(root)
        frame_p2.pack(pady=(35,60))
        frame_p2.config(bg="#A64D79")
        tk.Label(frame_p2, bg="#A64D79", text="Player 2 Color:", font = ('Ink Free', 30, 'bold')).grid(row=0, column=1, padx=15, pady=10)
        p2_color_var = tk.IntVar()
        tk.Radiobutton(frame_p2, bg="#A64D79", text="Red", variable = p2_color_var, value = 1, font=('Ink Free', 20)).grid(row=0, column=2, padx=15)
        tk.Radiobutton(frame_p2, bg="#A64D79", text="Yellow", variable = p2_color_var, value = 2, font=('Ink Free', 20)).grid(row=0, column=3, padx=15)

        error_label = tk.Label(root, bg="#A64D79", text="", font = ('Ink Free', 20, 'bold'))
        error_label.pack(pady=5)

        tk.Button(root, bg="#6A1E55", fg="#A64D79", text="Start Game", font = ('Ink Free', 20, 'bold'), command=start_game).pack(pady=20)

        root.mainloop()


    def pvc_setup(self):
        def start_game():
            player_color = player_color_var.get()
            algorithm = algorithm_var.get()
            computer_starts = computer_starts_var.get()

            if player_color == 0 or algorithm == 0 or computer_starts == 0:
                error_label.config(text="Fill in all fields")
            else:
                root.destroy()
                computer = False
                if player_color == 1:
                    if computer_starts == 1:
                        computer = True
                        p1 = "Y"
                        p2 = "R"
                        self.p1_img = "color1.png"
                        self.p2_img = "color2.png"
                    else:
                        p1 = "R"
                        p2 = "Y"
                        self.p1_img = "color2.png"
                        self.p2_img = "color1.png"
                else:
                    if computer_starts == 1:
                        computer = True
                        p1 = "R"
                        p2 = "Y"
                        self.p1_img = "color2.png"
                        self.p2_img = "color1.png"
                    else:
                        p1 = "Y"
                        p2 = "R"
                        self.p1_img = "color1.png"
                        self.p2_img = "color2.png"

                if algorithm == 1:
                    algo = "A"
                elif algorithm == 2:
                    algo = "B"
                else:
                    algo = "C"

                self.Game_obj = GameCore(p1, p2, True, computer, algo, 4)
                self.Game(computer)

        root = tk.Tk()
        root.title("Connect 4 - PvC")
        self.center_window(root, 1000, 800)
        root.config(bg="#A64D79")

        frame_pvc = tk.Frame(root)
        frame_pvc.pack(pady=60)
        frame_pvc.config( bg="#A64D79")

        self.person = tk.PhotoImage(file="Person.png")
        self.computer = tk.PhotoImage(file="Computer.png")

        tk.Label(frame_pvc, bg="#A64D79", image = self.person).grid(row=0, column=0, padx=15)
        tk.Label(frame_pvc, bg="#A64D79", text="VS", font = ('Ink Free', 30, 'bold')).grid(row=0, column=1, padx=15)
        tk.Label(frame_pvc, bg="#A64D79", image = self.computer).grid(row=0, column=2, padx=15)

        frame_1 = tk.Frame(root)
        frame_1.pack(pady=(40,20))
        frame_1.config( bg="#A64D79")
        tk.Label(frame_1, bg="#A64D79", text="Choose Your Color:", font = ('Ink Free', 30, 'bold')).grid(row=0, column=1, padx=15, pady=25)
        player_color_var = tk.IntVar()
        tk.Radiobutton(frame_1, bg="#A64D79", text="Red", variable = player_color_var, value = 1,  font=('Ink Free', 20)).grid(row=0, column=2, padx=15)
        tk.Radiobutton(frame_1, bg="#A64D79", text="Yellow", variable = player_color_var, value = 2, font=('Ink Free', 20)).grid(row=0, column=3, padx=15)
        
        tk.Label(frame_1, bg="#A64D79", text="Choose Algorithm:", font = ('Ink Free', 30, 'bold')).grid(row=1, column=1, padx=15, pady=25)
        algorithm_var = tk.IntVar()
        tk.Radiobutton(frame_1, bg="#A64D79", text="A", variable = algorithm_var, value = 1,  font=('Ink Free', 25, 'bold')).grid(row=1, column=2, padx=15)
        tk.Radiobutton(frame_1, bg="#A64D79", text="B", variable = algorithm_var, value = 2, font=('Ink Free', 25, 'bold')).grid(row=1, column=3, padx=15)
        tk.Radiobutton(frame_1, bg="#A64D79", text="C", variable = algorithm_var, value = 3, font=('Ink Free', 25, 'bold')).grid(row=1, column=4, padx=15)

        tk.Label(frame_1, bg="#A64D79", text="Computer Start?", font = ('Ink Free', 30, 'bold')).grid(row=3, column=1, padx=15, pady=25)
        computer_starts_var = tk.IntVar()
        tk.Radiobutton(frame_1, bg="#A64D79", text="Yes", variable = computer_starts_var, value = 1,  font=('Ink Free', 25, 'bold')).grid(row=3, column=2, padx=15)
        tk.Radiobutton(frame_1, bg="#A64D79", text="No", variable = computer_starts_var, value = 2, font=('Ink Free', 25, 'bold')).grid(row=3, column=3, padx=15)

        error_label = tk.Label(root, bg="#A64D79", text="", font = ('Ink Free', 20, 'bold'))
        error_label.pack(pady=5)

        tk.Button(root, bg="#6A1E55", fg="#A64D79", text="Start Game", font = ('Ink Free', 20, 'bold'), command=start_game).pack(pady=20)

        root.mainloop()

    def Game_over(self, winner, score):
        if winner == 1:
            text = "Player 1 won"
        elif winner == 2:
            text = "Player 2 won"
        else:
            text = "Draw"
        messagebox.showinfo("Game Over", str(text) + " with score = " + str(score))

    def on_label_click(self, event, index): 
        if self.Game_obj.Count_moves < 42:
                # for player vs player
                move, turn = self.Game_obj.Move(index)
                if move != -1:
                    if turn == 1:
                        self.labels[move].create_image(135 // 2, 123 // 2, image=self.p1_image, anchor="center")
                    else:
                        self.labels[move].create_image(135 // 2, 123 // 2, image=self.p2_image, anchor="center")
                    
                    if self.Game_obj.is_AI and self.Game_obj.Count_moves < 42:
                        # for AI vs player
                        AI_move = self.Game_obj.AI_Move()
                        if turn == 1:
                            self.labels[AI_move].create_image(135 // 2, 123 // 2, image=self.p2_image, anchor="center")
                        else:
                            self.labels[AI_move].create_image(135 // 2, 123 // 2, image=self.p1_image, anchor="center")


                    if self.Game_obj.Count_moves == 42:
                        self.Game_obj.Update_win_counts()
                        winner, score = self.Game_obj.Determine_winner()
                        self.Game_over(winner, score)

    def Game(self, computer):
        root = tk.Tk()
        root.title("Game")
        self.center_window(root, 1000, 800)
        root.config(bg="#1A1A1D")

        rows, cols = 6, 7
        self.labels = []

        self.p1_image = tk.PhotoImage(file = self.p1_img)
        self.p2_image = tk.PhotoImage(file = self.p2_img)

        for r in range(rows):
            for c in range(cols):
                canvas = tk.Canvas(root, width=135, height=123, bg="#6A1E55", highlightbackground="#3B1C32", relief="raised")
                canvas.grid(row=r, column=c, padx=2, pady=2)
                canvas.bind("<Button-1>", lambda event, index=c: self.on_label_click(event, index))
                self.labels.append(canvas)

        if computer:
            AI_move = self.Game_obj.AI_Move()
            self.labels[AI_move].create_image(135 // 2, 123 // 2, image=self.p1_image, anchor="center")

        root.mainloop()

Start = GUI()