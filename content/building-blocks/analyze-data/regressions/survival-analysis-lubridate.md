---
title: "Survival Analysis in R"
description: "Exploration of Survival Analysis in R, focusing on the lubridate package"
keywords: "Survival Analysis, Time-to-event, Censoring, Kaplan-Meier estimator, Cox proportional hazards model, Lubridate"
weight: 20
author: "Matthijs ten Tije"
authorlink: "https://tilburgsciencehub.com/contributors/matthijstentije/"
aliases:
  - /survival/analysis
  - /time/to/event
  - /censoring
  - /kaplan/meier/estimator
  - /cox/proportional/hazard/model
  - /lubridate
---

## Overview
 
In today's data-centric world, efficiently managing dates and data points is essential for activities such as logging, documentation, and analysis. 
The `lubridate` package in R meets this demand by simplifying date operations, playing a pivotal role in `survival analysis`. 
This technique is crucial in understanding the influence of time on events, useful in scenarios from evaluating product lifecycles to predicting customer churn. 
`Survival analysis` excels in dealing with censored data, modelling non-standard duration times, and adjusting to changing event rates. 
These capabilities make it vital for analyzing time-to-event data, offering unique insights and versatility that are hard to match with other statistical methods.

### Key Features of Survival Analysis
`Survival analysis`, also known as `event-time` analysis, is a statistical method for analyzing the time until an event occurs, like equipment failure or patient mortality. 
It's particularly adept at handling censored data where some subjects haven't experienced the event by the end of the study, leaving their event times unknown
It uses survival functions to predict the likelihood of an event happening after a certain period.

Key Features: 
1.  **Censoring**: 

*Partial Information Handling*: Not all subjects experience the event by the study's end, resulting in partially known data, known as censored data.  

2. **Positive duration times**: 

*Non-Normal Distribution*: The time until an event is always positive and typically does not follow a normal distribution. 
 
*Data Skewness*: The distribution of events over time is often skewed, with many occurrences early on and fewer as time progresses.  

3. **Variable Event Rates**: 

*Non-Linear Trends* The frequency of the event can change over time, often decreasing after an initial period. 

### Types of Censoring

The unique feature of `survival analysis` is the ability to deal with "censoring." Censoring can occur in various ways: 
- *Right Censoring*: The most common form, right censoring occurs when a study ends before the event has occurred, leaving the final event time unknown.
- *Left Censoring*: This happens when the event's initiation is unknown, but its conclusion is observed. 
Common in disease recurrence studies where the recurrence is detected during a check-up but its actual onset time is unclear.
- *Interval Censoring*: This arises when participants are not observed continuously and their event status is only known at specific checkpoints. 
Individuals who miss follow-up visits but later reappear in the study.

{{% example %}}

<p align = "center">
<img src = "../images/example_censoring.png" width="600">
</p>

To illustrate the concept of "Right censoring" in survival analysis, a visualization based on the dataset used later on in this building block is provided. In this scenario:
- Subjects 1, 3, and 5 encountered the event within the first year.
- Subjects 2, 4, 6, 7, 8, 9, and 10 did not experience the event by the end of the first year.

Note that subjects 2, 4, 6, 7, 8, 9, and 10  were censored after one year. This means that while we know they didn't experience the event during the first year, their status beyond that point remains unknown. 
This exemplifies right censoring, where the event's occurrence post-observation is uncertain.

{{% /example %}}

## Data Preparation 

### Walkthrough through the Lubridate Package
The `lubridate` package in R is a powerful and user-friendly tool designed to simplify working with dates and times. Dates and times can be tricky to handle in data analysis. 
The `lubridate` package makes it easier to perform common tasks like parsing dates, performing arithmetic, and comparing date-time objects. Streamlining common tasks, and allows you to focus more on your analysis rather than on the intricacies of date-time manipulation. This section will guide you through the basic functionalities of lubridate, helping you manage and manipulate date-time data more efficiently.

### Starting with lubridate

In this section, we introduce the basics of the lubridate package in R, focusing on installing the package, parsing dates and times, handling time zones, manipulating dates, and performing various operations.
{{% codeblock %}}

```R
# Installing and Loading the lubridate package
install.packages("lubridate")
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
```
{{% /codeblock %}}

### Advanced lubridate functions
Here, we explore more advanced features of lubridate, including custom parsing techniques, advanced arithmetic, time zone manipulations, and integration with other R packages for enhanced data analysis.
{{% codeblock %}}

