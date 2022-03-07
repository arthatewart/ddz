'''
This Program written by Aaron A. Dennis.
This software offers absolutely no waranty of fitness or purpose.
Do not use this software if you are uncertain of its fucntion or purpose. 
The user assumes all potential liability for loss or damages. 
This software may be redistributed as per GPL V2 public license. 
DDZ Version 0.0.1.3 
Copyrite Aaron A. Dennis 2022 
'''
###############################################################################
from reprint import output
from string import digits
from sys import argv
import subprocess 
import time
import re
import os
status_var = []
def cmd_out(cmd_ty, cmd_op, cmd_au): # Runs external CLI programs. 
	if (cmd_ty == 1):
		return None
	elif(cmd_ty == 2 and cmd_op != '' and cmd_au == ''):
		os.system(cmd_op)
		return None
	elif(cmd_ty == 2 and cmd_op !='' and cmd_au !=''):
		os.system('echo {} | sudo -S {}' . format(cmd_au, cmd_op))
		return None
	elif(cmd_ty == 3 and cmd_op != '' and cmd_au != ''):
		cmd_o= subprocess.Popen('echo {} | sudo -S {}' . format(cmd_au, cmd_op)
                          ,stdout=subprocess.PIPE, shell=True)
		cmd_pr= cmd_o.stdout.read()
		return(cmd_pr)
	elif(cmd_ty == 3 and cmd_op != '' and cmd_au == ''):
		cmd_o= subprocess.Popen(cmd_op, stdout=subprocess.PIPE, shell=True)
		cmd_pr= cmd_o.stdout.read()
		return(cmd_pr)
	else:
		return None		
def uname(): # Returns system info with uname.
	uname_wd= cmd_out(3, 'uname -a', '')
	uname_wd= re.split('\s+', uname_wd)
	uname_wd= "Running on " + uname_wd[0] + "!"
	return(uname_wd)
def whoami(): # Returns user name.
	whoami_wd= cmd_out(3, 'whoami', '')
	whoami_wd= re.split('\n+', whoami_wd)
	return(whoami_wd[0])
def dfh(): # Returns mounted disks and directories.
	dfh_wd= cmd_out(3, 'df -h', '')
	dfh_wd= re.split('\n+', dfh_wd)
	dfh_lt= []
	for x in range(len(dfh_wd[:-1])):
		if x == 0:
			pass
		elif x > 0:
			dfh_lt.append(dfh_wd[x])
	return(dfh_lt)	
def lsdev(): # Reruns contents of ls /dev with grep.
	lsdev_wd= cmd_out(3, 'ls /dev | grep -i sd', '')
	lsdev_wd= re.split('\n+', lsdev_wd)
	lsdev_lt= []
	for x in range(len(lsdev_wd[:-1])):
		lsdev_lt.append(lsdev_wd[x])
	return(lsdev_lt)
def comp_dk(): # Returns match comparison from df -h and ls /dev.
	dfh_lt= dfh()
	dev_lt= lsdev()
	cd_lt= []
	for x in dfh_lt:
		for y in dev_lt:
			if y in x:
				cd_lt.append(x)
	clean_lt = set(cd_lt)
	return(list(set(clean_lt)))
def format_dk(): # Removes entries in ls /dev with match comparison.  
	dev_lt= lsdev()
	devlt_r = []
	for x in range(len(dev_lt)):
		devlt_r.append(dev_lt[x].translate(None, digits))
	cdk_lt= comp_dk()
	cdklt_r = []
	for x in range(len(cdk_lt)):
		cdklt_r.append(cdk_lt[x].translate(None, digits))
	cot= 4
	for a in range(cot):
		for b in devlt_r:
			if b in cdklt_r:
				devlt_r.remove(b)
	clean_lt = set(devlt_r)
	return(list(set(clean_lt)))
def dd_null(dev_s, sudo_s): # This function calls dd from device to /null.
	dd_str= "dd if=/dev/" +dev_s +" of=/dev/null &"
	cmd_out(2, dd_str, sudo_s)
	return None
def dd_zero(dev_s, sudo_s): # This function calls dd from /zero to device. 
	dd_str= "dd if=/dev/zero of=/dev/" +dev_s+ " bs=1M &"
	cmd_out(2, dd_str, sudo_s)
	return None	
