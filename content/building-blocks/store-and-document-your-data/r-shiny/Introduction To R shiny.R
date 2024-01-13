# Load necessary libraries
library(shiny)
library(bslib)

# Define UI
ui <- fluidPage(
  theme = custom_theme, # Apply the custom theme
  titlePanel("Custom Themed Shiny App"),
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("slider", "Choose a number:", 
                  min = 1, max = 100, value = 50),
      actionButton("btn", "Click Me", class = "btn-primary")
    ),
    mainPanel(
      textOutput("output"),
      uiOutput("progressUI")
    )
  )
)

# Define server logic
server <- function(input, output) {
    output$gapPlot <- renderPlot({
        data <- gapminder %>%
            filter(year == input$yearInput)
        
        if (input$continentInput != "All") {
            data <- data %>% filter(continent == input$continentInput)
        }
        
        ggplot(data, aes(x = gdpPercap, y = lifeExp, size = pop, color = continent)) +
            geom_point(alpha = 0.7) +
            scale_size(range = c(3, 20), name="Population") +
            scale_x_log10() +
            theme_minimal() +
            labs(title = paste("Year:", input$yearInput),
                 x = "GDP Per Capita",
                 y = "Life Expectancy")
    })
}
server <- function(input, output) {
  output$output <- renderText({
    paste("You selected:", input$slider)
  })
  
  # Create a simple progress bar UI
  output$progressUI <- renderUI({
    input$btn # Trigger for reactivity
    myValue <- input$slider
    # Simple progress bar
    div(style = sprintf("width: %d%%; height: 20px; background-color: %s;", myValue, "#f3ad42"))
  })
}

# Run the app
shinyApp(ui, server)
