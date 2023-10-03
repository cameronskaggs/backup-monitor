# backup-monitor
A program to monitor file changes in monthly backups

## Prerequisites
Requires python 3 to run
## How to use
<ol>
<li> Clone this repo locally. cd into the project's root directory </li>
<li> Copy the values in from old backup files into a file called 
`Old.sha1.txt` and from your new ones in `New.sha1.txt` 
Copy these values into the project root directory</li>
<li> Run `python3 backup-monitor.py` </li>
</ol>

## Optional flags

-o, --oldfile &emsp; old backup file name (defaults to Old.sha1.txt)  
-n --newfile &emsp; new backup file name (defualts to New.sha1.txt)  
-or --oldresultfile &emsp; the name of the file produced by the program
which contains all the values which are in the old file but not in the new file (defaults to OldNotInNew.txt)  
-nr --newresultfile &emsp; the name of the file produced by the program
which contains all the values which are in the new file but not in the old file (defaults to NewNotInOld.txt)