#!/usr/bin/env python3
import requests
import datetime
import numpy as np
import yaml
from pathlib import Path
from perkichat import PerkiChat as pc

class Reminder:
    
    def __init__(self, today, chatter):
        self.today = today
        self.chatter = chatter
        
    
    def birthdayreminder(self):
        """
        brief: Returns list of people who celebrates their birthday today
                todo: also returns corresponding pictures and ages?

        Parameters
        ----------
        today: today
            Today data

        """
        import random

        month = self.today.month
        date = self.today.day

        birthday_fn = Path(__file__).resolve().parent.parent / 'YAML' / 'birthday.yaml'

        birthday_file = open(birthday_fn,'r')

        parsed_yaml = yaml.load(birthday_file, Loader = yaml.FullLoader)

        birthday_str = parsed_yaml[month][date]

        birthday_file.close()

        birthday_list = birthday_str.split(', ')

           #---------- Birthday reminder(s) -------------#

        birthday_greeting = [
                'Happy birthday buat {}! Kami mendoakan semoga semakin bertumbuh dan diberkati di dalam Tuhan!',
                'Selamat ulang tahun buat saudara kita tercinta {}! Tuhan memberkati dan terus bertumbuh-lah di dalam-Nya!',
                'Hari ini adalah hari yang spesial karena saudara kita {} berulangtahun! God bless you dan terus kejarlah kemuliaan Kristus di dalam hidupmu!'
                ]

        #birthday_list = self.birthday_lister(self.today)

        if birthday_list != ['']: #Ada yang berulang tahun
            for names in birthday_list:
                birthday_msg = random.choice(birthday_greeting).format(names)
                birthday_img = None
                status_code = self.chatter.send_message(birthday_msg,birthday_img)
                print('Status code = {}, birthday message for today sent!'.format(status_code))

       

    def eventreminder(self):   
    
        today = self.today.weekday()
            
        dailyReminder = True
        ## parameters
        if today == 4:
            msg = 'Reminder: Halo teman-teman, hari ini kita ada persekutuan doa (pd) loh! Buat yang di Jülich dan Aachen ikutan yaa! pd Aachen jam 18:30 jam. Link zoom : https://rwth.zoom.us/j/6252110893?pwd=ZmJYb09qNklaZEhRb0czTm1jSnpXQT09'
            img = None
        elif today == 5:
            msg = 'Reminder: Halo-teman-teman, hari ini kita ada pendalaman alkitab/ibadah loh jam 15:00! Yuk join kita bersekutu bersama! Link zoom : https://rwth.zoom.us/j/6252110893?pwd=ZmJYb09qNklaZEhRb0czTm1jSnpXQT09'
            img = None
        elif today == 6:
            FeGBerlin = 'FEG Immanuel Berlin: https://www.youtube.com/channel/UCp6z_JJITkQIs4KPsEH4p_Q'
            FeGHamburg = ' FEG Maranatha Hamburg: https://www.youtube.com/channel/UCbvRyQOQLV3InmOHt0eu3QQ'
            msg = ('Reminder: Selamat hari minggu teman-teman! Sudahkah beribadah hari ini? Beberapa link ibadah yang ada: ' +
                   FeGBerlin + FeGHamburg)   
            img = None
        else:
            dailyReminder = False

        if(dailyReminder):
            status_code = self.chatter.send_message(msg,img)
            print("Today's event reminder set with a status code of {}".format(status_code))
   


    
if __name__ == '__main__':
    mode = 'arya'
    today = datetime.datetime.today()
    chatter = pc(mode)
    re = Reminder(today, chatter)
    if today.hour < 12:
        re.birthdayreminder()
    else:
        re.eventreminder()

    