## Install the tidyverse package, which inlcudes dplyr and ggplot2
# install.packages("tidyverse")

# Load the tidyverse package into the R session
library(tidyverse)

## Load data 
data_url <- "https://github.com/tilburgsciencehub/website/tree/master/content/building-blocks/prepare-your-data-for-analysis/data-visualization/piaac.rda"
load(url(data_url)) #piaac.Rda is loaded now

## Data manipulation
barplot_education <- data %>%
  # Remove observations with missing values for hourly earnings, gender, and education level
  drop_na(earnhr, edlevel3) %>% 
  
  # Focus on the Netherlands and exclude the top and bottom 1% of earners to remove outliers
  filter(cntryid == "Netherlands", 
         earnhr > quantile(earnhr, 0.01) &
           earnhr < quantile(earnhr, 0.99)) %>%
  
  # Create a gender dummy variable, convert variables to appropriate types, and order education levels
  mutate( 
    earnhr = as.numeric(earnhr),
    edlevel3 = factor(edlevel3, levels = c("Low", "Medium", "High"))) %>%
  
  # Calculate mean and standard deviation of hourly earnings by education level
  group_by(edlevel3) %>%
  summarise(mean = mean(earnhr), 
            sd = sd(earnhr), 
            n = length(earnhr),
            se = sd / sqrt(n),
            .groups = 'drop') # End of grouping operations

## setting up the geom_lines
p_value_one <- tibble(
  x = c("Low", "Low", "Medium", "Medium"),
  y = c(20, 22, 22, 20))

p_value_two <- tibble(
  x = c("Low", "Low", "High", "High"),
  y = c(28, 30, 30, 28))

## plot
barplot_education %>% 
  ggplot(aes(edlevel3, mean)) +  # Mapping education level to x-axis and mean wage to y-axis
  geom_col(aes(fill = edlevel3), color = "black", width = 0.85) + # Creating bars filled by education level, with a black border for definition
  geom_errorbar(aes(ymin = mean - se, ymax = mean + se), width = 0.2) + # Adding error bars to indicate standard error
  geom_text(aes(label = round(mean, 2)), vjust = -1.5) + # Displaying mean values on top of each bar
  geom_line(data = p_value_one, aes(x, y, group = 1)) + # Drawing first significance line based on p_value_one data
  geom_line(data = p_value_two, aes(x, y, group = 1)) + # Drawing second significance line based on p_value_two data
  annotate("text", x = 1.5, y = 21, label = "**", size = 7) + # Adding text annotation for first significance level
  annotate("text", x = 2., y = 29, label = "***", size = 7) + # Adding text annotation for second significance level
  scale_fill_manual(values = c("white", "grey", "black")) +  # Customizing bar colors
  scale_y_continuous(limits = c(0, 30), expand = c(0, 0)) +  # Setting y-axis limits for better presentation of data
  theme_minimal() + # Applying a minimalistic theme for a clean look
  labs(
    title = "Mean Hourly Wage by Education Level" # Adding a plot title
  ) + 
  theme(
    plot.title = element_text(
      size = 15, face = "bold", margin = margin(b = 35), hjust = 0.5 # Enhancing the plot title for better visibility and aesthetics
    ),
    plot.margin = unit(rep(1, 4), "cm"),  # Adding uniform margins around the plot
    axis.text = element_text(
      size = 12, color = "#22292F"  # Customizing axis text size and color
    ),
    axis.title = element_text(size = 12, hjust = 1),  # Adjusting axis title appearance
    axis.title.x = element_blank(), # Removing x-axis title for simplicity
    axis.title.y = element_blank(), # Removing y-axis title for simplicity
    axis.text.y = element_text(margin = margin(r = 5)), # Customizing y-axis text margin
    axis.text.x = element_blank(),  # Removing x-axis text for simplicity
    legend.position = "top",  # Positioning the legend at the top of the plot
    legend.title = element_blank(),  # Removing the legend title
    panel.grid.major.y = element_blank(), # Removing major horizontal grid lines
    panel.grid.major.x = element_blank(), # Removing major vertical grid lines
    panel.grid.minor.y = element_blank()  # Removing minor horizontal grid lines
  )
ggsave("basicplot4.png")



