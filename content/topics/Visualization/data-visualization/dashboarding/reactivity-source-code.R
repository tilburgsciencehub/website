# Load necessary libraries
library(shiny)
library(ggplot2)
library(dplyr)
library(bslib)
library(thematic)
library(DT)

# Enable thematic with automatic font adjustment - improves visual consistency between UI and ggplot
thematic_shiny(font = "auto") 

# Define a theme using bslib - sets the visual theme of the app
theme <- bslib::bs_theme(
  bootswatch = "yeti"  # Choice of theme 
)

# UI definition
ui <- fluidPage(
  theme = theme,  # Apply the bslib theme for a cohesive look
  titlePanel("Air Quality Analysis"),
  sidebarLayout(
    sidebarPanel(
      # Interactive element: Dropdown for month selection
      selectInput("monthInput", "Select Month:", 
                  choices = month.abb[5:9], 
                  selected = "May"),
      sliderInput("windSlider", "Select Wind Speed Threshold:", 
                  min = 0, 
                  max = 20, 
                  value = 10),
      selectInput("variableInput", "Select Variable to Plot:",
                  choices = c("Temp", "Wind", "Solar.R", "Ozone"), 
                  selected = "Temp")
    ),
    mainPanel(
      textOutput("summary"),  # Display area for textual summary
      plotOutput("airQualityPlot"),  # Display area for the ggplot visualization
      DTOutput("dataTable")  # DataTable output for airquality data
    )
  )
)

# Server logic
server <- function(input, output, session) {
  summaryData <- reactiveVal()  # Store summary in a reactive value for dynamic update
  
  # Observer for reactivity: Responds to month selection changes
  observe({
    selectedMonth <- match(input$monthInput, month.abb)
    # Data processing based on user selection
    summaryResult <- airquality %>% 
      filter(Month == selectedMonth) %>%
      summarize(AvgTemp = mean(Temp, na.rm = TRUE), 
                AvgWind = mean(Wind, na.rm = TRUE))
    
    summaryData(summaryResult)  # Update reactive value dynamically
    # Console message for debugging and insight into app's reactivity
    message("Summary for ", month.abb[selectedMonth], ": Avg Temp = ", summaryResult$AvgTemp, ", Avg Wind = ", summaryResult$AvgWind)
  })
  
  # Reactive output: Dynamically displays the calculated summary
  output$summary <- renderText({
    data <- summaryData()
    paste("Average temperature: ", round(data$AvgTemp, 2), " degrees. Average wind speed: ", round(data$AvgWind, 2), " mph")
  })
  
  # Reactive plot output: Updates the plot based on the month selected by the user
  output$airQualityPlot <- renderPlot({
    filteredData <- airquality %>% 
      filter(Month == match(input$monthInput, month.abb), 
             Wind > input$windSlider)
    
    ggplot(filteredData, aes_string(x = "Day", y = input$variableInput)) +
      geom_line() +
      ggtitle(paste("Air Quality -", input$variableInput, "Trends in", input$monthInput)) +
      theme_minimal() + 
      theme(text = element_text(size = 12)) +
      xlab("Day of Month") + 
      ylab(input$variableInput)
  })
  
  # Display the airquality data in a DataTable
  output$dataTable <- renderDT({
    airquality %>%
      filter(Month == match(input$monthInput, month.abb),
             Wind > input$windSlider)
  })
}

# Run the App
shinyApp(ui, server)