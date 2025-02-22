import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Dict, List
import json
import re
from ttkthemes import ThemedTk
from PIL import Image, ImageTk, ImageDraw, ImageFont

class ToppingOptimizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Run: Kingdom Topping Optimizer")
        self.root.geometry("900x1000")
        
        # Cookie Run color scheme
        self.colors = {
            'background': '#291711',     # Darker brown
            'frame': '#3D2318',          # Medium brown
            'text': '#FFE6D5',           # Warm white
            'accent': '#FF9ECD',         # Soft pink
            'button': '#8B4513',         # Button brown
            'button_hover': '#A0522D'    # Lighter button brown
        }
        
        # Configure root
        self.root.configure(bg=self.colors['background'])
        
        # Configure styles
        style = ttk.Style()
        
        # Frame styles
        style.configure(
            "Cookie.TFrame",
            background=self.colors['background']
        )
        
        style.configure(
            "Inner.TFrame",
            background=self.colors['frame']
        )
        
        # Label styles
        style.configure(
            "Title.TLabel",
            font=("Comic Sans MS", 24, "bold"),
            foreground=self.colors['accent'],
            background=self.colors['background']
        )
        
        style.configure(
            "Header.TLabel",
            font=("Comic Sans MS", 14),
            foreground=self.colors['text'],
            background=self.colors['frame']
        )
        
        # Main container with padding
        main_frame = ttk.Frame(root, style="Cookie.TFrame", padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Title
        title_frame = ttk.Frame(main_frame, style="Cookie.TFrame")
        title_frame.pack(pady=(0, 20))
        
        # Create a rounded rectangle background for the title
        title_bg = self.create_rounded_rectangle(400, 80, self.colors['frame'])
        title_bg_label = ttk.Label(title_frame, image=title_bg)
        title_bg_label.image = title_bg
        title_bg_label.pack(pady=10)
        
        title_label = ttk.Label(
            title_frame,
            text="Cookie Run: Kingdom\nTopping Optimizer",
            style="Title.TLabel",
            justify="center"
        )
        title_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Cookie selection
        cookie_frame = self.create_section_frame(main_frame, "Choose Your Cookie")
        
        self.cookie_var = tk.StringVar()
        self.cookie_dropdown = ttk.Combobox(
            cookie_frame,
            textvariable=self.cookie_var,
            values=[
                "Black Sapphire",
                "Ferret",
                "Rebel",
                "Twizzly",
                "Pinecone",
                "Dark Choco",
                "Crème Brûlée",
                "Candy Apple",
                "Mint Choco",
                "Mystic Flower",
                "Palm Cookie"
            ],
            state="readonly",
            width=30
        )
        self.cookie_dropdown.pack(pady=10)
        
        # Topping management
        topping_frame = self.create_section_frame(main_frame, "Topping Management")
        
        # Button container
        button_frame = ttk.Frame(topping_frame, style="Inner.TFrame")
        button_frame.pack(fill="x", pady=10)
        
        buttons = [
            ("🗂️ Import", self.import_toppings),
            ("➕ Add", self.add_topping),
            ("📝 Parse", self.parse_raw_toppings)
        ]
        
        for text, command in buttons:
            self.create_custom_button(button_frame, text, command)
        
        # Text input
        input_label = ttk.Label(
            topping_frame,
            text="Paste your toppings data here:",
            style="Header.TLabel"
        )
        input_label.pack(anchor="w", pady=(10, 5))
        
        self.raw_text = tk.Text(
            topping_frame,
            height=10,
            font=("Consolas", 11),
            wrap="word",
            bg=self.colors['background'],
            fg=self.colors['text'],
            insertbackground=self.colors['text']
        )
        self.raw_text.pack(fill="both", expand=True, pady=5)
        
        # Optimize button
        optimize_frame = ttk.Frame(main_frame, style="Cookie.TFrame")
        optimize_frame.pack(pady=20)
        self.create_custom_button(
            optimize_frame,
            "✨ Find Best Combinations ✨",
            self.optimize,
            large=True
        )
        
        # Results
        results_frame = self.create_section_frame(main_frame, "Results")
        
        self.results_text = tk.Text(
            results_frame,
            height=15,
            font=("Consolas", 11),
            wrap="word",
            bg=self.colors['background'],
            fg=self.colors['text'],
            insertbackground=self.colors['text']
        )
        self.results_text.pack(fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.results_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.results_text.configure(yscrollcommand=scrollbar.set)

    def create_rounded_rectangle(self, width, height, color):
        """Create a rounded rectangle background"""
        image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle(
            [(0, 0), (width-1, height-1)],
            radius=20,
            fill=color
        )
        return ImageTk.PhotoImage(image)

    def create_section_frame(self, parent, title):
        """Create a section frame with rounded corners and title"""
        frame = ttk.Frame(parent, style="Inner.TFrame", padding=15)
        frame.pack(fill="x", padx=5, pady=5)
        
        title_label = ttk.Label(
            frame,
            text=title,
            style="Header.TLabel"
        )
        title_label.pack(anchor="w", pady=(0, 10))
        
        return frame

    def create_custom_button(self, parent, text, command, large=False):
        """Create a custom styled button"""
        button_frame = ttk.Frame(parent, style="Inner.TFrame")
        button_frame.pack(side="left", padx=5)
        
        width = 200 if large else 100
        height = 40 if large else 30
        
        bg = self.create_rounded_rectangle(width, height, self.colors['button'])
        hover_bg = self.create_rounded_rectangle(width, height, self.colors['button_hover'])
        
        button = tk.Label(
            button_frame,
            text=text,
            font=("Comic Sans MS", 12 if large else 10),
            fg=self.colors['text'],
            image=bg,
            compound="center"
        )
        button.image = bg
        button.hover_image = hover_bg
        button.pack()
        
        def on_enter(e):
            button.configure(image=button.hover_image)
            
        def on_leave(e):
            button.configure(image=button.image)
            
        def on_click(e):
            command()
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_click)

    def parse_raw_toppings(self):
        raw_data = self.raw_text.get("1.0", tk.END).strip()
        if not raw_data:
            messagebox.showerror("Error", "Please paste some topping data first")
            return
            
        try:
            # Split the data into lines and clean them
            lines = [line.strip() for line in raw_data.split('\n') if line.strip()]
            parsed_toppings = []
            
            for line in lines:
                # Skip lines that don't look like topping data
                if not line.startswith("{'type':"): continue
                
                try:
                    # Convert the string representation of dict to actual dict
                    # Using eval() here is safe because we know the exact format
                    topping = eval(line.rstrip(','))
                    parsed_toppings.append(topping)
                except:
                    continue
            
            if not parsed_toppings:
                messagebox.showerror("Error", "No valid topping data found")
                return
            
            self.toppings = parsed_toppings
            messagebox.showinfo("Success", f"Successfully parsed {len(parsed_toppings)} toppings")
            
            # Clear the text field
            self.raw_text.delete("1.0", tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to parse toppings: {str(e)}\n\nMake sure you've pasted the topping data correctly")
            return

    def import_toppings(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    self.toppings = json.load(f)
                messagebox.showinfo("Success", f"Imported {len(self.toppings)} toppings")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def add_topping(self):
        # Create a new window for topping input
        topping_window = tk.Toplevel(self.root)
        topping_window.title("Add New Topping")
        
        # Add input fields for each stat
        fields = ['type', 'ATK', 'ATK_SPD', 'Crit', 'Cooldown', 'DMG_Resist']
        entries = {}
        
        for field in fields:
            frame = ttk.Frame(topping_window)
            frame.pack(padx=5, pady=2)
            ttk.Label(frame, text=field).pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="right")
            entries[field] = entry
            
        def save_topping():
            try:
                topping = {
                    'type': entries['type'].get(),
                    'ATK': float(entries['ATK'].get() or 0),
                    'ATK_SPD': float(entries['ATK_SPD'].get() or 0),
                    'Crit': float(entries['Crit'].get() or 0),
                    'Cooldown': float(entries['Cooldown'].get() or 0),
                    'DMG_Resist': float(entries['DMG_Resist'].get() or 0)
                }
                self.toppings.append(topping)
                topping_window.destroy()
                messagebox.showinfo("Success", "Topping added successfully")
            except ValueError as e:
                messagebox.showerror("Error", "Please enter valid numbers for stats")
                
        ttk.Button(topping_window, text="Save", command=save_topping).pack(pady=10)

    def optimize(self):
        if not self.toppings:
            messagebox.showerror("Error", "Please add some toppings first")
            return
            
        cookie = self.cookie_var.get()
        if not cookie:
            messagebox.showerror("Error", "Please select a cookie")
            return
            
        # Convert cookie name to module name
        module_map = {
            "Black Sapphire": "black",
            "Ferret": "ferret",
            "Rebel": "rebel",
            "Twizzly": "twizzly",
            "Pinecone": "pinecone",
            "Dark Choco": "choco",
            "Crème Brûlée": "brulee",
            "Candy Apple": "capple",
            "Mint Choco": "mint",
            "Mystic Flower": "mystic",
            "Palm Cookie": "palm"
        }
        
        try:
            # Get the correct module name
            module_name = module_map.get(cookie)
            if not module_name:
                raise ValueError(f"No optimizer found for {cookie}")
            
            # Import and run the optimizer
            import importlib.util
            import sys
            import os
            
            # Get the absolute path to the optimizations directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            module_path = os.path.join(parent_dir, "optimizations", f"{module_name}.py")
            
            if not os.path.exists(module_path):
                raise FileNotFoundError(f"Optimizer file not found: {module_path}")
            
            # Import the module
            spec = importlib.util.spec_from_file_location(f"optimizations.{module_name}", module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module
            spec.loader.exec_module(module)
            
            # Run the optimization
            results = module.main(self.toppings)
            self.display_results(results)
            
        except Exception as e:
            messagebox.showerror("Error", f"Optimization failed: {str(e)}")
            import traceback
            traceback.print_exc()  # This will print the full error to console
            
    def display_results(self, results):
        # Clear previous results
        self.results_text.delete("1.0", tk.END)
        # Insert new results
        self.results_text.insert("1.0", results)

def main():
    root = ThemedTk(theme="arc")
    app = ToppingOptimizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 