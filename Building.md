# Building the Pomodoro Timer for Ubuntu

This step-by-step guide will walk you through building the Pomodoro Timer application for Ubuntu.

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
Follow a guide to create a .deb package from your Python application, such as this tutorial.

## Step 5: Test the Application
Run the application to ensure it works correctly:

```bash
python3 main.py
```
## Step 6: Distribute the Application
Share your built application with others, either by providing the standalone executable or by uploading the .deb package to your GitHub Releases page.
