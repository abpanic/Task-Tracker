In this blog post, I'll be discussing the build process of a custom Pomodoro Timer created for my use case. This project also showcases my product management skills. Let's dive into the details.

## The Build Process

### Visual Studio Code

I started by creating a new file in Visual Studio Code with the filename "PomodoroTimer.py" and added an initial scaffolding to outline the main components of the application. The initial code looks like this:

[Initial code]

The initial code is just the scaffolding of the application, and it's okay not to have all the components functional in the first go. However, running the initial code in VSCode should launch the app, as we kick off and that's precisely what happened.

![screenshot 1]

Next, I added the rest of the code components to ensure the application is functional and performs the tasks it's supposed to.

[Added code]

Now, the application is coming up nicely, and we can run it from the terminal with `python3 PomodoroTimer.py`.

The application launches and the timer starts. However, a Minimum Viable Product (MVP) should have features that go beyond basic functionality. It should include features in the initial phase that make users want to use it more.

So, I focused on two unique features to set it apart from other Pomodoro timers available in the Ubuntu snap store:

1. An alarm sound that the user can hear, allowing them to reset the timer.
2. The ability to launch the application with a double click on Ubuntu.

To implement these features, I made the following changes:

### Adding Alarm Sound

I used the `pygame` library to add the alarm sound feature:

[Added code]

### Making the Application Executable with Double Click on Ubuntu

To make the Python script executable with a double click on Ubuntu, I followed these steps:

1. Add a shebang line to the script.<br>
Open your Python script (PodomoroTimer.py) in a text editor and add the following line to the very top of the file:
```
#!/usr/bin/env python3
```
This line tells the operating system to use Python 3 to run the script.<br>
Save and close the file.

2. Make the script executable.<br>
Open a terminal window and navigate to the directory where the script is located. Then, run the following command:
```
chmod +x PodomoroTimer.py
```
This command grants the script executable permissions.

3. Associate the script with the Python interpreter.<br>
To make sure your script opens with Python when double-clicked, you need to associate .py files with the Python interpreter. To do this, follow these steps:<br>
a. Right-click on the PodomoroTimer.py file and select "Properties" from the context menu.<br>
b. In the "Properties" window, navigate to the "Open With" tab.<br>
c. Find the "Python 3" interpreter in the list of applications. If you don't see it, click "Show other applications" and find it in the extended list.<br>
d. Select "Python 3" and click the "Set as default" button.<br>
Double click the script: Now you should be able to double-click the PodomoroTimer.py file to run the script.<br>

4. (Optional) Create a desktop shortcut.<br>
Right-click on your desktop and select "Create a new launcher here" or "Create Launcher" (the wording may differ depending on your Ubuntu version).<br>
In the "Create Launcher" window, fill in the details:<br>
a. Type: Select "Application" from the dropdown menu.<br>
b. Name: Enter a name for the shortcut, such as "Podomoro Timer".<br>
c. Command: Click the "Browse" button and navigate to the location of your PodomoroTimer.py file. Select the file and click "Open".<br>
d. (Optional) Icon: Click the icon placeholder to choose an icon for the shortcut.<br>
Click "OK" or "Create" to create the desktop shortcut.<br>

With these enhancements, it's now time to work on creating a distributable version of the pilot application.

To convert the Python script into a Debian package (.deb file), I followed these steps:

1. Install required tools.
Open a terminal and run the following commands to install the necessary tools:
```
sudo apt update
sudo apt install dh-python devscripts debhelper
```
2. Create a directory structure for the package.
Replace your_package_name with a name for your package, and run the following commands:
```
mkdir -p your_package_name/usr/src/your_package_name
mkdir -p your_package_name/usr/bin
mkdir -p your_package_name/debian
```
Then, move your Python script (PodomoroTimer.py) to the your_package_name/usr/src/your_package_name directory.

3. Create a script to run the application.
In the your_package_name/usr/bin directory, create a new file called your_package_name (without any file extension). In this file, add the following content:
```
#!/bin/sh
/usr/bin/python3 /usr/src/your_package_name/PodomoroTimer.py
```
Save the file and make it executable by running:
```
chmod +x your_package_name/usr/bin/your_package_name
```

4. Create a `debian/control` file.
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
 
5. Create a `debian/rules` file.
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

6. Create a `debian/changelog` file.
Add the following content to the file, replacing the placeholder text with your package details:
```
your_package_name (1.0-1) unstable; urgency=low

  * Initial release.

 -- Your Name <your.email@example.com>  <current_date>
```
Replace <current_date> with the current date in the format Mon, DD MMM YYYY HH:MM:SS +ZZZZ.

7. Create `setup.py` file.
Create a setup.py file in the root directory of your project with the following content:
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

8. Create a `debian/compat` file.
Creating create a new file called compat in the debian directory with the following content:
```
10
```
This sets the compatibility level to 10, which should work with the tools you are using.

9. Build the Debian package.
Navigate to the root of your your_package_name directory in the terminal and run the following command:
```
dpkg-buildpackage -us -uc
```
If the build is successful, a .deb file will be generated in the parent directory of your your_package_name folder.

Now, I have a .deb file that I can distribute and install on Debian-based systems using the `dpkg -i your_package_name.deb` command.
