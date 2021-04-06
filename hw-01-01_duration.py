# минута = 60
# час = 3600
# сутки = 86400
# месяц (30 дней) = 2592000
# год (невисокосный) = 31536000

try:
    seconds = int(input("Введите время в секундах: "))
    if seconds < 60:
        print("%d сек" % (seconds % 60))
    elif seconds < 3600:
        print("%d мин %d сек" % (seconds // 60, seconds % 60))
    elif seconds < 86400:
        print("%d час %d мин %d сек" % (seconds // 3600, seconds % 3600 // 60, seconds % 60))
    elif seconds < 2592000:
        print("%d сут %d час %d мин %d сек" % (seconds // 86400, seconds % 86400 // 3600, seconds % 3600 // 60, seconds % 60))
    elif seconds < 31536000:
        print("%d мес %d сут %d час %d мин %d сек" % (seconds // 2592000, seconds % 2592000 // 86400, seconds % 86400 // 3600, seconds % 3600 // 60, seconds % 60))
    else:
        print("%d лет %d мес %d сут %d час %d мин %d сек" % (seconds // 31536000, seconds % 31536000 % 2592000, seconds % 2592000 // 86400, seconds % 86400 // 3600, seconds % 3600 // 60, seconds % 60))
except ValueError:
    print("Введено не число")
