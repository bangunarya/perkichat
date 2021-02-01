#!/usr/bin/env python3
import requests
import datetime
import numpy as np
import yaml
from pathlib import Path
from perkichat import PerkiChat as pc

class Renungan:
    
    def __init__(self, today, chatter):
        self.today = today
        self.chatter = chatter
    
      
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
        idx = np.int(self.today.strftime("%d"))#np.random.randint(len(ayat))
 
        ## parameters
        msg = 'Renungan: ' + ayat[idx]
        img = None
    
        ## Create instance of perkichat
        status_code = self.chatter.send_message(msg,img)
        print('Status Code = {}'.format(status_code))
        
        

    
if __name__ == '__main__':
    mode = 'arya'
    today = datetime.datetime.today()
    chatter = pc(mode)
    ren = Renungan(today, chatter)
    ren.renungan()
    