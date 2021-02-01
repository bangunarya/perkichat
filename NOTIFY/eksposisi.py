#!/usr/bin/env python3
import requests
import datetime
import numpy as np
import yaml
from pathlib import Path
from perkichat import PerkiChat as pc

class Eksposisi:
    
    def __init__(self, today, chatter):
        self.today = today
        self.chatter = chatter
    
       
    def poin(self):
        
        jam = self.today.hour
    
        if jam > 12:
            verse_choose = 'eveningverse2'
            ## load data
            data_fn = Path(__file__).resolve().parent.parent / 'YAML' / 'data.yaml' 
            load_data = open(data_fn,'r')
            data_yaml = yaml.load(load_data, Loader = yaml.FullLoader)
            ayat = data_yaml[verse_choose]
            
            ## verse
            idx = np.int(self.today.strftime("%d"))#np.random.randint(len(ayat))
 
            ## parameters
            msg = 'Renungan: ' + ayat[idx]
            img = None

        else:
            try:
                book_choose = 'ezra'
                ## load data
                data_fn = Path(__file__).resolve().parent.parent / 'YAML' / 'kitab.yaml' 
                load_data = open(data_fn,'r')
                data_yaml = yaml.load(load_data, Loader = yaml.FullLoader)
                book = data_yaml[book_choose]
                 ## verse
                idx = np.int(self.today.strftime("%d"))#np.random.randint(len(ayat))
 
                ## parameters
                msg = 'Eksposisi: ' + book[idx]
                
                img = None
            except:
                verse_choose = 'morningverse'
                ## load data
                data_fn = Path(__file__).resolve().parent.parent / 'YAML' / 'data.yaml' 
                load_data = open(data_fn,'r')
                data_yaml = yaml.load(load_data, Loader = yaml.FullLoader)
                ayat = data_yaml[verse_choose]
            
                ## verse
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
    eks = Eksposisi(today, chatter)
    eks.poin()
    
