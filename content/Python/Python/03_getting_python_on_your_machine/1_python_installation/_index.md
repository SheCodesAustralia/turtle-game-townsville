---
title: "Python installation"
weight: 10
chapter: true
---

We need Python before we can start. If you don't have Python installed yet, start by installing Python. Ideally we would like you to install the latest version of Python, however if you already have an earlier version installed that should work too! At a minimum, this tutorial requires Python 3.5.


## Check your version of Python

We're going to perform a simple experiment to check whether Python is already installed, and if it is, what version is installed.

Open the *Terminal* application of your choice (if you don't know what the terminal is feel free to ask a mentor) and enter the following command, depending on your operating system:

{{< tabs groupid="a" >}}
{{% tab title="_**MacOS**_" %}}
```shell
python3 --version
```
{{% /tab %}}
{{% tab title="_**Windows**_" %}}
```shell
py --version
```
{{% /tab %}}
{{< /tabs >}}

If the command returns `Python 3.Y.Z` congratulations you have Python installed! Otherwise you will have to install Python on your machine. How to do this will vary depending on your system, see below for instructions on how to do this for some common systems.

## Installation

{{< tabs groupid="a" >}}
{{% tab title="_**MacOS**_" %}}

Before you install Python on OS X, you should ensure your Mac settings allow installing packages that aren't from the App Store. Go to System Preferences (it's in the Applications folder), click
 "Security & Privacy," and then the "General" tab.  If your "Allow apps downloaded from:" is set to "Mac App Store," change it to "Mac App Store and identified developers."

You need to go to the website https://www.python.org/downloads/ and download the latest version of the Python installer:

* Download the *Mac OS X 64-bit/32-bit installer* file,
* Double click *python-3.x.x-macosx10.x.pkg* to run the installer.

{{% /tab %}}
{{% tab title="_**Windows**_" %}}

First check whether your computer is running a 32-bit version or a 64-bit version of Windows, by pressing the Windows key + Pause/Break key which will open your System info, and look at the "System type" line. You can download Python for Windows from the website https://www.python.org/downloads/windows/. Click on the "Latest Python 3 Release - Python x.x.x" link. If your computer is running a **64-bit** version of Windows, download the **Windows x86-64 executable installer**. Otherwise, download the **Windows x86 executable installer**. After downloading the installer, you should run it (double-click on it) and follow the instructions there.

One thing to watch out for: During the installation you will notice a window marked "Setup". Make sure you tick the "Add Python 3.x to PATH" checkbox and click on "Install Now", as shown below.

- If you forget to tick above checkbox, the easiest way is to uninstall and re-install with the option ticked.
- If `Microsoft Store` opens up when you run 'python' command in terminal, you can install python from the store directly. It will configure python environment for you.

{{< /tabs >}}
{{< /tabs >}}

![Don't forget to add Python to the Path](content/Python/Python/03_getting_python_on_your_machine/1_python_installation/images/python-installation-options.png)