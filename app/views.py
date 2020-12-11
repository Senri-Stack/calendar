import calendar

import datetime
from django.shortcuts import redirect
from django.views import generic
from .models import Schedule

class Monthcalendar:
    first_weekday = 0

    def setup_calendar(self):
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_next_month(self, date):
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(month=date.month+1, day=1)

    def get_month_days(self, date):
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_current_month(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')

        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        self.setup_calendar()
        current_month = self.get_current_month()
        week_names = ['月', '火', '水', '木', '金', '土', '日']
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'current_month': current_month,
            'month_next': self.get_next_month(current_month),
            'week_names':week_names
        }
        return calendar_data

class MyCalendar(Monthcalendar, generic.TemplateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'app/month.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context