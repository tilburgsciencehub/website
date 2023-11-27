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
The `lubridate` package in R simplifies date operations, making it a valuable tool for your survival analysis.  
`Survival analysis` is a statistical method that analyzes the influence of time on events. Originating from the medical sciences, it is also useful in scenarios like predicting customer churn probabilities. 

Our Survival analysis starts with the `Survival Function`, which estimates the probability of survival over time. Using methods like the `Kaplan-Meier estimator`, we plot survival probabilities to visualize and understand survival trends. Thereafter, the regression model, `Cox Proportional Hazards model`, will be discussed to examine how various covariates affect survival times, allowing for a detailed analysis of significant factors and their impacts.

### When to use Survival Analysis
`Survival analysis`, also known as `event-time` analysis, is a valuable tool when dealing with particular types of data and analytical needs.

**Applications of `Survival Analysis`**
- *Comparing Survival Rates*: Compare survival times across different groups (e.g., treatment vs. control groups in clinical trials). Survival analysis offers methods like the Kaplan-Meier estimator to make this comparison.
- *Modeling Survival Data*: Implementing regression models, such as the Cox Proportional Hazards model, to examine how various factors (e.g., age, treatment type) influence survival time.
- *Predicting Future Events*: In fields like finance, healthcare, and marketing, predicting when a future event (like default, disease recurrence, or customer churn) will occur is essential for planning and strategy. Survival analysis provides tools for such predictions.

**Data Characteristics in `Survival Analysis`**

`Time-to-Event Data`: This is the primary data type for survival analysis, focusing on recording the duration until an event of interest occurs. Furthermore, the time until an event is always positive and typically exhibits a non-normal distribution, often characterized by data skewness. This means that the distribution of events over time is skewed, with a higher concentration of observations early on and progressively declining as time advances.

`Censored data`: A fundamental element in survival analysis, occurring when not all participants have experienced the event by the study's end. Censoring can take several forms:
- *Right Censoring*: Most common, it occurs when the event of interest hasn't happened by the end of the observation period, leaving the exact timing of the event unknown.
- *Left Censoring*: This happens when the starting point of the event is unknown, but its event is confirmed.
- *Interval Censoring*: This arises when participants are not observed continuously and their event status is only known at specific checkpoints. 

{{% example %}}

To explain `censoring` in survival analysis, consider this example from a dataset used later in this building block.  
Here, subjects 1, 3, and 5 experience the event within the first year, while subjects 2, 4, 6, 7, 8, 9, and 10 do not. These latter subjects are 'censored' after one year, meaning we only know they didn't encounter the event in the first year, but their status thereafter is unknown.  
 This scenario exemplifies right censoring, where the occurrence of the event beyond a certain point is uncertain.

<p align = "center">
<img src = "../images/example_censoring.png" width="400">
</p>

{{% /example %}}

## Data Preparation 
To conduct a survival analysis, it's thus essential to have two key components: a variable indicating the time elapsed since a particular starting event and a dummy indicator of whether the survival event has occurred. The former is achieved by measuring the interval between two dates, and for the latter, a dummy variable is created to represent survival status.

For measuring the time interval, the R package `lubridate` is particularly useful. It simplifies the process of working with dates, allowing for easy calculation of time differences between events. With lubridate, you can efficiently handle various date formats and perform operations to determine the duration between two points in time, which is critical for your time-to-event variable in survival analysis.

Once you have calculated the time intervals using lubridate, you pair this data with your survival indicator. This is a dummy variable that shows whether the event of interest (like death, failure, recovery) has occurred. 

This combination of time-to-event data and survival status forms the foundation for conducting survival analysis.

### Walkthrough through the Lubridate Package
This section will guide you through the basic functionalities of lubridate, helping you manage and manipulate date-time data more efficiently.

#### Starting with lubridate
In this section, we introduce the basics of the lubridate package in R, focusing on installing the package, parsing dates and times, handling time zones, manipulating dates, and performing various operations.

{{% codeblock %}}

```R 
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
```
{{% /codeblock %}}

#### Advanced lubridate functions
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
## dplyr and ggplot2 Integration
data %>%
  mutate(quarter = quarter(date)) %>%
  ggplot(aes(x = quarter, y = value)) +
  geom_line()
