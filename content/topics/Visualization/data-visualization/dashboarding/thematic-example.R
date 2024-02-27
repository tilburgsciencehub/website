library(shiny)
library(bslib)
library(ggplot2)
library(dplyr)
library(gapminder)
library(thematic)
library(ragg) # To ensure auto/custom fonts function correctly

options(shiny.useragg = TRUE) # Let's `ragg` handles the font rendering

# To modify R plot theming defaults for all plots in your Shiny app, call thematic_shiny() before launching the app.
thematic_shiny(font = "auto") 

# Define UI
ui <- fluidPage(
  theme = bslib::bs_theme(
    bg = "#ffffff", 
    fg = "#123261", 
    primary = "#f3ad42",
    base_font = bslib::font_google("Pacifico")  # Example of using a Google Font
  ),
  titlePanel("Gapminder Data Visualization Shiny App"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("yearInput", "Year", 
                  min = 1952,
                  max = 2007, 
                  value = 1952, 
                  step = 5,
                  animate = TRUE), 
      selectInput("continentInput", "Continent", 
                  choices = c("All", sort(unique(gapminder$continent))),
                  selected = "All",
                  multiple = TRUE)
    ),
    mainPanel(
      tabsetPanel(
        type = "pills",
        tabPanel("Gapminder Visualization", plotOutput("ggplotPlot")),
        tabPanel("lattice", plotOutput("latticePlot")),
        tabPanel("base", plotOutput("basePlot")),
      )
    )
  )
)

server <- function(input, output) {
    output$ggplotPlot <- renderPlot({
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
  output$lattice <- renderPlot({
    lattice::show.settings()
  })
  output$base <- renderPlot({
    image(volcano, col = thematic_get_option("sequential"))
  })
}

shinyApp(ui, server)