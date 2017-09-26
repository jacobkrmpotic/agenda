# agenda
Simple CLI task manager written in python.

Your agenda file is stored at ~/.agenda

## Installation
===============
There are many ways to get a script and make it quickly accessible,
but this is usually how I do it. 

1. `git clone https://github.com/jacobkrmpotic/agenda.git`
2. `cd agenda`
3. `sudo chmod +x agenda`
4. `sudo ln -s /path/to/agenda /usr/local/bin/agenda`

*And to uninstall...*

1. `cd /path/where/you/cloned`
2. `rm -rf agenda`
3. `rm ~/.agenda`
4. `sudo rm /usr/local/bin/agenda`

If you don't have administrative rights, instead of
making it an executable, one can simply run:
python3 agenda ...

and instead of adding it to your /usr/local/bin 
directory, you can alias it in your shell's rc as so...



~/.zshrc or ~/.bashrc
---------------------
...
alias agenda="python3 /path/to/agenda"
...

Basic Usage
----------------
#### _Through examples_

**Listing the tasks in our agenda.**

`agenda`

One simply calls `agenda` itself. Calling agenda with an arugment will
also print out your tasklist after the modifications have been made
regardless.

**Adding event, 'hello world', to our agenda.**

`agenda add hello world`

Our tasklist now looks like:

...
1. hello world

**Changing event, 'hello world', to 'goodbye' world.**

`agenda edit 1 goodbye world`

**Stylizing our first task.**

`agenda style 1 italic black white`

The order here matters, the form for the `agenda style` command is as follows:

`agenda style [index] [text-decoration] <text-color> <text-highlight>`

To remove the italics one would:

`agenda style 1 normal black white`

**Removing the style for tasks 4 and 5.**

`agenda unstyle 4 5`

**Swapping the second and third tasks.**

`agenda swap 2 3`

**Removing the last task on our agenda, regardless of number of tasks.**

`agenda pop`

**Removing tasks 4 and 5.**

`agenda rm 4 5`

or

`agenda del 4 5`

or

`agenda remove 4 5`

**Deleting every task in our agenda.**

`agenda clear`

**Listing these options if you forget.**

`agenda help`
