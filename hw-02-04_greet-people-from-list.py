list_of_persons = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for person_info in list_of_persons:
    print(f'Привет, {person_info.split()[-1].capitalize()}')
