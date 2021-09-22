print('Ibu berkata : "Beli 1 Susu. Jika ada telur, Beli 6 Telur"')

Milk = int(input('Jumlah Susu di Toko = '))
Egg = int(input('Jumlah Telur di Toko = '))


if Milk >= 1:
    if Egg >= 6 or Egg >=1 <6 :
        print(f'Kamu membeli 1 Susu dan {Egg} Telur')
    else:
        print(f'Kamu membeli 1 Susu, tetapi tidak membeli Telur')

else:
    if Egg >= 6 or Egg >=1 <6 :
        print(f'Kamu tidak membeli Susu, tetapi membeli {Egg} Telur')
    else:
        print('Kamu tidak membeli Susu dan Telur')


