#! /usr/bin/env python3
import requests
import datetime
import numpy as np
import yaml
from perkichat import PerkiChat as pc

class Event:
    
    def __init__(self, today, mode):
        self.today = today
        self.mode = mode
        
    def renungan(self):
        
        jam = self.today.hour
    
        if jam < 12:
            verse_choose = 'morningverse'
        else:
            verse_choose = 'eveningverse'
        
        ## load data
        load_data = open("./YAML/data.yaml", "r")
        data_yaml = yaml.load(load_data, Loader = yaml.FullLoader)
        ayat = data_yaml[verse_choose]
    
        ## choose random verse
        idx = np.random.randint(len(ayat))
 
        ## parameters
        msg = 'Renungan: ' + ayat[idx]
        img = None
    
        ## Create instance of perkichat
        chat = pc(self.mode)
        status_code = chat.send_message(msg,img)
        print('Status Code = {}'.format(status_code))
        
        
    def birthday_lister(self, today):
        """
        brief: Returns list of people who celebrates their birthday today
                todo: also returns corresponding pictures and ages?

        Parameters
        ----------
        today: today
            Today data

        """
        month = today.month
        date = today.day

        birthday_fn = './YAML/birthday.yaml'

        birthday_file = open(birthday_fn,'r')

        parsed_yaml = yaml.load(birthday_file, Loader = yaml.FullLoader)

        birthday_str = parsed_yaml[month][date]

        birthday_file.close()

        birthday_list = birthday_str.split(', ')

        return birthday_list
        
        

    def reminder(self):   
    
        today = self.today.weekday()
            
        ## parameters
        if today == 4:
            msg = 'Reminder: Halo teman-teman, hari ini kita ada persekutuan doa loh! Buat yang di Jülich dan Aachen ikutan yaa!'
            img = None
            ## Create instance of perkichat
            chat = pc(self.mode)
            status_code = chat.send_message(msg,img)
            print('Status Code = {}'.format(status_code))
        elif today == 5:
            msg = 'Reminder: Halo-teman-teman, hari ini kita ada pendalaman alkitab/ibadah loh! Yuk join kita bersekutu bersama!'
            img = None
            ## Create instance of perkichat
            chat = pc(self.mode)
            status_code = chat.send_message(msg,img)
            print('Status Code = {}'.format(status_code))
        elif today == 6:
            FeGBerlin = 'FEG Immanuel Berlin: https://www.youtube.com/channel/UCp6z_JJITkQIs4KPsEH4p_Q'
            FeGHamburg = ' FEG Maranatha Hamburg: https://www.youtube.com/channel/UCbvRyQOQLV3InmOHt0eu3QQ'
            msg = ('Reminder: Selamat hari minggu teman-teman! Sudahkah beribadah hari ini? Beberapa link ibadah yang ada: ' +
                   FeGBerlin + FeGHamburg)   
            img = None
            ## Create instance of perkichat
            chat = pc(self.mode)
            status_code = chat.send_message(msg,img)
            print('Status Code = {}'.format(status_code))
        
        else:
            pass

        #---------- Birthday reminder(s) -------------#

        import random

        birthday_greeting = [
                'Happy birthday buat {}! Kami mendoakan semoga kamu semakin bertumbuh dan diberkati di dalam Tuhan!',
                'Selamat ulang tahun buat teman kita tercinta {}! Tuhan memberkati dan terus bertumbuh di dalam-Nya!',
                'Hari ini adalah hari yang spesial karena teman kita {} berulangtahun! God bless you dan terus kejarlah kemuliaan Kristus di dalam hidupmu!' 
                ]

        birthday_list = self.birthday_lister(self.today)

        if birthday_list != ['']: #Ada yang berulang tahun
            for names in birthday_list:
                birthday_msg = random.choice(birthday_greeting).format(names)
                birthday_img = None
                chat = pc(self.mode)
                status_code = chat.send_message(birthday_msg,birthday_img)
                print('Status code = {}'.format(status_code))

        
    
    
if __name__ == '__main__':
    mode = 'personal'
    today = datetime.datetime.today()
    ev = Event(today, mode)
    ev.renungan()
    ev.reminder()
    
