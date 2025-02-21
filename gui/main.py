import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Dict, List
import json
import re

class ToppingOptimizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Run: Kingdom Topping Optimizer")
        self.toppings = []
        
        # Cookie selection
        self.cookie_frame = ttk.LabelFrame(root, text="Cookie Selection")
        self.cookie_frame.pack(padx=10, pady=5, fill="x")
        
        self.cookie_var = tk.StringVar()
        self.cookie_dropdown = ttk.Combobox(
            self.cookie_frame, 
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
            ]
        )
        self.cookie_dropdown.pack(padx=5, pady=5)
        
        # Topping input
        self.topping_frame = ttk.LabelFrame(root, text="Topping Management")
        self.topping_frame.pack(padx=10, pady=5, fill="x")
        
        # Buttons frame
        button_frame = ttk.Frame(self.topping_frame)
        button_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Button(
            button_frame,
            text="Import from File",
            command=self.import_toppings
        ).pack(side="left", padx=5)
        
        ttk.Button(
            button_frame,
            text="Add Single Topping",
            command=self.add_topping
        ).pack(side="left", padx=5)
        
        ttk.Button(
            button_frame,
            text="Parse Pasted Data",
            command=self.parse_raw_toppings
        ).pack(side="left", padx=5)
        
        # Raw text input
        ttk.Label(self.topping_frame, text="Paste toppings data here:").pack(padx=5, pady=(10,0), anchor="w")
        self.raw_text = tk.Text(self.topping_frame, height=10)
        self.raw_text.pack(padx=5, pady=5, fill="both")
        
        # Optimize button
        ttk.Button(
            root,
            text="Find Best Combinations",
            command=self.optimize
        ).pack(padx=10, pady=10)
        
        # Results area
        self.results_frame = ttk.LabelFrame(root, text="Results")
        self.results_frame.pack(padx=10, pady=5, fill="both", expand=True)
        
        self.results_text = tk.Text(self.results_frame, height=20)
        self.results_text.pack(padx=5, pady=5, fill="both", expand=True)

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
    root = tk.Tk()
    app = ToppingOptimizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 