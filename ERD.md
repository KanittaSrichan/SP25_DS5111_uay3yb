# Analysis of Daily Stock Gainers

## Introduction
This report presents the findings from the analysis of daily stock gainers listed on Yahoo and Wall Street Journal’s news websites. The primary goal was to analyze a week's worth of stock market data to identify key trends and patterns that can inform investment decisions and provide insights to non-financial stakeholders. This analysis helps in understanding the behavior of stocks that have shown significant upward movements in their prices.

## Use Cases
The analysis focuses on several practical use cases:
- **Identifying Recurring Stocks**: Highlighting stocks that frequently appear, which may indicate consistency in performance or volatility.
- **Examining Price Ranges**: Understanding the distribution of price changes and their percentages to gauge market trends and stock volatility.
- **Pattern Recognition**: Investigating any discernible patterns in the appearance of gainers to predict future trends.

## Methods
The dataset consisted of daily records of stock prices, including open, midday, and closing. The data was processed using SQL queries and DBT (Data Build Tool) to create intermediate tables that facilitated deeper analysis. Weekly aggregations were performed to simplify the data for trend analysis and to create visual representations of these trends.

### Data Processing Steps Included:
1. **Creation of Daily and Weekly Tables**: Python scripts were used to collect and store daily data and aggregate it on a weekly basis.
2. **Analysis of Repeating Symbols**: SQL queries identified symbols that appeared frequently within the dataset.

## Entity Relationship Diagram (ERD)
Below is the ERD that illustrates the flow and transformation of the data:

```mermaid
erDiagram
    RAW-DATA ||--o{ CLEANED-DATA : "is cleaned and parsed"
    CLEANED-DATA ||--o{ WEEKLY-AGGREGATED : "aggregated weekly"
    WEEKLY-AGGREGATED ||--o{ ANALYSIS-TABLES : "used for detailed analysis"

    RAW-DATA {
        string Symbol
        string Name
        string Price
        float Change
        string Change_Percent
        string Volume
        string Market_Cap
        string PE_Ratio
        string Wk_Change_Percent
    }

    CLEANED-DATA {
        string Symbol
        float Current_Price
        float Price_Change
        float Price_Change_Percent
        float Volume
        float Market_Cap
        float PE_Ratio
        float Annual_Change_Percent
    }

    WEEKLY-AGGREGATED {
        date Week_End_Date
        float Avg_Price
        float Avg_Price_Change
        float Avg_Price_Change_Percent
        float Avg_Volume
    }

    ANALYSIS-TABLES {
        date Week_End_Date
        float Avg_Price
        float Avg_Price_Change
        float Max_Volume
        float High_PE_Ratio
    }
