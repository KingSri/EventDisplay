# # # datetime refers to a class to manipulate date and time, timedelta is the difference between date/time/datetime instance
# from datetime import datetime, timedelta
# from calendar import HTMLCalendar
# from .models import Event
#
# class Calendar(HTMLCalendar):
#     def __init__(self, year=None, month=None):
#         self.year = year
#         self.month = month
#         super(Calendar, self).__init__()
# # Breaking down into day, month, year
#     def dayformat(self,day,events):
#         day_events = event.filter(start_time__day = day)
#         e = ''
#         for event in day_events:
#             e += f'<li> {event.title} </li>'
#
#         if day != 0:
#             return f"<td><span class='date'>{day}</span><ul> {e} </ul></td>"
#         return '<td></td>'
#
#     def weekformat(self, weeks, task):
#         week = ''
#         for e, weekday in weeks:
#             week += self.dayformat(e, events)
#         return f'<tr> {week} </tr>'
#     def monthformat(self, withyear=True):
#         events = Event.objects.filter(
#         start_time__year = self.year,
#         start_time__month = self.month
#         )
#         cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
# 		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
# 		cal += f'{self.formatweekheader()}\n'
# 		for week in self.monthdays2calendar(self.year, self.month):
# 			cal += f'{self.formatweek(week, events)}\n'
# 		return cal
