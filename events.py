#!/usr/bin/env python3
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
        load_data = open("data.yaml", "r")
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
    
    
        
    
    
if __name__ == '__main__':
    mode = 'personal'
    today = datetime.datetime.today()
    ev = Event(today, mode)
    ev.renungan()
    ev.reminder()
    
