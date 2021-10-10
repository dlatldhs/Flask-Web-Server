#Unicode Error catch code
import locale
locale.setlocale(locale.LC_ALL,'')

#format_datetime 함수 날짜 형식같은거 ?
def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime(fmt)