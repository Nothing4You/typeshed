from datetime import date, datetime, time, timedelta

Date = date
Time = time
TimeDelta = timedelta
Timestamp = datetime

def DateFromTicks(ticks: float) -> date: ...
def TimeFromTicks(ticks: float) -> time: ...
def TimestampFromTicks(ticks: float) -> datetime: ...
