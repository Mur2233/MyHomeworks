secret_letter = [
    ['DFВsjl24sfFFяВАДОd24fssflj234'],  # Я
    ['asdfFп234рFFdо24с$#afdFFтasfо'], # ПРОСТО
    ['оafбasdf%^о^FFжа$#af243ю'], # ОБОЖАЮ
    ['afпFsfайFтFsfо13н'], # ПАЙТОН
    ['fн13Fа1234де123юsdсsfь'], # НАДЕЮСЬ
    ['чFFтF#Fsfsdf$$о'], # ЧТО
    ['и$ #sfF'], # И
    ['вSFSDам'], # ВАМ
    ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'], # ПОНРАВИТСЯ
    ['FFэasdfтDFsfоasdfFт'], # ЭТОТ
    ['FяDSFзFFsыSfкFFf']] # ЯЗЫК

small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

result = ''

for list_ in secret_letter:
    for string in list_:
        result += ' '
        for symbol in string:
            if symbol in small_rus:
                result += symbol
print(result)

exit_ = input('Для выхода из программы нажмите Enter ')