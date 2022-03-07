# ddz
This is a python script that uses DD to zero drives. 
DDZ is for linux only, and for linux scsi disks only. 

ddz depends on:

progress 
Progress likely can be installed with your package manager. 
For example: sudo apt install progress 

reprint 
reprint can be installed with python pip 
python -m pip install reprint 

DDZ tries to predict unmounted drives and zero them 
python DDZ.py -h displays these options 
python DDZ.py -a will auto zero all unmounted drives 
python DDZ.py -g will enter guided mode, and ask to mark each drive 
python DDZ.py -l will list the drives and mount points predicted by automode
python DDZ.py -t will run in auto mode and dd drives to /dev/null 

