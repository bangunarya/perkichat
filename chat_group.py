#! /usr/bin/env python3
import requests, json
import datetime



##------------------------Global Variables-------------------------------##

URL = "https://notify-api.line.me/api/notify"
#TODO
token = "iis96ihAcH7wPoTZQpBymGCcz1JTIVSv75USzXWBoYB"
#token = "DpOhVLboPeFIS4MbGoALTkyLMyjfyCkLBaK57P16dx8"

#LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+ token}
LINE_HEADERS = {'Authorization': 'Bearer ' + token}

def send_message(token, msg, img=None):
    message = {'message': msg}
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

    args = parser.parse_args()
    status_code = send_message(token,args.message,args.img_file)
    print('Status Code = {}'.format(status_code))


if __name__ == '__main__':
    main()
