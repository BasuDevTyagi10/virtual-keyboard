# VIRTUAL KEYBOARD
a virtual keyboard built using OpenCV and mediapipe

## Technologies Used:
The project is created using :
* Python 3.8.8
* OpenCV 4.5.3
* mediapipe v7.0

## Getting Started
Clone the repo on local machine:
```sh
$ git clone https://github.com/BasuDevTyagi10/virtual-keyboard.git
$ cd "virtual-keyboard"
```
### Create a virtual environment (for better control (version control) over the project)
It is better to use Anaconda Navigator ([Anaconda Documentation - Installation](https://docs.anaconda.com/anaconda/install/)) for handling such (and further mentioned) tasks of creating virtual environments, installing packages, IDEs, Applications, etc.
<br>
<br>For performing the mentioned operations manually (without Anaconda) :
<br><br>Install ```virtualenv``` module to create isolated virtual environments.
```sh
$ pip install virtualenv
```
To create a Virtual Environment for Python 2.x do the following
```sh
$ virtualenv myenv
```
For a Python 3 virtual environment type –
```sh
$ python3 -m venv myenv
```
To activate the virtual environment -
<br>On Windows, run:
```sh
$ myenv\Scripts\activate.bat
```

### Installing required packages
The required packages for this project are listed in ```requirements.txt``` file, for a brief overview the following packages are being used in the project to run the python scripts:
<br>```opencv-python```, ```mediapipe```, ```cvzone```, ```numpy```, ```pygame``` and ```pynput```
<br><br>Install the above mentioned packages in your virtual environment using Anaconda, and without it by:
<br>_run the below command after you're in your virtual environment_
```sh
(myenv)$ pip install -r requirements.txt
```

### Run the script:
(make sure youre in the home directory) run the following command -
```sh
(myenv)$ python main.py
```

## Documentations Refered:
The following documentations were refered to create this project :
* [Python 3.8.8](https://www.python.org/doc/)
* [OpenCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
* [mediapipe](https://google.github.io/mediapipe/)
* [cvzone](https://github.com/cvzone/cvzone)

## Authors

-   **Basudev Tyagi** - _Initial work_ - [BasuDevTyagi10](https://github.com/BasuDevTyagi10)
