library(WDI)
library(ggplot2)
library(dplyr)
library(colourpicker)
library(viridis)  # Ensure this package is installed for additional color palettes
library(extrafont)

# Define the indicators
co2_emissions_id <- "EN.ATM.CO2E.PC"  # CO2 Emissions (metric tons per capita)
health_expenditure_id <- "SH.XPD.CHEX.PC.CD"  # Health Expenditure per capita (current US$)

# Fetch the data for all countries from 2000 to 2020
data <- WDI(country = "all", indicator = c(co2_emissions_id, health_expenditure_id), 
            start = 2000, end = 2020, extra = TRUE)
data$region <- as.factor(data$region)
data$year <- as.numeric(data$year)

# UI setup
ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      textInput("title", "Title", "Health Expenditure vs CO2 Emissions"),
      textInput("xaxis", "X Axis Label", "Log of CO2 Emissions (metric tons per capita)"),
      textInput("yaxis", "Y Axis Label", "Log of Health Expenditure per capita (current US$)"),
      selectInput("theme", "Select Theme", choices = c("Minimal" = "theme_minimal", "Classic" = "theme_classic", "Light" = "theme_light", "Dark" = "theme_dark")),
      textInput("legendTitle", "Legend Title", "Region"),
      numericInput("size", "Point size", value = 1, min = 1),
      checkboxInput("fit", "Add smooth curve", FALSE),
      colourInput("smoothColor", "Smooth Curve Color", "blue"),  # Color picker for smooth curve
      selectInput("palette", "Color Palette", choices = c("Viridis", "Inferno", "Topo", "Cividis")),
      selectInput("regions", "Regions", choices = levels(unique(data$region)), multiple = TRUE),
      sliderInput("years", "Years", min = min(data$year), max = max(data$year), value = c(2005)),
      # New inputs for font size customization
      numericInput("titleSize", "Title Size", value = 15, min = 8),
      numericInput("axisTitleSize", "Axis Title Size", value = 15, min = 8),
      numericInput("axisTextSize", "Axis Text Size", value = 15, min = 8),
      downloadButton("downloadPlot", "Download Plot")  # Download button for the plot
    ),
    mainPanel(
      plotOutput("plot", width = "1000px", height = "1000px")  
    )
  )
)

# Server logic
server <- function(input, output) {
  output$plot <- renderPlot({
    data_plot <- subset(data, region %in% input$regions & year == input$years)
    color_palette <- switch(input$palette,
                            "Viridis" = viridis::viridis_pal(),
                            "Inferno" = viridis::viridis_pal(option = "B"),
                            "Topo" = viridis::viridis_pal(option = "C"),
                            "Cividis" = viridis::viridis_pal(option = "D"))
    
    plot <- ggplot(data_plot, aes(x = log(EN.ATM.CO2E.PC), y = log(SH.XPD.CHEX.PC.CD), color = region)) +
      geom_point(size = input$size) +
      scale_color_manual(values = color_palette(length(unique(data_plot$region)))) +
      labs(title = input$title, x = input$xaxis, y = input$yaxis, color = input$legendTitle) +
      do.call(get(input$theme), list()) 
    
    if (input$fit) {
      plot <- plot + geom_smooth(method = "lm", color = input$smoothColor)  
    }
    
    plot <- plot + theme(text = element_text(family = input$plotFont, size = input$axisTextSize),
                         title = element_text(size = input$titleSize),
                         axis.title = element_text(size = input$axisTitleSize))
    
    output$downloadPlot <- downloadHandler(
      filename = function() { paste("plot-", Sys.Date(), ".png", sep = "") },
      content = function(file) { ggsave(file, plot = plot, device = "png") }
    )
    
    plot
  })
}

# Run the Shiny application
shinyApp(ui = ui, server = server)



