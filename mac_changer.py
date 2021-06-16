#!/usr/bin/python

# this python2 program uses the program 'ip' and not 'ifconfig'.


import subprocess
import optparse
import random

def main():
    # creating parser object
    parser = optparse.OptionParser()

    # options for the parser
    parser.add_option('-i', '--interface', dest='interface', help="interface to change it's MAC address")
    parser.add_option('-m', '--mac-addr', dest='mac_address', help="specify which MAC address to use")
    parser.add_option('-r', '--random', action='store_true' , dest='random_mac', default=True, help="generate a random MAC address (default)")

    # output the options and arguments into options and args
    (options, args) = parser.parse_args()

    # check if we got an interface option
    if not options.interface:
        print('please specify an interface to change it\'s MAC address')
        quit()

    # if we did then it will pass it into a var
    interface = options.interface

    # check if we got random as an arg
    if options.random_mac:
        # define a var to store the random MAC address
        random_mac = str()

        # generate 6 random 1 byte sized hex numbers
        for i in range(0, 6):
            # rgenerate random byte sized number
            num = random.randrange(0, 255, 1)

            # if the number has only 1 digit
            if num < 10:
                num = int('0' + str(num))

            random_mac = random_mac + str(hex(num)[2:]) + ':'

        # return the result without the last column
        mac_address = random_mac[:-1]

    # if not random then the specified MAC
    elif options.mac_address:
        mac_address = options.mac_address

    # if we didn't get either, ask user to specify either MAC or RANDOM and quit
    else:
        print('please specify a MAC address or use the --random (-r) option')
        quit()

    change_mac(interface, mac_address)


def change_mac(inter, mac):
    print('[+] turning ' + inter + ' down...')

    # system call to turn the interface down
    subprocess.call(['ip', 'link', 'set', 'dev', inter, 'down'])

    print('[+] setting MAC address of ' + mac + ' on the interface ' + inter)

    # for now hardcoded the MAC which it will change to
    subprocess.call(['ip', 'link', 'set', 'dev', inter, 'address', mac])

    print('[+] turning ' + inter + ' back up')

    # system call to turn the interface up
    subprocess.call(['ip', 'link', 'set', 'dev', inter, 'up'])

    print('[+] Done')
    print('-' * 50)

    # display the result
    subprocess.call(['ip', 'link', 'show', inter])


if __name__ == '__main__':
    main()
