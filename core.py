import tkinter as tk

class ShipDangerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ship Danger App")
        self.geometry("1080x720")
        self.attributes('-fullscreen', True)
        self.current_dangers = []
        self.history_dangers = []

        self.create_widgets()

    def create_widgets(self):
        # Static side view of the ship (Placeholder)
        ship_side_view = tk.Label(self, text="Static Side View of the Ship")
        ship_side_view.pack()

        # Deck schematic (Placeholder)
        deck_schematic = tk.Label(self, text="Deck Schematic (Changeable)")
        deck_schematic.pack()

        # List of current danger inputs
        current_dangers_label = tk.Label(self, text="Current Danger Inputs:")
        current_dangers_label.pack()

        self.current_dangers_listbox = tk.Listbox(self, width=30, height=10)
        self.current_dangers_listbox.pack()

        # Timer (Placeholder)
        self.timer_label = tk.Label(self, text="Timer: 00:00:00")
        self.timer_label.pack()

        # Clear all button
        clear_all_button = tk.Button(self, text="Clear All", command=self.clear_all)
        clear_all_button.pack()

    def add_danger(self, room, danger_type):
        # Add danger to the current dangers list
        danger_info = f"{room} - {danger_type}"
        self.current_dangers.append(danger_info)
        self.current_dangers_listbox.insert(tk.END, danger_info)

    def delete_danger(self, index):
        # Move the danger from current to history list
        danger_info = self.current_dangers.pop(index)
        self.current_dangers_listbox.delete(index)
        self.history_dangers.append(danger_info)

    def clear_all(self):
        # Clear all inputs and lists
        self.current_dangers.clear()
        self.history_dangers.clear()
        self.current_dangers_listbox.delete(0, tk.END)

if __name__ == "__main__":
    app = ShipDangerApp()
    app.mainloop()
