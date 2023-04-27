# PodomoroTimer

## The Need..
I had to install Ubuntu on my personal machine and spend some time upskilling. I learnt about the [Pomodoro Technique](https://francescocirillo.com/products/the-pomodoro-technique#method). for better time management and realized that there was a need for an app for Ubuntu since none of the apps provided the functionality I wanted.

Hence, the project started of..

## Intro
This is a simple Pomodoro Timer using the tkinter library with sound created thanks to pygame library in Python. The timer helps you manage your work by breaking it down into intervals of 25 minutes, separated by short breaks. After completing four such intervals, you can take a longer break.

## Download and Installation

Follow these steps to download and install the Pomodoro Timer for Ubuntu:

1. Go to the [Releases](https://github.com/abpanic/PodomoroTimer/releases) page of the Pomodoro Timer repository.

2. Download the latest release's `.deb` file, which should be named something like `pomodoro-timer-X.Y.Z.deb`, where `X.Y.Z` is the version number.

3. Open a terminal and navigate to the folder where you downloaded the `.deb` file.

   For example, if you downloaded the file to your `Downloads` folder, you would run:

   ```bash
   cd ~/Downloads
   ```
Install the Pomodoro Timer using the following command (replace X.Y.Z with the actual version number):

```bash
sudo apt install ./pomodoro-timer-ubuntu-X.Y.Z.deb
```
Once the installation is complete, you can launch the Pomodoro Timer from your application menu or by running pomodoro-timer in the terminal.

## Usage

Once installed, you can launch the Podomoro Timer from the Applications menu or by running the `podomoro-timer` command in a terminal. 

The timer will start automatically and you can customize the intervals and sounds in the settings. 

## Contributing

If you find any issues or have suggestions for improvement, please feel free to submit a pull request or create an issue in this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# Step-by-step build guide:

The Guide to creation of this entire project is [here](https://abpanic.github.io/PodomoroTimer/Building)

Created an initial file for the project with the code: https://gist.github.com/abpanic/63b183c40ac29d95231a6d8babdeb64b

Working file on the initial scaffolding: https://gist.github.com/abpanic/9dd14bc85105d2320a10e4dd947c516e

Final file after adding alarm sound: https://gist.github.com/abpanic/e2964def37527f13ac36de5c23dbaf52

https://gist.github.com/abpanic/7b1e5557b06e7245e05237fd04462d34

