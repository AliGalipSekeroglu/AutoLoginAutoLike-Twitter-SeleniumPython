# AutoLoginAutoLike-Twitter-SeleniumPython
Login in Twitter without writing password/username and like tweets related with the hashtag that you search automaticly.


Hello everyone.

First of all,before you start to use the project,you must follow the instructions:

1-You must have Python3 to use this project. I use Python 3.6 through Anaconda 5.0.0

2- In order to setup Selenium package,open command line (CTRL + R) and run cmd and run the code below: pip install selenium

3-Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.

Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ Firefox:	https://github.com/mozilla/geckodriver/releases Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/

4- After downloading browser's file (For Chrome,Firefox etc.) and you need to give a path of this exe. file. Copy the path of that exe. file and follow the instructions:

*From the desktop, right click the Computer icon. *Choose Properties from the context menu. *Click the Advanced system settings link. *Click Environment Variables. ... *In the Edit System Variable (or New System Variable) window, specify the value of the PATH environment variable.

5-I use Visual Studio Code as compiler but you can use which compiler you wish. (I can advice to use Python IDLE.) I pretend you're going to use Visual Studio Code and open View-Integrated Terminal and type below and run:

python your_application_name.py
