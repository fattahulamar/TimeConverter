#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Detikstr(detik): #buat function
    if detik <=359999: #buat input tidak lebih dari 359999
        HH = (detik)//3600 #buat perhitungan jam, // berfungsi seperti math floor 
        MM = (detik - HH*3600)//60 #buat perhitungan menit
        SS = detik - HH*3600 - MM*60 #buat perbandingan detik
        result=("{}:".format(HH) if HH else "") +         ("{}:".format(MM) if MM else "") +         ("{} ".format(SS) if SS else "")
        #result adalah pengabungan dari hasil perhitungan di atas dan formating menjadi string
        return result
    else: #hasil yang keluar jika angka yang di masukan lebih dari 359999
        print('error')
print(Detikstr(int(input('masukan angka: '))))


# In[ ]:




