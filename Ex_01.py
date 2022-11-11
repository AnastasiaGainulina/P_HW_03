# Напишите программу, удаляющую из текста все слова, 
# в которых присутствуют все буквы "абв"

text_original = 'Этот текс содержит лишние символы абв, программа должна удалить символы абв,\
     чтобы остался только текст без всяких символов абв'

def del_letters(text_original):
    text_original = list(filter(lambda x: 'абв' not in x, text_original.split()))
    return " ".join(text_original)

text_original = del_letters(text_original)
print(text_original)
