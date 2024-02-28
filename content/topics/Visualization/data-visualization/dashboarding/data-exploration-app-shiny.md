---
title: "How to: Build a Data Exploration App in Shiny"
description: "Learn how to create an interactive data exploration app using Shiny for effective Exploratory Data Analysis (EDA)."
keywords: "Shiny, Exploratory Data Analysis, Data Exploration, Interactive Data App"
date: 2023-12-28
weight: 5
author: "Matthijs ten Tije"
authorlink: "https://tilburgsciencehub.com/contributors/matthijstentije/"
aliases:
  - /data-exploration-shiny-app
---

## Overview
This article is aimed at assisting you in the development of a `Shiny` application focused on `Exploratory Data Analysis` (EDA). The Shiny framework enhances data management capabilities, facilitating the creation of web applications. These applications can provide dynamic environments for interactive data exploration.

In `EDA`, the ability to interact with data is crucial. `Shiny` applications allows users to filter, sort, and visualize data in various ways, fostering a deeper and more intuitive understanding of the underlying trends and patterns.

As you progress through this article, you'll acquire the skills to use `Shiny` for various `EDA` tasks. This includes uploading and processing data, creating visual representations, and building interactive features that enhance data exploration. By the end, you'll be equipped with the skills to develop `Shiny` applications that enable comprehensive and insightful data analyses.

## Data Management in Shiny

### Handling Multiple Data Formats
Efficient management of diverse data formats is important in `EDA`. This section will take you through setting up a `Shiny` app capable of processing file uploads and API data, thereby building your data analysis toolkit.

#### User Interface
It's important to design your `Shiny` app's user interface (UI) to accommodate different data inputs. This part focuses on configuring the UI for CSV file uploads and API data retrieval.

{{% codeblock %}}
```R
ui <- fluidPage(
  titlePanel("Data Exploration App"),
  sidebarLayout(
    sidebarPanel(
      fileInput("fileCSV", "Upload CSV File"), # For CSV file uploads
      actionButton("loadData", "Load Data from World Bank API") # Button to trigger API data loading
    ),
    mainPanel(
      tableOutput("dataDisplay") # Area to display the data
    )
  )
)
```
{{% /codeblock %}}

#### Server 
The server function is where the CSV file uploads and fetched data from an API are retrieved, such as the World Bank API. 
This example illustrates basic yet useful data processing techniques in `Shiny`.

{{% codeblock %}}
```R
server <- function(input, output) {
  # Reactive value to store data
  dataStorage <- reactiveVal()

  # Observe CSV File Uploads
  observeEvent(input$fileCSV, {
    # Check if a file is uploaded
    req(input$fileCSV) 
    # Read and store CSV data
    csvData <- read.csv(input$fileCSV$datapath, stringsAsFactors = FALSE)
    dataStorage(csvData)
  })

  # Observe API Data Loading
  observeEvent(input$loadData, {
    # Fetch and store data from an API (example API call)
    apiData <- WDI::WDI(country = "all", indicator = "NY.GDP.MKTP.CD", start = 2019, end = 2019)
    dataStorage(apiData)
  })

  # Render the data in the UI
  output$dataDisplay <- renderTable({
    dataStorage() # Access the stored data
  })
}

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/eda-1.png" width="800">
</p>

{{% example %}}
**Dynamic Data Response and Management**

Your `Shiny` app incorporates the following elements: 

- *User Action Dependent*: The data in the app changes based on which file is uploaded or if the API data is fetched. The `observeEvent()` functions in the server listen for these specific user actions.
- *Overwriting dataStorage*: When a new file is uploaded or new data is fetched from the API, the existing data in `dataStorage()` is replaced with this new data. This overwriting mechanism ensures the app is always displaying the most recent data provided by the user.
- *Reactive Data Display:* As `dataStorage()` is a reactive value, any change in its data triggers a refresh in the UI where this data is displayed. Thus, users immediately see the updated data in the table output on the app.

{{% /example %}}

### Incorporating Additional File Types 
To extend the capabilities of the `Shiny` application to handle other file types, such as Excel or JSON, you can incorporate additional logic into the server function. Here are some tips for doing so:

- **Identify File Types**: Determine the additional file types you want your app to support. Common types include Excel (.xlsx), JSON (.json), and text files (.txt).
- **Install Necessary Packages**: Ensure you have the required R packages installed. For example, `readxl` for Excel files, `jsonlite` for JSON, and `readr` for more flexible text file reading.
- **Update UI**: Add UI elements for each new file type. For instance, separate `fileInput` widgets for each file type can make it easier for users to upload the correct format.
- **Modify Server Logic**: In the server function, add separate `observeEvent()` functions for each file type. 
  
{{% codeblock %}} 
```R
# Specify in UI
fileInput("fileExcel", "Upload Excel File"),
fileInput("fileJSON", "Upload JSON File")

