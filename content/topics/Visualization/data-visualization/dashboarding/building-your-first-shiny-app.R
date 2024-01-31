# Install and load the required packages
# install.packages("shiny")
# intall.packages("gapminder")
# install.packages("ggplot2")
# install.packages("dplyr")
library(shiny)
library(gapminder)
library(ggplot2)
library(dplyr)



# Define the User Interface (UI)
ui <- fluidPage(
  titlePanel("Gapminder Data Visualization Shiny App"),
  sidebarLayout(
    sidebarPanel(
      # Slider input for selecting the year
      sliderInput("yearInput", "Select Year:", 
                  min = 1952, 
                  max = 2007, 
                  value = 1952, 
                  step = 5,
                  animate = TRUE), # Adding animation for a better user experience
      
      # Dropdown menu for selecting continents
      selectInput("continentInput", "Select Continent(s):", 
                  choices = c("All", sort(unique(as.character(gapminder$continent)))),
                  selected = "All",
                  multiple = TRUE)
    ),
    mainPanel(  
      plotOutput("gapPlot")  # Render the plot
    )
  )
)

server <- function(input, output) {
  # Render plot based on user input (Reactivity)
  output$gapPlot <- renderPlot({
    # Filter the gapminder data for the selected year
    data <- gapminder %>%
      filter(year == input$yearInput)
    
    # If a specific continent is selected (other than "All"), filter data by that continent
    if (input$continentInput != "All") {
      data <- data %>% filter(continent == input$continentInput)
    }
    
    # Create a ggplot
    ggplot(data, aes(x = gdpPercap, y = lifeExp, size = pop, color = continent)) +
      geom_point(alpha = 0.7) +  # Use point geometry with some transparency
      scale_size(range = c(3, 20), name="Population") +  # Scale size for population visualization
      scale_x_log10() +  # Use a logarithmic scale for the x-axis (GDP Per Capita)
      theme_minimal() +  # Apply minimal theme for aesthetics
      labs(title = paste("Year:", input$yearInput),  # Add title with the selected year
           x = "GDP Per Capita",  # Label for x-axis
           y = "Life Expectancy")  # Label for y-axis
  })
}

shinyApp(ui = ui, server = server)