```

{{% /codeblock %}}

{{% tip %}}

**More on Lubridate**
For more detailed information and advanced functionalities, you can refer to the lubridate documentation:
?lubridate.  
Or visit the Comprehensive R Archive Network (CRAN) at [CRAN lubridate](https://cran.r-project.org/package=lubridate).

{{% /tip %}}

#### Calculating Survival Times Using Lubridate
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
<img src = "../images/lubridate-example.png" width="400">
</p>

Now you have the durations calculated and ready for survival analysis, with dates properly formatted and intervals measured in the unit of choice!

## Survival Analysis in R
With our date data now prepared and structured, we can begin examining the factors that influence whether a certain event occurs or not in survival analysis. This investigation starts with the concept of the Survival Function, a fundamental aspect of survival analysis.

### The Survival Function  

The Survival Function, typically denoted as 

{{<katex>}}
S(t)= P(T>t) =1−F(t)
 {{</katex>}}
 <br> 

Represents the probability of surviving or avoiding the event of interest until a specific time t. This function is key to understanding how different variables affect the likelihood of the event occurring over time.

### The Kaplan-Meier Estimator

In practical terms, to get an understanding of the survival function or survival probability, the `Kaplan-Meier estimator` is commonly used to estimate S(t). Furthermore, the Kaplan-Meier curve gives a visual representation of the survival probability over time, offering insights into the overall survival probability.  

For our analysis, imagine you are managing a subscription-based service, and you're interested in understanding customer churn over time. You start to log data on when customers unsubscribe. However, not all customers will have unsubscribed by the time of your analysis, leading to right-censored data.

1. Preparing the Data 

For our survival analysis, we need a dataset that includes the time of the event and dummy indicators for whether the event has occurred or the data is censored. 

{{% codeblock  %}}
```R
# Convert to Date objects
data$start_date <- ymd(data$start_date)
data$event_date <- ymd(data$event_date)

# Calculate time to event or censoring
data$time_to_event <- interval(start = data$start_date, end = data$event_date) / ddays(1)

# Create the censoring indicator (1 if event occurred, 0 if censored)
data$censoring_indicator <- ifelse(is.na(data$event_date), 0, 1)

# View the updated dataset
print(data)
```

{{% /codeblock  %}}

2. Creating the Survival Object 

The `Surv()` function from the `survival` package creates a survival object, which incorporates both the time and event data:
The `Surv()` function, part of the survival package in R, is used for creating a survival object. This survival object contains the two essential components of survival data: the time-to-event data and the event indicator.
The input of the `Surv()` function, are these two pieces of information. The function then combines them into a single object which can be used in subsequent survival analysis procedures. This object ensures that the survival analysis methods correctly account for both the timing of the event and the event occurrence or censoring.

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

To calculate the `Kaplan-Meier estimator`, we use the `survfit()` function. The `survfit()` function is then used to estimate the survival function. The basic syntax is survfit(Surv(time, event) ~ 1, data = your_data). Here, ~ 1 indicates that you're calculating the overall survival curve without dividing the data into groups. If you want to compare survival curves across groups, you replace 1 with a grouping variable.

The output of `survfit()` includes estimated survival probabilities at different time points, the number of subjects at risk, and the number of events.

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

# Display the plot
km_plot
```

{{% /codeblock  %}}

{{% example  %}}

This `Kaplan-Meier curve` illustrates customer retention across three promotional strategies over time. The y-axis quantifies the likelihood of customers staying, while the timeline is plotted along the x-axis. Each promotional group—Buy One Get One, Discount, and No Promotion—shows similar retention patterns, as the curves proceed with only slight differences. The lack of significant drop-offs suggests that the promotions have a marginal impact on churn rates. With the p-value of 0.23, indicating no statistical significance in the differences observed among the groups. This insight suggests promotions, in this case, do not drastically influence customer loyalty.

<p align = "center">
<img src = "../images/Kaplan-Meier-curve.png" width="600">
</p>

{{% /example  %}}

### The Cox Proportional Hazard Model

