---
title: "How to: Create the 'perfect' plot with R Shiny"
description: "Explore real-time plot customization using Shiny's reactivity and interactive widgets. Analyze the relationship between health expenditure and CO2 emissions with World Bank data."
keywords: "R Shiny, Data Visualization, Widgets, ggplot2"
date: 2023-12-20
weight: 7
author: "Matthijs ten Tije"
authorlink: 
aliases:
  - /widgets
  - /r-shiny 
  - /visualizations
---

## Overview
In this article, we explore a hands-on application of R Shiny's `reactivity` feature through a practical example: constructing live your “perfect” plot. While the concept of `reactivity` in R Shiny has been discussed in this [article](/shiny/reactivity), here we bring it to life by demonstrating how it enables the real-time creation and refinement of data visualizations. 

We'll delve into the global relationship between health expenditure (per capita, in current US dollars) and CO2 emissions (metric tons per capita) using a dataset from the World Bank. Through this analysis, we aim to explore potential correlations between a nation's healthcare spending and its environmental footprint. 

We'll walk you through a step-by-step process of building your 'perfect plot', using Shiny's responsive `widgets` like sliders, dropdowns, and color pickers.

### Load the dataset
{{% codeblock %}}
```R
# Install the WDI package for World Bank data
install.packages("WDI")
library(WDI)

# Specify the indicators: CO2 Emissions and Health Expenditure per capita
indicators <- c("EN.ATM.CO2E.PC" = "CO2 Emissions (metric tons per capita)", 
                "SH.XPD.CHEX.PC.CD" = "Health Expenditure per capita (current US$)")

# Fetch data from the World Bank for the years 2000-2020
data <- WDI(country = "all", indicator = indicators, start = 2000, end = 2020, extra = TRUE)
data$region <- as.factor(data$region)
data$year <- as.numeric(data$year)
```
{{% /codeblock %}}

## Adding Inputs to Modify a Plot

### Add a plot title: Text Input
The` textInput` widget is used to create an interactive text input field in the Shiny user interface.    
Its basic syntax is `textInput(inputId, label, value)`, where: `inputId` is a unique identifier for the widget. `label` provides a descriptive label for the input field. `value` sets an initial default text within the field, which is useful for initializing your app with pre-defined settings. 

{{% codeblock %}}

```R
# Load ggplot2 for plotting functionalities
library(ggplot2)

# UI setup: Includes a sidebar panel with a text input for entering the plot title
ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      textInput("title", "Title", "Health Expenditure vs CO2 Emissions")
    ),
    mainPanel(
      plotOutput("plot")
    )
  )
)

# Server logic: Reflects the entered title on the plot dynamically
server <- function(input, output) {
  output$plot <- renderPlot({
    ggplot(data, aes(x = log(EN.ATM.CO2E.PC), y = log(SH.XPD.CHEX.PC.CD))) +
    geom_point() +
    ggtitle(input$title)  # Updates the plot title based on user input
  })
}

# Run the Shiny application
shinyApp(ui = ui, server = server)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-1.png" width="600">
</p>

### Change the Point Size: numeric input
The `numericInput` widget in Shiny facilitates the creation of input fields specifically for numeric values. Its syntax extends beyond that of the `textInput` widget, including additional arguments like min and max. 
The syntax is `numericInput(inputId, label, value, min, max, step)`, where:
- `min` and `max` define the minimum and maximum values that can be entered.
- `step` determines the increment between each value in the input (optional).

{{% tip %}}
**Shiny's Intelligent Input Handling**

Shiny's is designed to recognize the type of user input and manage it accordingly in the server-side code. This ensures that the data type of the input is maintained throughout the application. For instance, if a numeric input with the ID size is used, accessing `input$size` in the server code will automatically return a numeric value. This feature of Shiny significantly simplifies data handling and ensures type consistency.

{{% /tip %}}

{{% codeblock %}}
```R
# Inside your existing UI setup
sidebarPanel(
  # Other input elements
  numericInput("size", "Point size", value = 1, min = 1, max = 10, step = 1)  # Numeric input for adjusting point size
  # Any other elements
)

