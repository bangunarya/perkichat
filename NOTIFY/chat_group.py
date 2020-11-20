#! /usr/bin/env python3
import requests, json
import datetime


##------------------------Global Variables-------------------------------##

URL = "https://notify-api.line.me/api/notify"


def getToken(mode):
    import yaml
    
    token_file = open("token.yaml", "r")
    parsed_yaml = yaml.load(token_file, Loader=yaml.FullLoader)
    return parsed_yaml['tokens'][mode]

def send_message(token, msg, img=None):
    message = {'message': msg}
    LINE_HEADERS = {'Authorization': 'Bearer ' + token}
    files = {'imageFile': open(img, 'rb')} if img else None
    session = requests.Session()
    resp = session.post(URL, headers=LINE_HEADERS, params=message, files=files)
    if files:
        files['imageFile'].close()
    return resp.status_code



def main():
    import os
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(
            description="Send LINE Message.")
    
    parser.add_argument('--img_file', help="Image File to be sent", default = None)
    parser.add_argument('message')
    parser.add_argument('-m','--mode', dest = "mode", help="perki/test", default ="personal")

    args = parser.parse_args()
    token = getToken(args.mode)
    status_code = send_message(token,args.message,args.img_file)
    print('Status Code = {}'.format(status_code))


if __name__ == '__main__':
    main()
