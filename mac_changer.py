#!/usr/bin/env python

import subprocess

def main(interface, mac):

	# keep track if everything went smoothly
	fail = False


	print('[+] turning {interface} down...')

	# system call to turn the interface down
	try:
		subprocess.call('ip link set dev {interface} down', shell=True)
	
	# on fail
	except:
		fail = True
		print('[!] please enter a valid interface')

	
	print('[+] setting MAC address of {mac} on the interface {interface}')

	# for now hardcoded the MAC which it will change to
	try:
		subprocess.call('ip link set dev eth0 address {mac}', shell=True)

	# on fail
	except:
		fail = True
		print('[!] please enter a valid MAC address')


	print('[+] turning eth0 back up')

	# system call to turn the interface up
	try:
		subprocess.call('ip link set dev eth0 up', shell=True)

	# on fail
	except:
		fail = True
		print('[!] something went wrong, could not turn {interface} back up')


	# feedback if program ran successfully
	if fail:
		print('[!] stopped')
	else:
		print('[+] done')


if __name__== '__main__':
	main(interface, main)