# Specify in Server
observeEvent(input$fileExcel, {
  req(input$fileExcel)
  excelData <- readxl::read_excel(input$fileExcel$datapath)
  dataStorage(excelData)
})

observeEvent(input$fileJSON, {
  req(input$fileJSON)
  jsonData <- jsonlite::fromJSON(file = input$fileJSON$datapath)
  dataStorage(jsonData)
})
```
{{% /codeblock %}} 

{{% tip %}}
**Use Your Own Data**

While we use the `iris` dataset for demonstration in the rest of this article, you now have the skills to adapt this code to work with your own data sources and formats.
{{% /tip %}}

## Interactive Tables in Shiny with DT
This section will guide you in transforming static tables, like in the previous example, into dynamic elements within your `Shiny` app. Interactive tables allow users to sort, filter, and paginate data, which are useful features for managing extensive datasets and complex information. To turn static tables into interactive tables we will use the `DT` package, a powerful tool within `Shiny`.

### User Interface
The first step in adding interactivity is to modify the `UI` to accommodate interactive tables. 
This involves replacing the traditional `tableOutput` with `DT::dataTableOutput` in the `UI` definition:

{{% codeblock %}}
```R
# UI Setup for interactive tables
ui <- fluidPage(
  titlePanel("Data Exploration App"),
  sidebarLayout(
    sidebarPanel(
      # Your existing input controls
    ),
    mainPanel(
      DT::dataTableOutput("dataDisplay") # Updated to use DT's dataTableOutput
    )
  )
)
```
{{% /codeblock %}}

### Server
On the server side, we adapt our logic to render the data as an interactive `DataTable`. This integration enhances the data presentation, making it more adaptable to user interactions and providing a richer experience in data exploration.

{{% codeblock %}}
```R
# Server Logic for interactive tables
server <- function(input, output) {
  # Existing data processing logic
  
  # Rendering the data as an interactive DataTable
  output$dataDisplay <- DT::renderDataTable({
    datatable(dataset(), 
              options = list(
                pageLength = 5,      # Set rows per page
                autoWidth = TRUE,    # Auto-adjust column widths
                searching = TRUE,    # Enable data filtering
                ordering = TRUE,     # Enable column sorting
                colReorder = TRUE))   # Allow column reorderingpagelength = 5,                        
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/eda-2.png" width="800">
</p>

These modifications transform your `Shiny` app's tables into interactive platforms. Users can now engage more deeply with the data by sorting, filtering, and paging, improving data exploration efficiency and intuitiveness. 

## Summary Statistics Display
Summary statistics are the backbone in `EDA`, offering a snapshot of  data characteristics like the distribution or correlation. Integrating these statistics into a `Shiny` application using `DT` enriches the data explanatory power, providing clear and concise data insights. Here's how to embed these summary statistics into a shiny app.

### User Interface
The user interface (UI) can be designed to facilitate an intuitive and interactive experience with summary statistics. Here are some examples to consider:
- Utilize a tabbed panel to segregate different data views. 
  - For example, dedicate one tab for the entire dataset and others for various summary statistics, ensuring an organized and user-friendly layout.
- Include dropdown menus or selectors for users to easily choose variables or categories for summary statistics.
- Focus on a clean UI design with clear labels, facilitating understable navigation and understanding.


{{% codeblock %}}
```R
# Generalized UI
ui <- fluidPage(
  titlePanel("`Shiny` App"),
  mainPanel(
    tabsetPanel(type = "tabs",
      # Tab 1: Data Table 
      tabPanel("Data Table", DTOutput("Table")), 
      # Tab 2: Summary
      tabPanel("Summary", 
               selectInput("summary_var", "Select Variable:", choices = names(iris)), 
               DTOutput("Table2") 
      ),
      # Tab 3: Summary per Species
      tabPanel("Summary per Species", 
               selectInput("species_var", "Select Species Variable:", choices = unique(iris$Species)), 
               selectInput("summary_var2", "Select Variable:", choices = names(iris)), 
               DTOutput("Table3") 
      )
    )
  )
)
```
{{% /codeblock %}}

### Server
Develop a server function that dynamically generates and displays summary statistics:
- *Reactive Data Processing*: Use `Shiny`'s reactive programming to create real-time, user-driven summary statistics.
- *Conditional Rendering*: Adapt the server logic to user inputs, like variable selection, to update the summary statistics correspondingly.
- *Interactive Tables with `DT`*: Implement the `DT` package to present summary statistics in a dynamic and engaging way.

{{% codeblock %}}
```R
# Generalized server logic
server <- function(input, output) {
  # Render the entire Iris dataset as an interactive data table (Tab 1)
  output$Table <- renderDT({
    datatable(iris, options = list(pageLength = 10))
  })
  
  # Render summary statistics for the selected variable in Tab 2
  output$Table2 <- renderDT({
    selected_var <- input$summary_var
    summary_data <- summary(iris[[selected_var]])
    summary_df <- data.frame(Statistic = names(summary_data), Value = as.numeric(summary_data))
    datatable(summary_df, options = list(pageLength = 5))
  })
  
  # Render summary statistics for the selected variable within the chosen species in Tab 3
  output$Table3 <- renderDT({
    species_summary <- iris %>%
      filter(Species == input$species_var) %>%
      select(input$summary_var2)
    species_summary_df <- data.frame(summary(species_summary))
    datatable(species_summary_df, options = list(pageLength = 5))
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/eda-3.png" width="800">
</p>

With this structure, you can easily provide users with interactive summary statistics, enhancing their ability to explore and understand your data.

## Data Visualization
Data visualization is the last aspect of `Exploratory Data Analysis `(`EDA`), offering visionary insights. With our `Shiny` app now capable of handling data and user interactions, we'll focus on visualizing this data, utilizing both `ggplot2` for static plots and `Plotly` for interactive graphics.

### Static Visualizations
The process begins with establishing static visualizations, revealing basic data trends and correlations. 

{{% codeblock %}}
```R
# Tab 4: Data Visualizations
tabPanel("Visualizations",
  h2("Explore Data Through Visualizations"),
  p("Visualizations provide an effective way to uncover patterns, trends, and relationships in your data."),
  plotOutput("visualization")
)

# Define the server logic
server <- function(input, output) {
  # ... Existing server logic ...

  # Render data visualizations in Tab 4
  output$visualization <- renderPlot({
    # Include your code for data visualizations here
    # Example: Create a scatter plot of Sepal.Length vs. Sepal.Width
    plot(iris$Sepal.Length, iris$Sepal.Width, 
         main = "Scatter Plot of Sepal.Length vs. Sepal.Width",
         xlab = "Sepal.Length", ylab = "Sepal.Width", 
         col = iris$Species, pch = 19)
  })
}
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/eda-4.png" width="800">
</p>

{{% tip %}}

Inside the `renderPlot` function, you can include your code for creating data visualizations. In the provided example, we've created a scatter plot of `Sepal.Length` vs. `Sepal.Width` from the `Iris` dataset. You can replace this example with your preferred visualization code, whether it's bar charts, histograms, or any other type of plot that suits your data exploration goals.

{{% /tip %}}

### Interactive Visualizations using Plotly
Enhance `EDA` with interactive visualizations using `Plotly`. This enables users to engage with the plot actively, discovering insights that static visuals might not reveal. The Interactive features of `Plotly` allows for zoomable and clickable plots. Users can hover over data points for more details, zoom in on areas of interest, and even select specific data segments for closer examination. Thereby allowing users to explore data in real-time, uncovering insights that static analysis might miss. 

This section demonstrates how to effectively integrate these interactive elements using `Plotly` into your `EDA` process using `Shiny`:

```R
  # Server for Interactive Plotly Visualizations
server <- function(input, output) {
  # Assigning the output plot to 'plot' in the `Shiny` UI
  output$plot <- renderPlotly({
    # Converting a ggplot object into an interactive Plotly plot
    ggPlotly(
      # Creating a ggplot object
      ggplot(your_dataset, aes(x = variable1, y = variable2, color = factorVar)) +
        # Adding a geom_point layer for a scatter plot
        geom_point() +
        # Applying a minimalistic theme
        theme_minimal()
      )
  })
}
```

<p align = "center">
<img src = "../images/eda-5.png" width="800">
</p>

By integrating both static and interactive visualizations, your `Shiny` app becomes a powerful tool for `EDA`. Users can start with an overall view of data trends and then delve deeper into specifics with interactive plots, making the data exploration process both comprehensive and engaging.

{{% tip %}}
**Further Learning with Plotly**

Explore more advanced functionalities of `Plotly` for sophisticated data visualization. Check out our in-depth [article](/Plotly) on `Plotly` to expand your knowledge and skills.

{{% /tip %}}


{{% summary %}}

This article, "`Exploratory Data Analysis` (`EDA`)", is part of the R `Shiny` series, focusing on crafting interactive data exploration applications using `Shiny`. 

Key learning goals of this article include:

- Setting Up a UI in `Shiny`: You've learned to set up a UI in `Shiny` for managing various data sources.
  - This includes handling CSV file uploads and retrieving data from external APIs like the World Bank API.
- Creating Interactive Tables with `DT`:
  - This section taught you how to enable features such as sorting, filtering, and pagination, significantly improving data interaction.
- Integrating Summary Statistics with `DT`:
  - You've learned how to construct a UI and server logic in `Shiny` to dynamically display summary statistics.
- Visual Data Exploration: The article provided practical examples of data visualization, starting with basic scatter plots using `ggplot2` and advancing to interactive plots with `Plotly`.

You are now equipped with the necessary skills to build comprehensive `Shiny` applications that enable effective data exploration, accommodating diverse data sources, interactive tables, summary statistics, and insightful visualizations.
The next article of the R shiny series discusses how to use Shiny for [Data Storytelling](/plotly).

{{% /summary %}}