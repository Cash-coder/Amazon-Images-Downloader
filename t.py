title = 'Samsung Smartphone Galaxy waca S20+ FE con Pantalla Infinity-O FHD+ de 6,5 Pulgadas, 8 GB de RAM y 256 GB de Memoria Interna Ampliable, Batería de 4500 mAh y Carga rápida Azul (Version ES)'
title = title.lower()

item_p = 'samsung galaxy s20+'
attribute_p = 'azul'

s = item_p.split(' ')
n = len(s)

if n == 1:
    pass
elif n == 2:
    pass
elif n == 3:
    if s[0] in title:
        if s[1] in title:
            if s[2] in title:
                print('correct')


# if title in splitted and attribute_p in title:
#     #if prod.text not in ['Carcasa', 'Funda', 'Protector', 'Soporte'] :
#     #if 'Carcasa' and 'Funda' and 'Protector' and 'Soporte' not in prod.text:
#     if 'carcasa' not in title and 'funda' not in title and 'protector' not in title and 'soporte' not in title:
#         print('match')
# else:
#     print('not found:')
#     print(r"\n")