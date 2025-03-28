def schedule_reminder(cls):
    class jadwal(cls):
        def __init__(self, activity, date):
            super().__init__(activity, date)
            self.date = date
            self.activity = activity
            print(f" Reminder: Jangan lupa jadwal '{self.activity}' pada {self.date}!")
    return jadwal

@schedule_reminder
class Schedule:
    def __init__(self, activity, date):
        self.activity = activity
        self.date = date

s1 = Schedule("Tugas SOJAR", "27 Maret 2025, 11:59 PM")
s2 = Schedule("Laporan PBO", "01 April 2025, 11:59 PM")
