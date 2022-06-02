# Program to modify text
text = "thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado...-agrega el comentarista"

""" text variable is split to work with small phrases"""
text_list = text.split("#")

""" phrases are modify accordingly """
first_phrase = text_list[0].capitalize() + "...\n\n"
flash_uppercase = text_list[1][:1].upper()
second_phrase = "- ¡" + flash_uppercase + text_list[1][1:] + ".\n"
third_phrase = "- " + text_list[2][:1].upper() + text_list[2][1:] + ".\n"
fourth_phrase = "- " + flash_uppercase + text_list[3][1:] + "."

print(first_phrase + second_phrase + third_phrase + fourth_phrase)