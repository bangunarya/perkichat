#! /usr/bin/env python3
import requests
import os
import sys
import argparse
from perkichat import PerkiChat as pc


def main():

    ## call parse argument
    parser = argparse.ArgumentParser(
            description="Send LINE Message.")

    parser.add_argument('--img_file', help="Image File to be sent", default = None)
    parser.add_argument('message')
    parser.add_argument('-m','--mode', dest = "mode", help="perki/test", default ="personal")

    args = parser.parse_args()
    
    ## Create instance of perkichat
    chat = pc(args.mode)
    status_code = chat.send_message(args.message,args.img_file)
    print('Status Code = {}'.format(status_code))


if __name__ == '__main__':
    main()             
