# HOWTO Work on Assignments

We will provide you with a CoLab link to the assignment notebook.

* **Option 1:** You can work directly on CoLab by using `File>Save a copy to Drive`(you will need a Google Account). To use data files from within CoLab, you need to go to your [Google Drive](drive.google.com) to the folder called My Drive - CoLab Notebooks and copt the needed files there. Then you need to mount your Google drive in your notebook, and change to the directory to the notebook folder. The needed code for your code cell looks like this:

    ```{python}
    from google.colab import drive
    import os

    drive.mount('/content/drive')
    os.chdir('/content/drive/My Drive/Colab Notebooks/')
    !pwd
    ```

* **Option 2:** You can download individual assignment notebooks using `File>Download>Download .ipynb` and then work locally on the project. You will need to download additional files as well.

Make sure that you have a copy of your assignment in a save place that has a backup (e.g., Google Drive).
If you want to work on the assignment using version control, then create a new **private** repository and check your code in there. 

Your assignment notebook needs to be a complete project reports with 

- documentation (including your design choices), 
- code (with comments for difficult to understand sections) and
- results (e.g., tables with simulation results) with a short discussion of what they mean. 

Use the provided notebook cells and insert additional code and markdown cells as needed.
