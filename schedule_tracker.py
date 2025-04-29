#This helps users track when medications should be taken and notifies the patient.
from datetime import datetime, timedelta

def generate_schedule(start_time, interval_hours, doses):
    schedule = []
    current_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    for _ in range(doses):
        schedule.append(current_time.strftime("%Y-%m-%d %H:%M"))
        current_time += timedelta(hours=interval_hours)
    return schedule
