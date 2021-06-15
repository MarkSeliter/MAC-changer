#!/usr/bin/env python

# this python2 program uses the program 'ip' and not 'ifconfig'.


import subprocess
import optparse


def main():

	parser = optparse.OptionParser()

	print('[+] turning ' + inter + ' down...')

	# system call to turn the interface down
	subprocess.call(['ip', 'link', 'set', 'dev', inter, 'down'])
	
	print('[+] setting MAC address of ' + mac_addr + ' on the interface ' + inter)

	# for now hardcoded the MAC which it will change to
	subprocess.call(['ip', 'link', 'set', 'dev', inter, 'address', mac_addr])


	print('[+] turning ' + inter + ' back up')

	# system call to turn the interface up
	subprocess.call(['ip', 'link', 'set', 'dev', inter, 'up'])

	print('[+] Done')
	print('-' * 50)

	# display the result
	subprocess.call(['ip', 'link', 'show', inter])


def help():

	print('test')
	print('test')
	print('test')
	print('test')


if __name__== '__main__':

	main()
