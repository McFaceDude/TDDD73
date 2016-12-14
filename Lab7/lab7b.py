from calendar_ADT import *

#7b
# ----- TIME_SPANS -----
def new_time_spans():
    " -> time_spans"
    return attach_tag('time_spans', [])


def is_time_spans(object):
    "Python-object -> Bool"
    return get_tag(object) == 'time_spans'


def is_empty_time_spans(time_spans):
    "time_spans -> Bool"
    ensure(cal_day, is_time_spans)
    return not strip_tag(time_spans)


def insert_span(time_spans, ts):
    "time_spans x span -> time_spans"
    
    def add_time_span(ts):
        "[ts] -> [ts]"
        if not ts or precedes(start_time(get_span(time_spans)),
                              start_time(get_span(ts[0]))):
            return [time_spans] + ts
        else:
            return [ts[0]] + add_time_span(ts[1:])
    
    ensure(time_spans, is_time_spans)
    ensure(ts, is_time_span)
    
    return attach_tag('time_spans', add_time_span(strip_tag(time_spans)))


def first_time_span(time_spans):
    "time_spans -> time_span"
    ensure(time_spans, is_time_spans)
    if is_empty_time_spans(time_spans):
        raise Exception('Empty time spans.')
    else:
        return strip_tag(time_spans)[0]


def rest_time_spans(time_spans):
    "calendar_day -> calendar_day"
    ensure(time_spans, is_time_spans)
    if is_empty_time_spans(time_spans):
        return time_spans
    else:
        return attach_tag('time_spans', strip_tag(time_spans)[1:])
