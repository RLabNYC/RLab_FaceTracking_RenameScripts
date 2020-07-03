# RLab_RenameScripts

Todd Bryant, Kat Sullivan and Grant Ng

# Installing Python

If you don't have Python 3, download Python [here](https://www.python.org/downloads/). Make sure you check off "Python version number to PATH"! Also be sure to include pip in the installation. (If you don't, details on how to do that are below)

![python screenshot](https://i.ibb.co/5RYbr30/Inkedwin-installer-LI.jpg)



# Installing pip

If you already have pip installed, please skip this section.

In terminal, cd to where you installed this repository, then cd to the PythonScripts folder.
To install pip, simply run:

```
python get-pip.py
```

# Running the Renaming Script

The script will take care of any additional python libraries and run the Python renaming script. It will search for a csv file in the PythonScript file so **be sure you choose either the Fuse.csv or Makehuman.csv file (found in the csv_files folder) and move it inside the PythonScripts folder**. You will also place your Maya file (.ma) into the PythonScripts folder. The script will rewrite the .ma file with the correct naming syntax.

Once that is done, be sure to be running command prompt as admin and run

```
runme.bat
```



If you have any pip-related issues try upgrading pip by

```
py -m pip install --upgrade pip
```