def find_dd(): # This function uses ps to find PID's of active dd jobs.
	dd_snif= cmd_out(3, "ps -a", '')
	dd_snif= re.split('\n+', dd_snif)
	dd_active= []
	dd_hld= ''
	for x in range(len(dd_snif)):
		if "dd" in dd_snif[x]:
			dd_hld= re.split('\s+', dd_snif[x])
			dd_active.append(dd_hld[1])
	return(dd_active)
def progress_dd(pid_dd, sudo_s): # This tracks disk progress for dd.
	trigr= cmd_out(3, "progress -qdw -c dd", sudo_s)
	mitgr= ''
	if trigr != '':
		global status_var
		for x in range(len(pid_dd)):
			mitgr= 'progress -qdw -p ' + pid_dd[x]
			status_var.append(str(re.split
                         ("\n",(cmd_out(3, mitgr, sudo_s)))))
		return None
def status_update(sudo_s): # This generates persistent update to terminal.
	while cmd_out(3, "progress -qdw -c dd", sudo_s):
		progress_dd(find_dd(), sudo_s)
		with output(initial_len=len(status_var), interval=0) as output_lines:	
			for x in range(len(status_var)):
				output_lines[x] = str(status_var[x])
			time.sleep(1.75)
	return None
def skull_cross(): # This lets you know this software kills... Data...
	print(r"""                       ______
                    .-"      "-.
                   /    DDz     \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "x._     | )( */  \*_)( |     _.f" <
      (_/"x._"x._ |/     /\     \| _.f"_.f"\_)
             "x._ (_     ^^     _)"_.f"
                 "x\__|IIIDII|__/f"
                _.v"| \IIIIII/ |"z._
      _     _.v"_.v"\          /"z._"z._     _
     ( \_.v"_.v"     `--------`     "z._"z._/ )
      > _.v"                            "z._ <
     (_/                                    \_)
     """)
def root_dt1():
	if (uname().lower == "root"):
		run_me= ''
	else:
		run_me= raw_input('Please provide sudo password: ')
	return(run_me)
def print_dk():
	for x in range(len(format_dk())):
		print(format_dk()[x] + " is not mounted.")
	return None
def ddn_dk(sudo_s):
	for x in range(len(format_dk())):
		dd_null(format_dk()[x], sudo_s)
	return None	
def ddz_dk(sudo_s):
	for x in range(len(format_dk())):
		dd_null(format_dk()[x], sudo_s)
	return None
def guide_wp(sudo_s):
	final_lt= []
	for x in range(len(format_dk())):
		msg= "Type y to mark disk " + format_dk()[x] + "  :: "
		if(raw_input(msg) == 'y'):
			final_lt.append(format_dk()[x])
	for x in range(len(final_lt)):
		dd_null(final_lt[x], sudo_s)
        time.sleep(3)
       	status_update(sudo_s)
       	return None
if (__name__ == '__main__' and uname().lower == 'linux'):
	if(len(argv)<2):
		exit()
	elif (argv[1] == "-h" or argv[1] == "--help"):
		print("This program tries to predict unmounted drives and zero them.")
		print("-a will auto zero all unmounted drives.")
		print("-g will enter guided mode, and ask to mark each drive.")
		print("-l will list the drives and mount points predicted by automode")
		print("-t will run in auto mode and dd drives to /dev/null")	
	elif (argv[1] == "-l"):
		print_dk()
	elif (argv[1] == "-t" and len(argv) < 3):
		run_me= root_dt1()
		print_dk()
		ddn_dk(run_me)
	elif (argv[1] == "-t"):
        	run_me= argv[2]
        	print_dk()
		ddn_dk(run_me)
	elif (argv[1] =="-a" and len(argv) <3):
		skull_cross()
		print("DDZ Running in auto!")
		run_me= root_dt1()
        	print_dk()	
        	ddz_dk(run_me)
        	time.sleep(3)
        	status_update(run_me)	
	elif (argv[1] =="-a"):
		skull_cross()
		print("DDZ Running in auto!")
		run_me= argv[2]
		print_dk()
		ddz_dk(run_me)
        	time.sleep(3)
        	status_update(run_me)
	elif(argv[1] =="-g" and len(argv) <3):
		skull_cross()
		print("DDZ is Running in guided mode!")
		run_me= root_dt1()
		print_dk()
		guide_wp(run_me)
	elif(argv[1] =="-g"):
		skull_cross()
		print("DDZ is Running in guided mode!")
		run_me= argv[2]
		print_dk()
		guide_wp(run_me)
	elif(argv[1] == "-s"):
		skull_cross()
		exit()
###############################################################################	

