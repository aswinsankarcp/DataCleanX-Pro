import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import csv_cleaner
import docx_cleaner
import report_generator
import matplotlib.pyplot as plt
import seaborn as sns


class DataCleanXApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DataCleanX Pro")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="DataCleanX Pro", font=("Helvetica", 18))
        title.pack(pady=20)

        # CSV File Selection
        self.csv_label = tk.Label(self.root, text="No CSV file selected")
        self.csv_label.pack(pady=5)

        csv_button = tk.Button(self.root, text="Select CSV File", command=self.select_csv)
        csv_button.pack(pady=5)

        # DOCX File Selection
        self.docx_label = tk.Label(self.root, text="No DOCX file selected")
        self.docx_label.pack(pady=5)

        docx_button = tk.Button(self.root, text="Select DOCX File", command=self.select_docx)
        docx_button.pack(pady=5)

        # Clean Files Button
        clean_button = tk.Button(self.root, text="Clean Files", command=self.clean_files)
        clean_button.pack(pady=20)

        # Generate Report Button
        report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        report_button.pack(pady=5)

    def select_csv(self):
        self.csv_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.csv_path:
            self.csv_label.config(text=self.csv_path)

    def select_docx(self):
        self.docx_path = filedialog.askopenfilename(filetypes=[("DOCX Files", "*.docx")])
        if self.docx_path:
            self.docx_label.config(text=self.docx_path)

    def clean_files(self):
        if hasattr(self, 'csv_path'):
            self.cleaned_csv_path = csv_cleaner.clean_csv(self.csv_path)
        if hasattr(self, 'docx_path'):
            self.cleaned_docx_path = docx_cleaner.clean_docx(self.docx_path)
        messagebox.showinfo("Success", "Files cleaned successfully!")

    def generate_report(self):
        if hasattr(self, 'cleaned_csv_path') and hasattr(self, 'cleaned_docx_path'):
            report_path = report_generator.generate_report(self.cleaned_csv_path, self.cleaned_docx_path)
            messagebox.showinfo("Report Generated", f"Report saved as: {report_path}")
            self.show_csv_summary(self.cleaned_csv_path)

    def show_csv_summary(self, csv_path):
        summary = csv_cleaner.generate_csv_summary(csv_path)
        plt.figure(figsize=(10, 4))
        sns.heatmap(summary.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

    def run(self):
        self.root.mainloop()
