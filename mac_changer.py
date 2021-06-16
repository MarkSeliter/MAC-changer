#!/usr/bin/python

# this python2 program uses the program 'ip' and not 'ifconfig'.


import subprocess
import optparse
import random


def main():
    # get the options and args
    (options, args) = get_args()

    # check if we got an interface option
    if not options.interface:
        print('please specify an interface (-i) to change it\'s MAC address')
        return 1

    # if we did then it will pass it into a var
    interface = options.interface

    # if not random then the specified MAC
    if options.mac_address:
        mac_address = options.mac_address

    # check if we got random as an arg
    elif options.random_mac:
        mac_address = generate_random_mac()

    # if we didn't get either, ask user to specify either MAC or RANDOM and quit
    else:
        print('please specify a MAC address (-m / --mac-addr) or use the (-r / --random) option')
        return 2

    change_mac(interface, mac_address)
    return 0


# gets the options and arguments from the commandline
def get_args():
    # creating parser object
    parser = optparse.OptionParser()

    # options for the parser
    parser.add_option('-i', '--interface', dest='interface', help="interface to change it's MAC address")
    parser.add_option('-m', '--mac-addr', dest='mac_address', help="specify which MAC address to use")
    parser.add_option('-r', '--random', action='store_true' , dest='random_mac', help="generate a random MAC address")

    # return the options and arguments
    return parser.parse_args()


# changes the MAC address with system commands
def change_mac(inter, mac):
    print('[+] turning ' + inter + ' down...')

    # system call to turn the interface down
    check = subprocess.call(['ip', 'link', 'set', 'dev', inter, 'down'])

    # check if the command executed succesfully
    if check != 0:
        print('[!] couldn\'t turn ' + inter + ' down')
        return 3

    print('[+] setting MAC address of ' + mac + ' on the interface ' + inter)

    # for now hardcoded the MAC which it will change to
    check = subprocess.call(['ip', 'link', 'set', 'dev', inter, 'address', mac])

    # check if the command executed succesfully
    if check != 0:
        print('[!] couldn\'t set MAC address, please make sure it\'s a valid address')
        return 4


    print('[+] turning ' + inter + ' back up')

    # system call to turn the interface up
    subprocess.call(['ip', 'link', 'set', 'dev', inter, 'up'])

    # check if the command executed succesfully
    if check != 0:
        print('[!] couldn\'t turn ' + inter + ' back up')
        return 5


    print('[+] Done')
    print('-' * 50)

    # display the result
    check = subprocess.call(['ip', 'link', 'show', inter])

    # check if the command executed succesfully
    if check != 0:
        print('[!] couldn\'t display ' + inter)
        return 6


# generates random MAC address
def generate_random_mac():

    # define a string to store the result
    random_mac = str()

    # generate first unicast byte in the MAC address
    num = random.randrange(0, 255, 1)

    # checks if the last bit is multicast
    if num & 1 == 1:
        num -= 1

    # check if the num has only 1 digit in hex
    num = check_digit(num)

    # adds the first digit to the MAC
    random_mac = random_mac + num+ ':'

    # generate 5 additional random 1 byte sized hex numbers
    for i in range(0, 5):
        # rgenerate random byte sized number
        num = random.randrange(0, 255, 1)

        # if the number has only 1 digit in hex
        num = check_digit(num)

        random_mac = random_mac + num+ ':'

    # return the result without the last column
    result = random_mac[:-1]

    return result


# checks if a num has 1 digits
def check_digit(x):
    if x < 0x10:
        x = '0' + str(hex(x))[2:]
    
    else:
        x = str(hex(x))[2:]

    return x


if __name__ == '__main__':
    main()
