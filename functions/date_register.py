import datetime
def date_register():
  date_day_int = datetime.datetime.today().weekday() + 1
  day_str = ""
  img_day = ""
  match date_day_int:
    case 1:
      img_day, day_str = "1.png","Понедельник"
    case 2:
      img_day, day_str = "2.png","Вторник"
    case 3:
      img_day, day_str = "3.png","Среду"
    case 4:
      img_day, day_str = "4.png","Четверг"
    case 5:
      img_day, day_str = "5.png","Пятница"
    case 6:
      img_day, day_str = "6.png","Среду"

  s = datetime.datetime.now().strftime("%H,%M")
  return [img_day,day_str,s]