```R
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
## plyr and ggplot2 Integration
data %>%
  mutate(quarter = quarter(date)) %>%
  ggplot(aes(x = quarter, y = value)) +
  geom_line()
```
{{% /codeblock %}}

{{% tip %}}

**More on Lubridate**
For more detailed information and advanced functionalities, you can refer to the lubridate documentation:
?lubridate

Or visit the Comprehensive R Archive Network (CRAN) at [CRAN lubridate](https://cran.r-project.org/package=lubridate).

{{% /tip %}}

### Calculating Survival Times Using Lubridate
Data for survival analysis typically comes with the start and end dates for each observation, rather than pre-calculated durations. Ensuring these dates are formatted correctly in R for any analysis is essential. Here's how to set up a simple dataset with start_date and followup_date columns:

{{% codeblock %}}

```R
# Example dataset with start and follow-up dates
date_ex <- data.frame(
  start_date = as.Date(c("2022-06-22", "2022-02-13", "2022-10-27")), 
  followup_date = as.Date(c("2023-04-15", "2023-07-04", "2023-10-31"))
)
```
{{% /codeblock  %}}

Initially, R treats these data inputs as character strings. To properly handle them, we convert them into R date objects. 
The `lubridate` package provides convenient functions for this, such as `ymd()`, which interprets strings in the "year-month-day" format as dates.

{{% codeblock  %}}

```R
library(tibble)
library(dplyr)
library(lubridate)

# Your original data
date_ex <- tibble(
  start_date = c("2022-06-22", "2022-02-13", "2022-10-27"), 
  followup_date = c("2023-04-15", "2023-07-04", "2023-10-31")
)

# Convert character columns to date columns
date_ex$start_date <- ymd(date_ex$start_date)
date_ex$followup_date <- ymd(date_ex$followup_date)
```

{{% /codeblock  %}}

Once you have ensured that the dates are correctly formatted, you can confirm this by printing out your output. Now, you can move forward to compute the time interval between the start and follow-up dates. In the lubridate package, the \%--\% operator is used to create an interval object, and you can convert it into a duration measured in seconds using the as.duration() function. To obtain the difference in days, you can divide the duration by `ddays()`.

{{% codeblock  %}}
```R
# Create an event-time variable 
date_ex <- date_ex %>% 
  mutate(
    eventtime = as.duration(start_date %--% followup_date) / ddays()
    )

# Display the updated data frame
print(date_ex)
```
{{% /codeblock  %}}

<p align = "center">
<img src = "../images/lubridate-example.png" width="600">
</p>

Now you have the durations calculated and ready for survival analysis, with dates properly formatted and intervals measured in the unit of choice!

## Survival Analysis in R

### The Survival Function  

The survival function, S(t), is pivotal in survival analysis, signifying the likelihood that a particular event, like equipment malfunction, patient recovery, or customer attrition, hasn't happened by a specific time, t. Mathematically, this is captured as:

S(t)=P(T>t)=1−F(t)

Here, T stands for the time until the event, P(T > t) is the probability that the event occurs after a time t, and F(t) is the cumulative distribution function of the survival times.

The `Kaplan-Meier estimator` is commonly used to approximate S(t). This non-parametric technique is particularly effective for analyzing censored data, where not all subjects have experienced the event by the end of the observation period. 


### Implementing Kaplan-Meier in R

Imagine you are managing a subscription-based service, and you're interested in understanding customer churn over time. You start to log data on when customers unsubscribe. However, not all customers will have unsubscribed by the time of your analysis, leading to right-censored data.

1. Preparing the Data 

For our survival analysis, we need a dataset that includes the time of the event and whether the event has occurred or the data is censored. 

Imagine you are managing a subscription-based service, and you're interested in understanding customer churn over time. You start to log data on when customers unsubscribe. However, not all customers will have unsubscribed by the time of your analysis.

{{% codeblock  %}}
```R
# Load necessary libraries
library(dplyr)
library(lubridate)

# Set a seed for reproducibility
set.seed(123)

# Create a mock data frame for customer churn analysis
customer_churn_data <- data.frame(
  id = 1:100,
  campaign_type = sample(c('Email', 'Social Media', 'PPC'), 100, replace = TRUE),
  promotion_applied = sample(c('Discount', 'Buy One Get One', 'No Promotion'), 100, replace = TRUE),
  start_date = as.Date('2022-01-01') + days(sample(1:365, 100, replace = TRUE)), # Subscription start dates throughout the year
  churn_date = as.Date(NA), # Initialize churn dates as NA
  event_occurred = sample(1:0, 100, replace = TRUE) # Whether the customer has churned (1) or not (0)
)

# Assumption: Track a customer for 1 year
# Assign churn dates for customers who have churned
customer_churn_data$churn_date[customer_churn_data$event_occurred == 1] <- 
  customer_churn_data$start_date[customer_churn_data$event_occurred == 1] + 
  days(sample(1:365, sum(customer_churn_data$event_occurred == 1), replace = TRUE)) 


# Creating a survival_time variable
customer_churn_data <- customer_churn_data %>%
  mutate(survival_time = as.numeric(churn_date - start_date),
         # Replace NA with maximum observation period (365 days) for censored data
         survival_time = ifelse(is.na(survival_time), 365, survival_time))

# Correct data types
customer_churn_data <- customer_churn_data %>%
  mutate_at(vars(id, campaign_type, promotion_applied), factor) %>%
  mutate(id = as.numeric(id))
```

{{% /codeblock  %}}

2. Creating the Survival Object 

The `Surv()` function from the `survival` package creates a survival object, which incorporates both the time and event data:

{{% codeblock  %}}

```R
# Load the survival package
library(survival)

# Create the survival object
surv_obj <- with("YOUR DATASET", 
                Surv(time = "EVENTTIME VARIABLE", # Eventtime Variable 
                     event = "CHURNING / CENSORED VARIABLE")) # Churning / Censored Variable
```
{{% /codeblock  %}}

3. Calculating the Kaplan-Meier Estimate 

To calculate the `Kaplan-Meier estimator`, we use the `survfit()` function:

{{% codeblock  %}}

```R
# Compute the Kaplan-Meier estimate
km_fit <- survfit(surv_obj ~ "COVARIATE 1" + "COVARIATE 2" + ... , data = "DATASET")
 # km_fit <- survfit(surv_obj ~ 1) implies a model without covariates.

```

{{% /codeblock  %}}

4. Visualizing the Kaplan-Meier Estimate:

The `ggsurvplot()` function in R, part of the `survminer` package, is a key tool for producing enhanced visualizations of Kaplan-Meier survival estimates in survival analysis. Drawing on the aesthetic capabilities of `ggplot2`, it not only depicts survival probabilities over time but also integrates a risk table that displays the number of subjects at risk at different time intervals. 

This feature is crucial for gaining insights into the dynamics of the study. The function's ability to intuitively represent 'time-to-event' data makes it valuable for understanding how survival probabilities evolve and change throughout a study.

{{% codeblock  %}}
```R
# Load the survminer package
library(survminer)

# Plot the Kaplan-Meier curve
km_plot <- ggsurvplot(
  km_fit, # Kaplan-Meier estimate
  conf.int = FALSE, # Omit Confidence Interval
  risk.table = TRUE, # Provide a Risk Tabe 
  surv.median.line = "hv", # Add a median horziontal line 
)
```
{{% /codeblock  %}}

{{% example  %}}

The `Kaplan-Meier curve`, derived from our primary dataset, effectively illustrates the survival probabilities over time across different customer segments: those who received a promotion, those who did not, and those who were offered a 'buy one get one free' deal. This graphical representation is particularly useful for analyzing and comparing customer churn rates associated with various promotional strategies. By visually displaying these differences, it becomes easier to identify which promotional tactics are more effective in retaining customers, thereby providing valuable insights for strategic decision-making in marketing and customer relationship management.

<p align = "center">
<img src = "../images/Kaplan-Meier-curve.png" width="800">
</p>

{{% /example  %}}

{{% codeblock %}}
```R
# Load the necessary libraries
library(survival)
library(survminer)

# Create the survival object using the customer churn data
# 'survival_time' represents the time until the event or censoring
# 'event_occurred' is a binary indicator (1 if event occurred, 0 if censored)
surv_obj <- with(customer_churn_data, Surv(survival_time, event_occurred))

# Fit the Kaplan-Meier model, considering the effect of promotion
# 'promotion_applied' is a factor variable indicating the type of promotion
km_fit <- survfit(surv_obj ~ promotion_applied, data = customer_churn_data)

# Display summary statistics of the fit
summary(km_fit)

# Plot the Kaplan-Meier curve using ggsurvplot
# - 'conf.int = FALSE' omits confidence intervals for a cleaner plot
# - 'risk.table = TRUE' adds a risk table showing the number at risk over time
# - 'surv.median.line = "hv"' adds a horizontal-vertical line at the median
km_plot <- ggsurvplot(
  km_fit,
  conf.int = FALSE,
  risk.table = TRUE,
  surv.median.line = "hv",
  pval = TRUE, # Add a p-value to the plot
  palette = "Dark2", # Use a different color palette for better visuals
  title = "Kaplan-Meier Survival Curve for Customer Churn", # Add a title
  xlab = "Days", # Label for the x-axis
  ylab = "Survival Probability" # Label for the y-axis
)

# Display the plot
km_plot
```

{{% /codeblock %}}

### The Cox Proportional Hazard Model

The `Cox proportional hazards model`, is an essential tool in survival analysis, often used to assess the impact of various factors on the timing of a particular event. This semi-parametric model excels in both univariate and multivariate contexts.  

The model's formula is expressed as: 

{{<katex>}}
h(t|X_{i}) = h_{0}(t)exp(β_{1}X_{i,1}+...+β_{p}X{i,p})
 {{</katex>}}
 <br> 
  
The formula integrates a baseline hazard function, $h_{0}(t)$, with the exponentiation of a linear combination of covariates ($X_{i}$) and their coefficients (β), to estimate the hazard or the rate at which the event is expected to occur, at any given time point.

### The Cox Proportional Hazard Model in R

To apply the Cox model in R, the coxph() function from the survival package is used. This function requires a Surv() object, which encapsulates event time and status, and a formula specifying the model's covariates.
Results can be summarized using the `tbl_regression()` function from the `gtsummary` package, with parameters set to show the hazard ratio (HR) instead of the logarithm of the hazard ratio.  

The HR compares the hazard rates between groups, with a value greater than 1 indicating an increased event rate and a value less than 1 indicating a reduction. Notably, HR represents a rate of occurrence, not a probability of occurrence.

{{% tip %}}

**Enhanced Presentation**

For a more effective presentation of the results, consider using the ggforest() function to generate a forest plot. This plot graphically displays the HRs for all variables in the model, along with their confidence intervals, providing a visual and comprehensive summary of the findings.

{{% /tip %}}

The codeblock underneath entails a template for estimating the Cox Proportional Hazard Model in R: 

{{% codeblock %}}

```R
# Load necessary packages
library(survival)
library(gtsummary)
library(ggplot2)

# Fit a Cox proportional hazards model
fit.coxph <- coxph(Surv(time = "Eventtime_Variable", 
                        event = "Churning_Censored_Variable") ~ "Covariate_1" + "Covariate_2", 
                        data = "Your_dataset")

# Create a summary table with Hazard Ratios
tbl <- tbl_regression(fit.coxph, exp = TRUE)

# Visualize the results with a forest plot
ggforest("fit.coxph", data = "Your_dataset")
```

{{% /codeblock %}}

{{% example %}}

The Cox proportional hazards model, applied to our primary dataset, provides a detailed analysis of the impact of various promotional strategies on customer churn rates. By examining customer segments such as those who received promotions, those who did not, and those offered a 'buy one get one free' deal. This method assesses the relative hazard ratios associated with each group. The model's ability to include multiple covariates, like promotion and campaign type, allows for a more nuanced understanding of how different factors contribute to customer retention. Furthermore, the results, visualized through a forest plot, offer clear insights into the effectiveness of each promotional tactic. 

{{% /example %}}

{{% codeblock %}}
```R
# Fit the Cox model
fit.coxph <- coxph(Surv(survival_time, event_occurred) ~ promotion_applied + campaign_type, 
                   data = customer_churn_data)

# Create a summary table with exponentiated coefficients (Hazard Ratios)
tbl_cox <- tbl_regression(fit.coxph, exponentiate = TRUE)

# Print the summary table
print(tbl_cox)

# Visualize the Cox model results with a forest plot
forest_plot <- ggforest(fit.coxph, data = customer_churn_data)

# Print the forest plot
print(forest_plot)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/table-cox.png" width="400">
</p>

<p align = "center">
<img src = "../images/forest-plot-cox.png" width="400">
</p>

{{% summary %}}

This building block provides a comprehensive overview of `survival analysis` and its application in various fields, emphasizing the role of the `lubridate` package in R for effective date management. 

Key takeaways include:
- **Importance of Date Management**: Demonstrating how l`ubridate` simplifies handling dates and times in R, crucial for survival analysis.
- **Survival Analysis Explained**: Introducing survival analysis, its significance in assessing the timing of events, and its applicability from product lifecycles to customer churn prediction.
- **Practical Application**: Providing practical examples, including visualizations like the `Kaplan-Meier` curve and the `Cox proportional hazards model`, to illustrate survival probabilities and the effectiveness of various strategies in scenarios like customer retention.

{{% /summary %}}