# Inside your existing server function
server <- function(input, output) {
  output$plot <- renderPlot({
    # Existing plotting code
    geom_point(size = input$size)  # Adjust point size dynamically based on input
    # Any additional plot customization
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-2.png" width="600">
</p>

### Fit a smooth curve: checkbox input
The `checkboxInput` widget, which is distinct in its binary nature, is limited to only two possible values: TRUE or FALSE. This widget is ideal for scenarios requiring a simple yes/no or on/off decision from the user. 

The `checkboxInput` function in Shiny is used to create this widget, and it includes a `value` parameter that determines its initial state. This parameter accepts only two values: TRUE or FALSE. Setting it to TRUE means the checkbox will be checked by default when the application loads, and conversely, setting it to FALSE will leave it unchecked initially.

The basic syntax of the `checkboxInput` function is `checkboxInput(inputId, label, value)`.

{{% codeblock %}}
```R
# Inside your existing UI setup
sidebarPanel(
  # Other input elements
  checkboxInput("fit", "Add smooth curve", FALSE)  # Checkbox for adding a smooth curve
)

# Inside your existing server function
server <- function(input, output) {
  output$plot <- renderPlot({
    # Previous plot code
    if (input$fit) {
      plot <- plot + geom_smooth(method = "lm")  # Adds smooth curve if checked
    }
    plot
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-3.png" width="600">
</p>

## More input types

### Add colours to your plot: radio buttons
`Radio buttons` are used when you want to present multiple options to the user but require them to select only one. This input type is particularly useful for situations where the choice is exclusive and cannot be multiple.

The `radioButtons` function includes a `choices` parameter to define the options available for selection and a `selected` argument to specify which option is selected by default. Unlike other input types, there is no value parameter; the `selected` argument serves a similar purpose, setting the initial state of the selection.

The basic syntax for `radioButtons` is `radioButtons(inputId, label, choices, selected)`, where:
- `choices` is a list of options that the user can select from.
- `selected` determines which choice is pre-selected when the app loads.

{{% codeblock %}}
```R
# Inside your existing UI setup
sidebarPanel(
  # Other input elements
  radioButtons("color", "Point color", choices = c("blue", "red", "green", "black"))  # Radio buttons for color selection
)

# Inside your existing server function
server <- function(input, output) {
  output$plot <- renderPlot({
    # Previous plot code
    plot <- plot + geom_smooth(method = "lm", color = input$color)  # Color changes as per selection
    plot
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-4.png" width="600">
</p>

### Using Select Inputs for Extensive Choice Lists
`Select inputs`, also known as dropdown lists, are an ideal choice in Shiny when you need to present a user with a long list of options without consuming much screen space. Unlike radio buttons which are best for limited choices due to their space requirements, select inputs neatly encapsulate numerous options within a scrollable dropdown menu.

The `selectInput` widget features the `choices` parameter to list the available options and the `selected` parameter to set the default selected option(s). A significant feature of select inputs is the `multiple` argument. When set to TRUE, it allows users to select more than one value from the list, offering flexibility for user interaction.

The basic syntax for `selectInput` is `selectInput(inputId, label, choices, selected, multiple)`.

{{% codeblock %}}
```R
# Inside your existing UI setup
sidebarPanel(
  # Other input elements
  selectInput("regions", "Regions", choices = levels(unique(data$region)), multiple = TRUE)  # Dropdown for region selection
)

# Inside your existing server function
server <- function(input, output) {
  output$plot <- renderPlot({
    # Filter data based on selected regions
    data_plot <- subset(data, region %in% input$regions)
    # Previous plot code
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-5.png" width="600">
</p>

### Using Slider Inputs for Numerical Value Selection in Shiny
`Slider inputs` are widgets that allow users to select numeric values through a sliding mechanism. They serve a similar purpose to numeric inputs but offer a more interactive and visual approach to value selection. Sliders can be  effective for adjusting parameters within a specific range, such as setting thresholds, defining ranges, or filtering data.

#### Single vs. Range Value Selection with Slider Inputs
The configuration of the slider input can vary depending on the initial value provided:
- **Single Value Selection**: If the initial value (specified in the `value` argument) is a single number, the slider is set up for selecting a single numeric value.
- **Range Value Selection**: If the initial value is a vector of two numbers, the slider allows the selection of a range of values, represented by the two end points of the vector

{{% codeblock %}}
```R
# Inside your existing UI setup
sidebarPanel(
  # Other input elements
  sliderInput("years", "Years", min = min(data$year), max = max(data$year), value = c(2005))  # Slider for year selection
)

# Inside your existing server function
server <- function(input, output) {
  output$plot <- renderPlot({
    # Filter data based on selected year range
    data_plot <- subset(data, year == input$years)
    # Previous plot code
  })
}

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-6.png" width="600">
</p>

{{% tip %}}
**Remembering Input Arguments** 

Each input type in Shiny comes with its own set of arguments, and it can be challenging to remember all of them. To understand the available arguments for a specific input type, it's advisable to refer to the Shiny documentation or the help files associated with the input functions. 
{{% /tip %}}

## Advanced features to improve your plot

### Incorporating Color Inputs Using the Colourpicker Package
While color inputs are not a part of the basic Shiny package, they can be integrated into Shiny applications using the `colourpicker` package. The `colourInput()` function from this package allows users to select colors interactively, adding a visually engaging element to the app. 

The `colourInput()` function is straightforward to use, with its essential arguments being `inputId`, `label`, and `value`:
- `inputId` is a unique identifier for the color input widget.
- `label` provides a descriptive title for the color picker.
- `value` sets the initial color, which can be specified in various formats, including English color names like "red" or "yellow".

{{% codeblock %}}
```R
install.packages("Colourpicker")
library(Colourpicker)

# Inside your existing UI setup
sidebarPanel(
  # Other input elements
  colourInput("smoothColor", "Smooth Curve Color", "blue")  # Color picker for smooth curve
)

# Inside your existing server function
server <- function(input, output) {
  output$plot <- renderPlot({
    # Previous plot code
    if (input$fit) {
      plot <- plot + geom_smooth(method = "lm", color = input$smoothColor)  # Use picked color for smooth curve
    }
    plot
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-7.png" width="600">
</p>

### Tailoring Plot Appearance with Output Placeholder Functions
In Shiny, just like input functions, `output placeholder functions` also come with various arguments that allow you to modify the appearance or behavior of the outputs. This flexibility is particularly useful when you want to customize how data visualizations or other UI elements are displayed in your app.

The `plotOutput()` function, used for displaying plots in a Shiny application, includes parameters to adjust the dimensions of the plot. By default, the `height` of the plot is set to 400 pixels. However, you can easily change this using the `height` and `width` parameters within `plotOutput()`.

{{% codeblock %}}
```R
# Inside your existing UI setup
mainPanel(
  plotOutput("plot", width = "1000px", height = "1000px")  # Adjusting plot size
)
# Server logic remains the same as previous
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-8.png" width="600">
</p> 

### Leveraging Plotly for Interactive Data Visualization
`Plotly`, a widely used package, is especially valued in Shiny applications for its capacity to transform static plots into interactive visualizations. `Plotly` stands out, because of its `ggplotly()` function. This function effortlessly converts a `ggplot2` plot, static visualizations in R, into an interactive format.


To incorporate `Plotly`'s interactive capabilities into a Shiny app, you will need to make some adjustments to both the UI and server components of your application:
- The `plotlyOutput` function in the UI defines a space for the interactive plot with specified dimensions.
- The `renderPlotly` function in the server script takes a `ggplot` object and converts it into an interactive plot using `ggplotly()`.

{{% codeblock %}}
```R
# Inside your existing UI setup
mainPanel(
  plotlyOutput("plot", width = "1000px", height = "1000px")  # Interactive Plotly plot
)

# Inside your existing server function
server <- function(input, output) {
  output$plot <- renderPlotly({
    # Convert ggplot to interactive Plotly plot
    ggplotly(plot)
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-9.png" width="600">
</p>

{{% tip %}}
**Benefits of Interactive Plots**

Interactive plots significantly enhance the user experience by allowing for dynamic engagement with the visualized data. Features like zooming, panning, tooltips, and selective viewing of plot elements make it easier for users to explore and understand complex datasets. For more information check out this [article](/plotly)

{{% /tip %}}

### Adding a Download Plot Function in Shiny 
At last, now that we have a range of options to create live the "perfect" plot. It is important to use Shiny's ability for users to download the plots they interact with. In addition, this can be particularly useful for data analysis and reporting purposes. You can achieve this by implementing a `download handler`, which allows users to save the plot as an image or other file formats directly from the app.

To add a download function for plots in your Shiny application, you'll need to update both the UI and server components. This involves adding a `download button` in the UI and defining the server logic to handle the plot download process.

{{% codeblock %}}
```R
# Inside your existing UI setup
sidebarPanel(
  # Other input elements
  downloadButton("downloadPlot", "Download Plot")  # Button for downloading the plot
)

# Inside your existing server function
server <- function(input, output) {
  # Previous plot logic
  output$downloadPlot <- downloadHandler(
    filename = function() {paste("plot-", Sys.Date(), ".png", sep = "")},
    content = function(file) {ggsave(file, plot = plot, device = "png")}
  )
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-10.png" width="600">
</p>


{{% example %}}
**Advanced Example**

For this example, we've integrated several widgets to elevate the user interaction and visualization customization. 

We introduced a color theme selector, greatly enhancing the visual distinction of regions within the scatter plot. This feature allows users to choose from a variety of color palettes, making the data more interpretable and visually appealing.

Additionally, we incorporated a theme selector, offering options like 'Minimal', 'Classic', 'Light', and 'Dark'. This selector empowers users to change the overall aesthetic of the plot, catering to diverse preferences and enhancing readability under different viewing conditions.

To further tailor the visualization, we added new textInput fields for X and Y-axis labels. These inputs enable users to provide custom, descriptive labels for the axes, thereby making the plots more informative and contextually relevant.

{{% /example %}}

{{% codeblock %}}

```R 
# Download the example file in the right corner
```
[R-link](perfect-plot-source-code.R)

{{% /codeblock %}}

<p align = "center">
<img src = "../images/perfect-plot-11.png" width="750">
</p>

{{% summary %}}

In this article, we've discussed a specific application of R Shiny's `reactivity`: enabling users to construct and customize their own plots live within the app. Here's what we've achieved:

- **Live Plot Customization**: We illustrated how users can dynamically build and modify plots using Shiny's reactive framework. This was demonstrated using a `World Bank` dataset, where users can explore the relationship between health expenditure and CO2 emissions.
- **Enhanced User Interaction**: Key to our implementation is the range of `widgets` we introduced. `Sliders` for adjusting numerical values, `dropdowns` for selecting data categories, and `color pickers` for aesthetic choices give users full control over the plot's appearance.
- **Personalization Tools**: We added `text inputs` for plot titles and axis labels, allowing users to personalize their visualizations further. Additionally, the inclusion of a `theme selector` provides options for changing the overall look and feel of the plots.
- **Practical Output Features**: The app includes a download function, enabling users to save their customized plots for use in presentations or reports.
  
{{% /summary %}}