# Multiple categorical variable bar plot 
data <- read_csv("Desktop/Universiteit/Master/Tilburg University/Seminars/Seminar Labor Economics/Assignments/Assignment 1/piaac20-2.csv")
# Data manipulation
piaac <- data %>%
  # Remove observations with missing values for hourly earnings, gender, and education level
  drop_na(earnhr, gender_r, edlevel3) %>% 
  
  # Focus on the Netherlands and exclude the top and bottom 1% of earners to remove outliers
  filter(cntryid == "Netherlands", 
         earnhr > quantile(earnhr, 0.01) &
           earnhr < quantile(earnhr, 0.99)) %>%
  
  # Create a gender dummy variable, convert variables to appropriate types, and order education levels
  mutate(gender_r = as.factor(gender_r), 
         earnhr = as.numeric(earnhr),
         edlevel3 = factor(edlevel3, levels = c("Low", "Medium", "High"))) %>%
  
  # Calculate mean and standard deviation of hourly earnings by education level and gender
  group_by(edlevel3, gender_r) %>%
  summarise(mean = mean(earnhr), 
            sd = sd(earnhr), 
            n = length(earnhr),
            se = sd / sqrt(n),
            .groups = 'drop') %>% # End of grouping operations
  
  # Append overall mean and standard deviation for each education level 
  bind_rows( # Consolidate overall and gender-specific statistics into one dataset
    data %>%
      drop_na(earnhr, gender_r, edlevel3) %>%
      filter(cntryid == "Netherlands",
             earnhr > quantile(earnhr, 0.01) &
               earnhr < quantile(earnhr, 0.99)) %>%
      group_by(edlevel3) %>%
      summarise(mean = mean(earnhr), 
                sd = sd(earnhr),
                n = length(earnhr),
                se = sd / sqrt(n),
                gender_r = "All") %>%
      mutate(
        gender_r = factor(gender_r, levels = c("All", "Male", "Female")),
        edlevel3 = factor(edlevel3, levels = c("Low","Medium","High"))
      ))  # Refactor the education levels

annotations <- tibble(
  x = c(1.5, 2),
  y = c(21, 29),
  label = c("**", "***"),
  gender_r = c("Male", "Male") # assuming these are for the "male" facet
)

# option 1 manual significance stars)
p_value_one <- tibble(
  x = c("Low", "Low", "Medium", "Medium"),
  y = c(20, 22, 22, 20),
  gender_r = c("Male", "Male", "Male", "Male"))

p_value_two <- tibble(
  x = c("Low", "Low", "High", "High"),
  y = c(28, 30, 30, 28),
  gender_r = c("Male", "Male", "Male", "Male"))


piaac %>% 
  ggplot(aes(edlevel3, mean)) +  # Mapping education level to x-axis and mean wage to y-axis
  geom_col(aes(fill = edlevel3), color = "black", width = 0.85) + # Creating bars filled by education level, with a black border for definition
  geom_errorbar(aes(ymin = mean - se, ymax = mean + se), width = 0.2) + # Adding error bars to indicate standard error
  geom_text(aes(label = round(mean, 2)), vjust = -1.5) + # Displaying mean values on top of each bar
  geom_line(data = p_value_one, aes(x = x, y = y, group = 1)) +
  geom_line(data = p_value_two, aes(x = x, y = y, group = 1)) +
  geom_text(data = annotations, aes(x = x, y = y, label = label, group = gender_r), size = 7) +
  facet_wrap(~ gender_r, strip.position = "bottom" , nrow = 1) +  # Display facet labels beneath each section
  scale_fill_manual(values = c("white", "grey", "black")) +  # Customizing bar colors
  scale_y_continuous(limits = c(0, 30), expand = c(0, 0)) +  # Setting y-axis limits for better presentation of data
  theme_minimal() + # Applying a minimalistic theme for a clean look
  labs(
    title = "Mean Hourly Wage by Education Level and Gender" # Adding a plot title
  ) + 
  theme(
    plot.title = element_text(
      size = 15, face = "bold", margin = margin(b = 35), hjust = 0.5 # Enhancing the plot title for better visibility and aesthetics
    ),
    plot.margin = unit(rep(1, 4), "cm"),  # Adding uniform margins around the plot
    axis.text = element_text(
      size = 12, color = "#22292F"  # Customizing axis text size and color
    ),
    axis.title = element_text(size = 12, hjust = 1),  # Adjusting axis title appearance
    axis.title.x = element_blank(), # Removing x-axis title for simplicity
    axis.title.y = element_blank(), # Removing y-axis title for simplicity
    axis.text.y = element_text(margin = margin(r = 5)), # Customizing y-axis text margin
    axis.text.x = element_blank(),  # Removing x-axis text for simplicity
    legend.position = "top",  # Positioning the legend at the top of the plot
    legend.title = element_blank(),  # Removing the legend title
    panel.grid.major.y = element_blank(), # Removing major horizontal grid lines
    panel.grid.major.x = element_blank(), # Removing major vertical grid lines
    panel.grid.minor.y = element_blank()  # Removing minor horizontal grid lines
  )
ggsave("basicplot6.png")
