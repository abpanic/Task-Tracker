# Building the Pomodoro Timer for Ubuntu

This step-by-step guide will walk you through the step-by-step building process I went through for the Pomodoro Timer application for Ubuntu.

## Prerequisites

Ensure you have the following tools and libraries installed on your system:

- Python 3
- Pip (Python package manager)
- GTK+ 3
- Git (optional, for cloning the repository)

## Step 1: Install Dependencies

Install the required dependencies using the following command:

```bash
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```
## Step 2: Clone or Download the Repository
Option A: Clone the repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/abpanic/pomodoro-timer.git
```
Option B: Download the repository
Download the repository as a ZIP file from the GitHub page and extract it to your desired location.

## Step 3: Install Python Packages
Navigate to the repository folder and install the required Python packages using the following command:

```bash
cd pomodoro-timer-ubuntu
pip3 install -r requirements.txt
```
## Step 4: Build the Application
Build the application using your desired method. For example, you can create a standalone executable or a .deb package.

### Option A: Create a standalone executable
Use PyInstaller to create a standalone executable:

```bash
pip3 install pyinstaller
pyinstaller --onefile main.py
```
### Option B: Create a .deb package
Follow a guide to create a .deb package from your Python application, such as this [tutorial](https://www.electronjs.org/docs/latest/tutorial/application-distribution#creating-packages).

## Step 5: Test the Application
Run the application to ensure it works correctly:

```bash
python3 main.py
```
## Step 6: Distribute the Application
Share your built application with others, either by providing the standalone executable or by uploading the .deb package to your GitHub Releases page.
For more information on how to use the Pomodoro Timer, please refer to the [step-by-step guide](https://abpanic.github.io/PodomoroTimer/).

## The Build Process

Onto VS Code.

Starting new file with the filename "PodomoroTimer.py" with an initial scaffolding on what the item is supposed to contain.
The initial code look like the below:

The initial code is just the scaffolding of the application is okay, not to have all the components functional in first go.
But the initial run in VSCode should show us the app launched and this was certainly the case.

[screenshot 1]

Now adding the rest of the code components to ensure it is functional and does what application is supposed to.

hence added the below:

[added code..]

Now the application is coming up nicely and we can run it from terminal with "python3 PodomoroTimer.py"

The application launches and the timer can continue. But an Minimum Viable Product should have the features that goes beyond being the bare functions. It should have the functionalities in the initial phase that make users want to use it more.

So on to the part that would make is different from others available in Ubuntu snap(Ubuntu marketplace for apps) 
A->It should have an alarm sound that the user can hear allowing the user to reset.
B->Make it executable with double click on Ubuntu

A->
This can be done with pygame library and hence:

[added code..]

B->
To make your Python script executable with a double click on Ubuntu:
To make your Python script executable with a double click on Ubuntu, you need to follow these steps:

Add a shebang line: Open your Python script (PodomoroTimer.py) in a text editor and add the following line to the very top of the file:

```
#!/usr/bin/env python3
```
This line tells the operating system to use Python 3 to run the script.

Save and close the file.

Make the script executable: Open a terminal window and navigate to the directory where the script is located. Then, run the following command:

```
chmod +x PodomoroTimer.py
```
This command grants the script executable permissions.

Associate the script with Python: To make sure your script opens with Python when double-clicked, you need to associate .py files with the Python interpreter. To do this, follow these steps:

a. Right-click on the PodomoroTimer.py file and select "Properties" from the context menu.

b. In the "Properties" window, navigate to the "Open With" tab.

c. Find the "Python 3" interpreter in the list of applications. If you don't see it, click "Show other applications" and find it in the extended list.

d. Select "Python 3" and click the "Set as default" button.

Double click the script: Now you should be able to double-click the PodomoroTimer.py file to run the script.

If you want to create a desktop shortcut for your script, follow these additional steps:

Right-click on your desktop and select "Create a new launcher here" or "Create Launcher" (the wording may differ depending on your Ubuntu version).

In the "Create Launcher" window, fill in the details:

a. Type: Select "Application" from the dropdown menu.

b. Name: Enter a name for the shortcut, such as "Podomoro Timer".

c. Command: Click the "Browse" button and navigate to the location of your PodomoroTimer.py file. Select the file and click "Open".

d. (Optional) Icon: Click the icon placeholder to choose an icon for the shortcut.

Click "OK" or "Create" to create the desktop shortcut.

Now you should be able to run your Python script by double-clicking the desktop shortcut or the script file itself.


With these steps it is now time to go to working on making a distributable of the pilot version:

## To convert Python script into a Debian package (.deb file), steps were :

### Install required tools:

Open a terminal and run the following commands to install the necessary tools:

```
sudo apt update
sudo apt install dh-python devscripts debhelper
```
Create a directory structure for your package:

Replace your_package_name with a name for your package, and run the following commands:

```
mkdir -p your_package_name/usr/src/your_package_name
mkdir -p your_package_name/usr/bin
mkdir -p your_package_name/debian
```
Then, move your Python script (PodomoroTimer.py) to the your_package_name/usr/src/your_package_name directory.

### Create a script to run your application:

In the your_package_name/usr/bin directory, create a new file called your_package_name (without any file extension). In this file, add the following content:

```
#!/bin/sh
/usr/bin/python3 /usr/src/your_package_name/PodomoroTimer.py
```
Save the file and make it executable by running:

```
chmod +x your_package_name/usr/bin/your_package_name
```
### Create a debian/control file:

In the your_package_name/debian directory, create a new file called control. Add the following content to the file, replacing the placeholder text with your package details:

```
Source: your_package_name
Section: utils
Priority: optional
Maintainer: Your Name <your.email@example.com>
Build-Depends: debhelper (>=9), dh-python, python3
Standards-Version: 3.9.8

Package: your_package_name
Architecture: all
Pre-Depends: dpkg (>= 1.16.1), python3
Depends: ${shlibs:Depends}, ${misc:Depends}, ${python3:Depends}
Description: Short description of your package
 Long description of your package.
 ```
### Create a debian/rules file:

In the your_package_name/debian directory, create a new file called rules. Add the following content to the file:

```

#!/usr/bin/make -f

%:
	dh $@ --with python3 --buildsystem=pybuild --system=setuptools
```
Save the file and make it executable by running:

```

chmod +x your_package_name/debian/rules
```
### Create a debian/changelog file:

In the your_package_name/debian directory, create a new file called changelog. Add the following content to the file, replacing the placeholder text with your package details:

```
your_package_name (1.0-1) unstable; urgency=low

  * Initial release.

 -- Your Name <your.email@example.com>  <current_date>
 ```
Replace <current_date> with the current date in the format Mon, DD MMM YYYY HH:MM:SS +ZZZZ.

### Setup.py to for the build system
Make sure that you have a setup.py file in the root directory of your project. If you don't have one, create a setup.py file with the following content:

```
from setuptools import setup, find_packages

setup(
    name="podomorotimer",
    version="1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'podomorotimer=podomorotimer:main',
        ],
    },
)
```
Replace podomorotimer:main with the appropriate module and function name for your application entry point.

###  Create a debian/compat file:
Creating  create a new file called compat in the debian directory with the following content:

```
10
```
This sets the compatibility level to 10, which should work with the tools you are using.

### Build the Debian package:

Navigate to the root of your your_package_name directory in the terminal and run the following command:

```
dpkg-buildpackage -us -uc
```
If the build is successful, a .deb file will be generated in the parent directory of your your_package_name folder.

Now you have a .deb file that you can distribute and install on Debian-based systems using the dpkg -i your_package_name.deb command.
