library(WDI)
library(dplyr)
library(ggplot2)

# Fetch World Bank Development Indicators for all countries
# with specific indicators (GDP, primary and secondary school enrollment, fertility rate)
# for years starting from 2000.
db <- WDI(country = "all",
          indicator = c("ny.gdp.mktp.kd", "SE.PRM.ENRR.FE", "SE.SEC.ENRR.FE", "SP.DYN.TFRT.IN"),
          extra = TRUE,
          start = 2000,
          language = "en")

# Group data by country code (iso3c) and fill in missing values
# both upwards and downwards within each group.
db <- db %>% 
  group_by(iso3c) %>% 
  fill(names(.), .direction = "downup")

# Filter out aggregate regions and select data for the year 2000.
db_filtered <- db %>% 
  filter(region != "Aggregates") %>%
  filter(year == 2000)

# Convert the 'region' column to a factor for better categorization in plots.
db_filtered$region <- as.factor(db_filtered$region)

# Create a ggplot of the data, plotting log of GDP per capita against female enrollment in primary school, colouring by income group
p <- db_filtered %>%
  ggplot(aes(x = log(ny.gdp.mktp.kd), y = SE.PRM.ENRR.FE, color = income, label = iso3c)) + 
  geom_point(alpha = 0.6, size = 2) +
  geom_smooth(method = lm, se = FALSE, col = 'maroon', size = 0.6) +
  scale_color_viridis_d() +
  labs(
    title = "% Female Enrollment in Primary School and GDP per Capita (2000)",
    caption = "Source: World Bank WDI",
    x = "Log GDP per capita (constant 2015 US$)",
    y = "School enrollment, primary, female (%)"
  ) + 
  theme_minimal() +
  theme(
    legend.position = "top",
    legend.title = element_blank(),
    panel.grid.major = element_blank(), 
    panel.grid.minor = element_blank(),
    axis.title = element_text(face = "bold", color = "grey24"),
    plot.margin = margin(1, 1, 1, 1, "cm")
  )

# Save the plot as a PNG file
ggsave("2000.png", plot = p,  dpi = 300)
