# ddz
This is a python script that uses DD to zero drives. 
DDZ is for linux only, and for linux scsi disks only. 

ddz depends on:

progress 

Progress likely can be installed with your package manager. 

For example: sudo apt install progress 

reprint 

reprint can be installed with python pip,  

python -m pip install reprint 

DDZ tries to predict unmounted drives and zero them 


python DDZ.py -h displays these options 

python DDZ.py -a will auto zero all unmounted drives

python DDZ.py -g will enter guided mode, and ask to mark each drive 

python DDZ.py -l will list the drives and mount points predicted by automode

python DDZ.py -t will run in auto mode and dd drives to /dev/null 


DDZ was created to fullfill the needs of the author and is not intended for general use. 

DDZ is shared for two express purposes, the first is to save time for similar applications. 
The second is to enrich FOSS, and or to be harvested for examples. 

WARNING!

--------------------

This program was designed and impliented to perminantly destroy data do not use this program if you do not understand and accept the potential risks associated with its use. 

