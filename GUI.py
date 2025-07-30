import tkinter as tk
from tkinter import ttk, messagebox
from Books import initialize_driver, search_books, print_books

class BookScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Goodreads Book Scraper")
        self.root.geometry("400x300")
        self.driver = initialize_driver()  
        self.books_list = []  

        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(main_frame, text="Enter Book Category:").grid(row=0, column=0, padx=5, pady=5)
        self.category_entry = ttk.Entry(main_frame, width=30)
        self.category_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(main_frame, text="Search Books", command=self.search).grid(row=1, column=0, columnspan=2, pady=20)
        ttk.Button(main_frame, text="Save to CSV", command=self.save_csv).grid(row=2, column=0, columnspan=2, pady=10)
        ttk.Button(main_frame, text="Exit", command=self.on_closing).grid(row=3, column=0, columnspan=2, pady=10)

        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)


    def search(self):
        category = self.category_entry.get().strip()
        if not category:
            messagebox.showwarning("Warning", "Please enter a book category")
            return
        
        self.status_label.config(text="Searching... Please wait")
        self.root.update()
        
        try:
            self.books_list = search_books(self.driver, category)  
            self.status_label.config(text=f"Found {len(self.books_list)} books")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Error occurred during search")

    def save_csv(self):
        if not self.books_list:
            messagebox.showwarning("Warning", "No books to save! Please search first.")
            return
        
        try:
            print_books(self.books_list)  
            messagebox.showinfo("Success", "Books saved to CSV file successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save CSV: {str(e)}")

    def on_closing(self):
        try:
            self.driver.quit()  
        except:
            pass
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BookScraperGUI(root)
    root.mainloop()