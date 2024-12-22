from datetime import datetime, timedelta
import Get_data
import Show_data 
import Png_to_gif

to_time = int(datetime.now().timestamp())
number_of_days = 10

for i in range(0, number_of_days):
    to_time = int(datetime.now().timestamp()) - i*86400
    from_time = to_time - 86400
    to_time = str(to_time)
    from_time = str(from_time)
    date = datetime.now() - timedelta(days = i)
    date = str(date.year) + " " + str((date.month)) + " " + str((date.day))
    Get_data.get_data(from_time, to_time)
    Show_data.show_data(i, date)

Png_to_gif.img_to_gif(number_of_days)