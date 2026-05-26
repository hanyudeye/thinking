import datetime as dt
from pytz import timezone, UTC

# Define the location and its offset from UTC
location = "America/Chicago"  # adjust to your desired location
offset = -5 * 60 * 60  # in seconds (adjust according to your time zone)

# Create a timezone object for the given location
tz = timezone(location)
UTC_tz = UTC()

def high_tide(date_str):
    date_obj = dt.datetime.strptime(date_str, "%Y-%m-%d")
    date_obj_utc = UTC_tz.localize(date_obj).astimezone(tz)
    
    # Calculate the high tide time based on the location
    if location == "America/Chicago":
        high_tide_offset = 2.5 * 60 * 60  # in seconds (adjust according to your high tide offset)
        return date_obj_utc + dt.timedelta(seconds=high_tide_offset)
    else:
        raise ValueError(f"High tide calculation not implemented for {location}.")

date_str = input("Enter a date (YYYY-MM-DD): ")
print(high_tide(date_str))
