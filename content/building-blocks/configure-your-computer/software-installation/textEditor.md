# Text Editors

A good text editor lies at the heart of any serious programmer's toolkit: It can do almost anything and makes you much more productive.
The editors built into each program often are not the best option (we will find certain cases where you may want to use them).

Please download, install it along with the necessary packages and stick with it for at least the duration of the project or assignment to get a feel for how it works.

There is a slight learning curve, but soon you hopefully will be wondering why no-one forced you to do this before!

!!! note
    - None of the skills on this website are tied to Atom,
	so if you do decide to move away to another editor, nothing will be lost. For example, [Visual Studio Code](https://code.visualstudio.com/) or [Vim](https://www.vim.org/) are also widely used text editors.

<!-- ## Installing Sublime Text

Go to the [downloads page](https://www.sublimetext.com/3) and download the live installer for your operating system.-->

## Installing Atom

### Mac and Windows Users

Go to the [downloads page](https://github.com/atom/atom/releases/latest) and download the installer for your operating system:

* Windows users download AtomSetup-x64.exe and execute the installer
* Mac users download Atom-Mac.zip and copy the contained Atom.app into the applications folder

### Linux/Ubuntu users

Enter the following information to add a repository that has the Atom installation, then press `Return`:

```bash
sudo add-apt-repository ppa:webupd8team/atom
```

Install Atom by entering the following commands into a terminal and then pressing `Return:`

```bash
sudo apt update; sudo apt install atom
```

## Verifying Atom Installation

We want Atom to be available from the command line. For Mac and Linux Users this is the default after you have started the program once. So please open Atom. Then open your terminal and type the following into the command line:

```bash
atom --version
```
followed by pressing `Return` you should see output like the following
```bash
Atom    : 1.28.2
Electron: 2.0.5
Chrome  : 61.0.3163.100
Node    : 8.9.3
```
Make sure that the version numbers are above `1.26.x` or newer.

!!! danger "Additional Step for Windows:"
    Getting things to run from the command line for Windows users is a bit harder. You will need local administration rights for your computer, but you should have these on your personal computers or those owned by the University.

    - Right-click on Computer.
	- Then go to "Properties" and select the tab "Advanced System Settings".
	- Choose "Environment Variables" and select `Path` from the list of system variables.
	- If you accepted all defaults during your installation, and didn't have any other non-default setting prior to starting this guide, choose `Edit.`

		- **On Windows 7 or 8 machines:**
			Append the following (i.e., do not overwrite the previous value) modifying the string, with your relevant `username`:

            `;C:\Users\username\AppData\Local\atom\bin`

			to the variable value – make sure the rest remains as it is and do not include spaces between the ";" and preceeding text.

		- **On Windows 10 machines:**
			Click `New` and paste the following string, modifying the `username`

			`C:\Users\username\AppData\Local\atom\bin`

		Click on `OK` as often as needed.

    Close your current terminal session, open a new one, and again try `atom .` - the Atom editor will open if this was successful.

!!! tip "Installing Additional Packages for Atom"

    One of the advantages of Atom is that there are many *packages* that make your life easier, ranging from simple syntax highlighting to environments that can mimic a complete graphical user interface.

    * To access Atom's settings press `Ctrl + ,` (`CMD + ,` on Mac) on your keyboard then click on the `Install` tab which is visible on the left hand side.
    * On the Installation page there is a prompt where you can type in a package name and then press `Return` and Atom will search for that package for you and return results with similar names.
    When you find the package that you need, you click the blue 'Install' button and the package will be installed.
    * If during the installation of a package Atom asks to install dependencies, always choose to accept.

    * If you decide to stick with Atom, you may find the following packages useful in your day-to-day work:

        *   tablr
        *   tablr-json

        *   autocomplete-R
        *   autocomplete-python (choose Jedi as your engine when asked)
        *   autoflow
        *   language-r
        *   linter
        *   linter-lintr
        *   platformio-ide-terminal
        *   project-plus
        *   language-markdown
        *   markdown-table-editor
        *   markdown-preview-plus
        *   autocomplete-citeproc
        *   open-unsupported-files
        *   advanced-open-file
        *   language-latex
        *   language-matlab
        *   language-stata
        *   atom-latex
        *   whitespace



    Feel free to ask us for whatever other packages we use to make our programming lives easier during some downtime.
