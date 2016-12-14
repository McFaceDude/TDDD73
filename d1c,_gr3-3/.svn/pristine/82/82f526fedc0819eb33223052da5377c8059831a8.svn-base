from calendar_ADT import *
from calendar import *
from output import *

#Code that should be in calendar.py in the Interface section

def remove(cal_name, d, m, t1):
    "String x Integer x String x String ->"
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t1)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    print("Calendar day:", cal_day)
    if is_booked_from(cal_day, start):
        print("Remove that booii!")

        remove_appointment(fetch_calendar(cal_name), day, mon, start)

    else:
        print("There is no appointment at that time.")



#Code that should be in booking.py in the second section



def remove_appointment(cal_year, day, mon, start):
    "calendar_year x day x month x time -> calendar_year"
    print("remove_appointment func")
    cal_day = calendar_day(day, calendar_month(mon, cal_year))
    print("appintment:", get_appointment_with_start_time(cal_day, start))
    app = get_appointment_with_start_time(cal_day, start)
   

#Code that should be in booking.py in the first section

        

#Code that should be in calendar_ADT.y in the iterator fucntion
def get_appointment_with_start_time(cal_day, start):
    "cal_day x time -> appointment"
    appointment_pred = lambda app: is_same_time(start, start_time(get_span(app)))
    if is_empty_calendar_day(cal_day):
        return False
    elif appointment_pred(first_appointment(cal_day)):
        print("not that")
        return first_appointment(cal_day)
    else:
        return some_meeting_satisfies(rest_calendar_day(cal_day),
                                      appointment_pred)



create("Jayne")
book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
book("Jayne", 20, "sep", "16:00", "17:00", "Rob train")
show("Jayne", 20, "sep")

remove("Jayne", 20, "sep", "15:00")
show("Jayne", 20, "sep")

