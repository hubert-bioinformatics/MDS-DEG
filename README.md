# MDS-DEG
Create MDS and DEG result plots from RNA expression data.

# Prepare
## Install Python and Required Libraries
1. Install Python:
    * Download and install Python from the official website.
    * During installation, make sure to check the box that says "Add Python to PATH".

2. Install Required Libraries:
    * Open Command Prompt (cmd) and install the required Python libraries using pip:
    * `pip install flask pandas scikit-learn plotly`


## Run the Flask Application
1. Navigate to the Project Directory:
    * Open Command Prompt and navigate to your project directory:
    * `cd path\to\your\project\directory`

2. Run the Flask Application:
    * Execute the following command to run the Flask application:
    * `python app.py`

3. Access the Website:
    * Open a web browser and go to http://127.0.0.1:5000 to access your website.


## Example Directory Structure
```
mds_plot_generator/
│
├── uploads/
│
├── app.py
└── index.html
```


## Steps to Test
1. Run the Flask Application:
    * Start the Flask server by running python app.py.

2. Upload a TSV File:
    * Upload your RNA sequencing data file through the web interface.

3. Drag and Drop Samples:
    * Drag samples from the "All Samples" box to the "Selected Samples" box.
    * Drag samples back from the "Selected Samples" box to the "All Samples" box to deselect them.

4. Select MDS Plot Type:
    * Choose between a 2D or 3D MDS plot using the radio buttons.

5. Generate MDS Plot:
    * Click the "Generate MDS Plot" button to generate and visualize the MDS plot.

6. Create Groups for DEG Analysis:
    * Drag samples from the "Selected Samples" box to the "Test" and "Control" boxes.

7. Perform DEG Analysis:
    * Click the "Perform DEG Analysis" button to perform DEG analysis and visualize the results, including the list of DEGs ordered by p-value.


## Example

![DEG1](https://github.com/user-attachments/assets/019e4f1c-6b1f-4598-ac53-de75790d61b4)

![DEG2](https://github.com/user-attachments/assets/5189479e-02b6-478f-93cb-e12697af3434)

![DEG3](https://github.com/user-attachments/assets/d0fd919d-2422-4588-bf36-bcb076ea0ff5)

![DEG4](https://github.com/user-attachments/assets/c572f72f-136a-45c6-a48b-728fbd0363fb)
