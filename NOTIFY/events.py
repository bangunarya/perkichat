#!/usr/bin/env python3
import requests
import datetime
import numpy as np
import yaml
from pathlib import Path
from perkichat import PerkiChat as pc

class Event:
    
    def __init__(self, today, chatter):
        self.today = today
        self.chatter = chatter
        
    def renungan(self):
        
        jam = self.today.hour
    
        if jam < 12:
            verse_choose = 'morningverse'
        elif jam == 12:
            #------------ Article From Desiring God ---------#

            article_msg = 'Selamat siang guys, berikut ini ada link article dari Desiring God. Semoga menjadi berkat bagi kita semua!\n{}'.format(self.article_dg())
            status_code = self.chatter.send_message(article_msg,None)
            print('Desiring God article link sent with a status code of {}'.format(status_code))

            # Don't send verse for noon message
            return
        else:
            verse_choose = 'eveningverse'
        
        ## load data
        data_fn = Path(__file__).resolve().parent.parent / 'YAML' / 'data.yaml' 
        load_data = open(data_fn,'r')
        data_yaml = yaml.load(load_data, Loader = yaml.FullLoader)
        ayat = data_yaml[verse_choose]
    
        ## choose random verse
        idx = np.random.randint(len(ayat))
 
        ## parameters
        msg = 'Renungan: ' + ayat[idx]
        img = None
    
        ## Create instance of perkichat
        status_code = self.chatter.send_message(msg,img)
        print('Status Code = {}'.format(status_code))
        
        
    def article_dg(self):
        """
        brief: Returns featured article link from Desiring God

        Parameters
        ----------
         - 
        """

        from bs4 import BeautifulSoup

        url = 'https://www.desiringgod.org'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        a = soup.find('a', attrs = {'class':'featured-resource__link'})
        ext = a.get('href')

        return url+ext

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

        birthday_fn = Path(__file__).resolve().parent.parent / 'YAML' / 'birthday.yaml'

        birthday_file = open(birthday_fn,'r')

        parsed_yaml = yaml.load(birthday_file, Loader = yaml.FullLoader)

        birthday_str = parsed_yaml[month][date]

        birthday_file.close()

        birthday_list = birthday_str.split(', ')

        return birthday_list
        
        

    def reminder(self):   
    
        today = self.today.weekday()
            
        dailyReminder = True
        ## parameters
        if today == 4:
            msg = 'Reminder: Halo teman-teman, hari ini kita ada persekutuan doa loh! Buat yang di Jülich dan Aachen ikutan yaa!'
            img = None
        elif today == 5:
            msg = 'Reminder: Halo-teman-teman, hari ini kita ada pendalaman alkitab/ibadah loh! Yuk join kita bersekutu bersama!'
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
        #---------- Birthday reminder(s) -------------#

        import random

        birthday_greeting = [
                'Happy birthday buat {}! Kami mendoakan semoga semakin bertumbuh dan diberkati di dalam Tuhan!',
                'Selamat ulang tahun buat saudara kita tercinta {}! Tuhan memberkati dan terus bertumbuh-lah di dalam-Nya!',
                'Hari ini adalah hari yang spesial karena saudara kita {} berulangtahun! God bless you dan terus kejarlah kemuliaan Kristus di dalam hidupmu!' 
                ]

        birthday_list = self.birthday_lister(self.today)

        if birthday_list != ['']: #Ada yang berulang tahun
            for names in birthday_list:
                birthday_msg = random.choice(birthday_greeting).format(names)
                birthday_img = None
                status_code = self.chatter.send_message(birthday_msg,birthday_img)
                print('Status code = {}, birthday message for today sent!'.format(status_code))

    
if __name__ == '__main__':
    mode = 'test'
    today = datetime.datetime.today()
    chatter = pc(mode)
    ev = Event(today, chatter)
    if today.hour < 12:
        ev.reminder()
    ev.renungan()
    
