from calendar_ADT import *

create("Mal")
create("River")

create("Jayne")
book("Jayne", 20, "sep", "12.00", "14.00", "Rob train")
book("Jayne", 20, "sep", "15.00", "16.00", "Escape with loot")
show("Jayne", 20 , "sep")
show_calendars()
save("testdata")
load("testdata")

t1315 = new_time(new_hour(8), new_minute(15))
print(t1315)

new_subject("samuel")
day = new_calendar_day()
cd15 = new_day(15)

ts0830 = new_time_span(new_time(new_hour(9), new_minute(30)), new_time(new_hour(10), new_minute(30)))
ts0900 = new_time_span(new_time(new_hour(7), new_minute(0)), new_time(new_hour(10), new_minute(00)))


"""
7A
"""


def start_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return earliest_time(strip_tag(ts)[0], strip_tag(ts)[1])

def end_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return latest_time(strip_tag(ts)[0], strip_tag(ts)[1])

def overlap(ts1, ts2):
    "span x span -> span"
    return new_time_span(latest_time(start_time(ts1), start_time(ts2)), 
        earliest_time(end_time(ts1), end_time(ts2)))

def new_duration(hour, minute):
    "hour × minute -> duration"
    ensure(hour, is_hour)
    ensure(minute, is_minute)
    minutes_in_an_hour = 60
    return attach_tag('duration', (new_hour(get_integer(hour) + get_integer(minute) // minutes_in_an_hour), 
        (new_minute(get_integer(minute) % minutes_in_an_hour))))

def length_of_span(ts):
    "span -> duration"
    ensure(ts, is_time_span)
    minutes_in_an_hour = 60
    mins = get_integer(get_minute(end_time(ts))) + get_integer(get_hour(end_time(ts)))*minutes_in_an_hour -\
    get_integer(get_minute(start_time(ts))) - get_integer(get_hour(start_time(ts)))*minutes_in_an_hour

    return (new_duration(new_hour(mins//minutes_in_an_hour), (new_minute(mins%minutes_in_an_hour))))
