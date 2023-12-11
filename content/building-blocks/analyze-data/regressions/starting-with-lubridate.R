# Install packages if needed
## install.packages(lubridate"))
library(lubridate)

# 1. Parsing Dates and Times
## lubridate provides functions to parse dates and times from character strings:
ymd("2023-11-20") # Year-month-day format
mdy("11/20/2023") # Month-day-year format
dmy("20-11-2023") # Day-month-year format

# 2. Handling Time Zones
## Specify time zones with the tz argument:
ymd("2023-11-20", tz = "UTC")

# 3. Manipulating Dates and Times
## Perform arithmetic operations like addition and subtraction:
my_date <- ymd("2023-01-01")
my_date + days(30) # Add 30 days
my_date - months(2) # Subtract 2 months

## Extract specific components from a date-time object:
year(my_date)
month(my_date)
day(my_date)
wday(my_date, label = TRUE) # Day of the week

#  4. Interval, Period, and Duration
## Working with Intervals
interval_start <- ymd_hms("2023-01-01 00:00:00")
interval_end <- ymd_hms("2023-12-31 23:59:59")
my_interval <- interval(interval_start, interval_end) # Time span between two specific points.

## Period vs. Duration
my_period <- as.period(my_interval) # Human-readable time spans (years, months, etc.)
my_duration <- as.duration(my_interval) #  Exact time spans in seconds

# 5. Comparison and Operations
## Use logical operators to compare dates:
date1 <- ymd("2023-01-01")
date2 <- ymd("2023-06-01")
date1 < date2 # TRUE