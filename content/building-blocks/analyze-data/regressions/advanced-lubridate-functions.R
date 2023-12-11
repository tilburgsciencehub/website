# 1. Advanced Parsing Techniques
## Custom Date Formats
parse_date_time("20th Nov 2023", orders = "dmy") # If your dates don't fit standard formats, use parse_date_time()

## Handle multiple date formats simultaneously:
dates <- c("2023-11-20", "20/11/2023", "November 20, 2023")
parse_date_time(dates, orders = c("Ymd", "dmy", "BdY"))

# 2. Advanced Arithmetic
## Combine periods and durations for precise calculations:
my_date <- ymd("2023-01-01")
my_date + years(1) + ddays(30) # Add 1 year and 30 days

# 3. Time Zone Manipulations
## Convert times to different time zones:
my_time <- ymd_hms("2023-01-01 12:00:00", tz = "UTC")
with_tz(my_time, tz = "America/New_York")

# 4. Periodic Patterns in Time Series Data
## Aggregating by Time Periods
time_series_data %>%
  group_by(floor_date(date, unit = "month")) %>%
  summarize(total = sum(value))

# 5. Advanced Date Comparison
## Comparing Periods and Intervals
check_date <- ymd("2023-06-15")
check_date %within% my_interval # Use set operations like %within% to check if a date falls within an interval:

## Sequence Generation
seq.Date(from = ymd("2023-01-01"), to = ymd("2023-12-31"), by = "month") # Generate sequences of dates for simulations or testing:

# 6. Integrating with Other R Packages
## dplyr and ggplot2 Integration
data %>%
  mutate(quarter = quarter(date)) %>%
  ggplot(aes(x = quarter, y = value)) +
  geom_line()