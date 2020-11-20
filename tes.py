#! /usr/bin/env python3

import requests, json
import datetime
import random
 
token = "iis96ihAcH7wPoTZQpBymGCcz1JTIVSv75USzXWBoYB" # isi token grup



pagi = {0:'Selamat pagi teman-teman! Disela kesibukanNya Yesus selalu memiliki waktu berelasi dengan BapaNya (Mark 1:35). Bagaimana dengan kita?',
        1:'Selamat pagi teman-teman! Jangan lupakan persekutuan dengan Tuhan, karena Ia menanti kita untuk bersekutu denganNya! (Wahyu 3:20)',
        2:'Dipagi ini mari kita nyatakan kerinduan kita seperti nyanyian pengajaran bani Korah (Maz 42:2), Seperti rusa yang merindukan sungai berair, demikianlah jiwa kita merindukan Tuhan!',
        3:'Selamat pagi teman-teman, Tuhan Yesus sudah memberikan damai sejahteraNya bagi kita dan yang Ia berikan tidak seperti yang diberikan dunia ini. Hendaknya kita jangan gelisah dan gentar dalam menghadapi hari ini (Yoh 14:27)',
        4:'Selamat pagi! Marilah kita berkata seperti Daniel (Dan 2:20). Terpujilah nama Tuhan dari selama-lamanya sampai selama-lamanya, sebab dari pada Dialah hikmat dan kekuatan kita!',
        5:'Selamat pagi! Tuhanlah gembala kita yang menuntun kita di hari ini sehingga kita tidak akan pernah kekurangan (Maz 23:1)',
        6:'Selamat pagi! Sebelum memulai hari ini mari kita merenungkan bagaimana hari ini kita melakukan segala sesuatu di hari ini untuk Tuhan bukan untuk manusia (Kol 3:23)'}

malam = {0:'Dunia bisa mengecewakan, hari ini mungkin kita punya kekecewaan dan kegagalan. Tapi Tuhan tetap setia (2 Tim 2:13). Mari datang dan nyatakan keluh kesah kita kepadaNya!',
         1: 'Mari kita melihat kembali hari kita hari ini, dalam hal apa yang kita bisa syukuri dan menghitung hari kita agar kita beroleh hati yang bijaksana (Maz 90:12)',
         2: 'Mari kita mengucap syukur akan hari ini, sebab itulah yang dikehendaki Allah didalam Kristus bagi kita (1 Tes 5:18)',
         3: 'Bagaimanapun hari kita, Allah bekerja dalam segala sesuatu untuk mendatanggkan kebaikan bagi kita jika kita mengasihi Dia, yang terpanggil dalam rencana Allah (Roma 8:28)',
         4: 'Meskipun hari kita mengecewakan, ataupun tidak menyenangkan, mari kita berkata seperti nabi Habakuk (Hab 3:17-18). Aku akan bersuka cita selalu sebab Engkau Tuhan Allah penyelamatku.',
         5: 'Bagaimanapun hari ini, kita tahu bahwa dalam persekutuan dengan Tuhan jerih payah kita tidak sia-sia (1 Kor 15:58)'}


idx_pgi = random.randint(len(pagi))
idx_mlm = random.randint(len(malam))



def perkiselamatpagi():
    LINE_ACCESS_TOKEN = token

    url = "https://notify-api.line.me/api/notify"
    msg = {"message": pagi[idx_pgi]} #message
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    resp =session.post(url, headers=LINE_HEADERS, data=msg)
    print(resp.text)



def perkiselamatmalam():
    LINE_ACCESS_TOKEN = token

    url = "https://notify-api.line.me/api/notify"
    msg = {"message": malam[idx_mlm]} #message
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    resp =session.post(url, headers=LINE_HEADERS, data=msg)
    print(resp.text)





def perkipd():
    LINE_ACCESS_TOKEN = token 

    url = "https://notify-api.line.me/api/notify"
    msg = {"message":" Halo teman-teman, hari ini kita ada persekutuan doa loh! Buat yang di Jülich dan Aachen ikutan yaa!"} #message
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    resp =session.post(url, headers=LINE_HEADERS, data=msg)
    print(resp.text)


def perkipa():
    LINE_ACCESS_TOKEN = token 

    url = "https://notify-api.line.me/api/notify"
    msg = {"message":" Halo-teman-teman, hari ini kita ada pendalaman alkitab/ibadah loh! Yuk join kita bersekutu bersama!"} #message
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    resp =session.post(url, headers=LINE_HEADERS, data=msg)
    print(resp.text)



today = datetime.datetime.today().weekday()
jam = datetime.datetime.today().hour

if jam < 11:
    perkiselamatpagi()
else:
    perkiselamatmalam()


#perkiselamatpagi()
if today == 4:
    perkipd()

elif today == 5:
    perkipa()

else:
    pass



