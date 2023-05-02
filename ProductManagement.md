# PomodoroTimer 

## The Need..
I had to install Ubuntu on my personal machine and spend some time upskilling. I learnt about the [Pomodoro Technique](https://francescocirillo.com/products/the-pomodoro-technique#method). for better time management and realized that there was a need for an app for Ubuntu since none of the apps provided the functionality I wanted.

Hence, the project started of..

## Intro
This is a simple Pomodoro Timer using the tkinter library with sound created thanks to pygame library in Python. The timer helps you manage your work by breaking it down into intervals of 25 minutes, separated by short breaks. After completing four such intervals, you can take a longer break.

## Download and Installation

Follow these steps to download and install the Pomodoro Timer for Ubuntu:

1. Go to the [Releases](https://github.com/abpanic/PomodoroTimer/releases) page of the Pomodoro Timer repository.

2. Download the latest release's `.deb` file, which should be named something like `pomodorotimer-X.Y.Z.deb`, where `X.Y.Z` is the version number.

3. Open a terminal and navigate to the folder where you downloaded the `.deb` file.

   For example, if you downloaded the file to your `Downloads` folder, you would run:

   ```bash
   cd ~/Downloads
   ```
Install the Pomodoro Timer using the following command (replace X.Y.Z with the actual version number):

```bash
sudo apt install ./pomodorotimer-ubuntu-X.Y.Z.deb
```
Once the installation is complete, you can launch the Pomodoro Timer from your application menu or by running pomodoro-timer in the terminal.

## Usage

Once installed, you can launch the Pomodoro Timer from the Applications menu or by running the `Pomodoro-timer` command in a terminal. 

The timer will start automatically and you can customize the intervals and sounds in the settings. 

To DO: 

## Project Tracking: 

## User personas and scenarios:

Abpanic: Leader for a team that works on SDK troublshooting. Need to plan the day properly and move in a timebaound manner for each task.

Dbugr: A Software Engineer working on a project with Abpanic and would look to have a productivity tool to be aware of the time and the backlog/tasks at hand.

## Competitive analysis: 

What do the other Pomodoro Timers or Task Trackers available in the market provide?

## Prioritization and backlog management: 


## Roadmap: 

1.Adjustable work and break intervals: Allow users to customize the duration of work and break intervals. You can add two entry fields or spinboxes for users to set the desired work and break durations.

2.Automatic break intervals: After a work interval is completed, automatically start a break interval. You can implement a state variable to track whether the timer is in work or break mode and adjust the timer accordingly.

3.Task completion tracking: Add checkboxes or another method for users to mark tasks as complete. You could display completed tasks with a strikethrough or a different color.

4.Statistics: Keep track of the number of completed Pomodoro cycles and tasks. Display this information in a separate window or at the bottom of the main window.

5.Save and load tasks: Implement a feature to save and load tasks from a file, allowing users to manage and track tasks across sessions.

6.Audio customization: Allow users to choose a custom alarm sound or select from a list of built-in sounds.

7.Visual customization: Offer a settings panel where users can choose custom colors or themes for the application.

8.Keyboard shortcuts: Implement keyboard shortcuts to start, stop, and reset the timer, as well as add, remove, or complete tasks.

9.Notifications: Send desktop notifications when a work or break interval ends, ensuring users are aware even if the application is minimized.

10.Progress bar: Display a progress bar that fills up as the timer counts down, providing a visual representation of the time remaining.

## User feedback and analytics: 
Add a feedback page from disqus.

## Product iteration and continuous improvement: 
Share product timeline.

## Documentation and user guides: 
Start creating one about Documentation

## Collaboration and communication: 

## Risk assessment and mitigation:


## Release management:
Stable version released as .py
Executable creation pipeline currently underway. 

