# ddz
This is a python script that uses DD to zero drives. 
DDZ is for linux only, and for linux scsi disks only. 

ddz depends on:

progress \n
Progress likely can be installed with your package manager. \n 
For example: sudo apt install progress \n

reprint \n
reprint can be installed with python pip \n
python -m pip install reprint \n

DDZ tries to predict unmounted drives and zero them \n
python DDZ.py -h displays these options \n
python DDZ.py -a will auto zero all unmounted drives \n
python DDZ.py -g will enter guided mode, and ask to mark each drive \n
python DDZ.py -l will list the drives and mount points predicted by automode \n
python DDZ.py -t will run in auto mode but dd drives to /dev/null \n

