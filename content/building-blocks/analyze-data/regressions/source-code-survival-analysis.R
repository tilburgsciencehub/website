## Install.packages(c("dplyr","lubridate","survival","survminer","gtsummary"))
# Load the necessary libraries
library(dplyr)
library(lubridate)
library(survival)
library(survminer)
library(gtsummary)

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


# Example Censoring Data
# Creating a subsample,
Example_censoring <- customer_churn_data %>%
  filter(id == 1:10) %>%
  select(id, start_date, churn_date, event_occurred) %>%
  mutate(diff = difftime(time2 = start_date, time1 = churn_date, units = "days"),
         churned = as.factor(event_occurred)
  )

# Just for illustration purposes
Example_censoring$diff[is.na(Example_censoring$diff)] <- 365

ggplot(Example_censoring, aes(x = id, y = diff)) +
  geom_segment(aes(x = id, xend = id, y = 0, yend = diff), color = "black", na.rm = F) +
  geom_point(aes(color = churned), size = 4, na.rm = F) +
  scale_color_manual(values = c("red", "blue")) +  # Adjust color for better contrast
  theme_light() +
  ylim(0, 365) +
  coord_flip() +
  theme(
    panel.grid.major.y = element_blank(),
    panel.border = element_blank(),
    axis.text.x = element_text(angle = 45, hjust = 1),  # Improve text readability
    plot.title = element_text(hjust = 0.5)  # Center align the title
  ) +
  xlab("Customer ID") +
  ylab("Days Until Event/Churn") +  # More descriptive label
  labs(title = "Censoring in Customer Churn Data", subtitle = "Black lines indicate duration until churn or censoring")  # Add subtitle for context