From here, we can delve deeper into analyzing how various covariates influence survival times. This is where regression models like the `Cox Proportional Hazards model` come into play. The Cox model allows you to assess the effect of several variables simultaneously on survival, adjusting for the impact of others. It's a powerful tool for identifying significant factors and quantifying their influence on the probability and timing of the event occurring.

The model's formula is expressed as: 

{{<katex>}}
h(t|X_{i}) = h_{0}(t)exp(β_{1}X_{i,1}+...+β_{p}X{i,p})
 {{</katex>}}
 <br> 

The formula combines a starting risk level with the influence of specific factors and their strengths to calculate the chance of an event happening at any particular time. 

#### The Cox Proportional Hazard Model in R

To apply the Cox model in R, the `coxph()` function from the `survival` package is used. This function requires again a `Surv()` object, and a formula specifying the model's covariates.  
Results can be summarized using the `tbl_regression()` function from the `gtsummary` package, with parameters set to show the hazard ratio (HR) instead of the logarithm of the hazard ratio.  

The HR compares the hazard rates between groups, with a value greater than 1 indicating an increased event rate and a value less than 1 indicating a reduction. Note that the HR states the rate of occurrence, not the probability of occurrence.

{{% tip %}}

**Enhanced Presentation**

For a more effective presentation of the results, consider using the `ggforest()` function to generate a forest plot. This plot graphically displays the HRs for all variables in the model, along with their confidence intervals, providing a visual and comprehensive summary of the findings.

{{% /tip %}}

The codeblock underneath contains a template for estimating the Cox Proportional Hazard Model in R: 

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

# Print the forest plot
print(forest_plot)
```

{{% /codeblock %}}

{{% example %}}

<p align = "center">
<img src = "../images/table-cox.png" width="300">
<img src = "../images/forest-plot-cox.png" width="350">
</p>


The forest plot visualizes the Hazard Ratios (HRs) for different categories of promotion and campaign types. The reference category for promotion_applied is "Buy One Get One," and for campaign_type, it's "Email."
- The "Discount" promotion has a HR of 1.61, suggesting a 61% increase in the hazard compared to the "Buy One Get One," but this is not statistically significant (p-value 0.175).
- The "No Promotion" category has a HR close to 1 (0.91), indicating no substantial change in hazard compared to the reference.
- For campaign_type, "PPC" (Pay-Per-Click) and "Social Media" have HRs below 1 (0.80 and 0.70, respectively), suggesting a lower hazard of the event occurring compared to "Email," but again, these are not significant. 

{{% /example %}}

{{% summary %}}

This building block contains an extensive overview of `survival analysis` and its application in various fields, emphasizing the role of the `lubridate` package in R for effective date management. 

Key takeaways include:
- **Importance of Date Management**: Demonstrating how `lubridate` simplifies handling dates and times in R, crucial for survival analysis.
- **Survival Analysis Explained**: Introducing survival analysis, its significance in assessing the timing of events, and its applicability from product lifecycles to customer churn prediction.
- **Practical Application**: Providing practical examples, including visualizations like the `Kaplan-Meier` curve and the `Cox proportional hazards model`, to illustrate survival probabilities and the effectiveness of various strategies in scenarios like customer retention.

{{% /summary %}}

Here is the source code for the analysis: 

{{% codeblock %}}

```R
```R
## Install.packages(c("dplyr","lubridate","survival","survminer"))
# Load the necessary libraries
library(dplyr)
library(lubridate)
library(survival)
library(survminer)

# Set a seed for reproducibility
set.seed(123)

# Create a mock data frame for customer churn analysis
customer_churn_data <- data.frame(
  id = 1:100,
  campaign_type = sample(c('Email', 'Social Media', 'PPC'), 100, replace = TRUE),
  promotion_applied = sample(c('Discount', 'Buy One Get One', 'No Promotion'), 100, replace = TRUE),
  start_date = as.Date('2022-01-01') + days(sample(1:365, 100, replace = TRUE)), # Subscription start dates throughout the year
  churn_date = as.Date(NA), # Initialize churn dates as NA
  event_occurred = sample(1:0, 100, replace = TRUE) # Dummy indicator: Whether the customer has churned (1) or not (0)
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