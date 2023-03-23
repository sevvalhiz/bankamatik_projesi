#bankamatik projesi
SevvalHesap= {
    'ad': 'Şevval Hız',
    'hesapNo': '123456',
    'bakiye': 3000,
    'ekHesap':2000
}
CevdetHesap= {
    'ad': 'Cevdet Sedef',
    'hesapNo': '156456',
    'bakiye': 6000,
    'ekHesap':3000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']} ")
    
    if hesap['bakiye'] >= miktar:
        hesap['bakiye']-= miktar
        print('Paranızı çekebilirsiniz.')
        bakiyeSorgula(hesap)
        
    else:
        toplam= hesap['bakiye']+hesap['ekHesap']
        
        if(toplam>= miktar):
            ekHesapKullanimi= input("Ek hesap kullanılsın mı?(evet/hayır) ")
            
            if ekHesapKullanimi== 'evet':
                ekHesapKullanilacakMiktar= miktar- hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-= ekHesapKullanilacakMiktar
                print('Paranızı çekebilirsiniz.')
                bakiyeSorgula(hesap)
                
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır ve ek hesabınızda {hesap['ekHesap']}TL bulunmaktadır.")
        
        else:
            bakiyeSorgula(hesap)
            yukleme= input('Üngünüz bakiyeniz yetersiz. Para yüklemek ister misiniz?(evet/hayır)')
            if yukleme == 'evet':
                miktar= int(input('Kaç TL yatırmak istersiniz?'))
                hesap['bakiye']+= miktar
                bakiyeSorgula(hesap)
                
            else:
                bakiyeSorgula(hesap)
                
            
            
            
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']}TL bulunmaktadır.")     

        
paraCek(SevvalHesap,7000)


