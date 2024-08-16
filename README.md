

# DataCleanX Pro

**DataCleanX Pro** is a powerful and user-friendly data cleaning tool built with Python. It allows you to clean CSV and DOCX files, generate detailed reports, and visualize data through a graphical user interface (GUI). This project utilizes various Python libraries to handle data manipulation, text processing, and visualization.

## Features

- **CSV Cleaning:**
  - Handle missing values, duplicate rows, and standardize column names.
  - Generate summary statistics for the cleaned CSV files.
  - Visualize data correlations with heatmaps.

- **DOCX Cleaning:**
  - Normalize text formatting and remove unnecessary whitespace.
  - Clean and process DOCX files for better readability.

- **Report Generation:**
  - Automatically generate a detailed DOCX report summarizing the cleaning process.
  - Include charts and visualizations to enhance the report.

- **Graphical User Interface (GUI):**
  - Intuitive GUI built with `tkinter` for easy file selection and cleaning.
  - View summary statistics and visualizations directly within the application.

## Tools and Libraries

- **CSV Handling:**
  - `pandas`: For reading and cleaning CSV files.
  - `numpy`: For handling missing values and performing numerical operations.

- **DOCX Handling:**
  - `python-docx`: For reading, cleaning, and writing DOCX files.

- **General Utilities:**
  - `re`: For regular expressions to clean text data.
  - `tkinter`: For GUI development.
  - `matplotlib` & `seaborn`: For generating charts and visualizations.

## Project Structure

```plaintext
DataCleanX_Pro/
│
├── main.py                # Entry point of the application
├── csv_cleaner.py         # CSV cleaning module
├── docx_cleaner.py        # DOCX cleaning module
├── gui.py                 # GUI development using tkinter
├── report_generator.py    # Report generation and visualization
├── utils.py               # Utility functions
└── assets/
    └── icon.png           # GUI icon 
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/DataCleanX_Pro.git
   cd DataCleanX_Pro
   ```

2. **Install dependencies:**

   Make sure you have Python installed. Then, install the required Python packages:

   ```bash
   pip install pandas numpy python-docx matplotlib seaborn
   ```

## Usage

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Using the GUI:**
   - Select the CSV and DOCX files you wish to clean.
   - Click on "Clean Files" to process the files.
   - Generate a report by clicking "Generate Report."
   - View summary statistics and visualizations directly in the application.



## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **pandas** and **numpy** for powerful data manipulation.
- **python-docx** for DOCX handling.
- **matplotlib** and **seaborn** for creating visualizations.
- **tkinter** for the GUI development.

