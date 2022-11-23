<!-- #region -->
# HOWTO Tools

## Installing Python and Jupyter Notebook

You can experiment with the code online without installation using 
[Google CoLab](https://colab.research.google.com/github/mhahsler/CS7320-AI/).

To work on assignments, you can use one of several environments: 
* Use the online service [Google CoLab](https://colab.research.google.com). No additional installations are necessary.
* Install [Docker](https://www.docker.com/products/docker-desktop) and 
use a prepared JupyterLab on Ubuntu image.
Execute `docker run -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook` to download and create a container that runs
JupyterLab and bookmark the link (including the login token) that you get during installation. 
Details and configuration options can be found on the [Jupyter Docker stack GitHub page](https://github.com/jupyter/docker-stacks)) 
From now on, use `docker ps -a` to list containers and their container id, `docker stop <container id>` and `docker start <container id>` to stop and start the container (**do not use `run` again** because it will create a new empty container).
* Install Python, [JupyterLab](https://jupyter.org/) and all needed packages yourself. You can also use
Visual Studio Code as a nice editor.

## Learning Python and Jupyer Notebook

If you are not familiar with Python, then you should work through one of the many Python tutorials (e.g., [this tutorial](https://www.w3schools.com/python/default.asp)) to learn the basics about Python and the packages `numpy` and `pandas`. Some code examples that help with the assignments are available [here](.).

How to use Jupyter notebooks is covered in many online tutorials like the [Jupyer notebook tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).


## License
All code and documents in this repository are provided under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License.](https://creativecommons.org/licenses/by-sa/4.0/)

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)
<!-- #endregion -->
