---
title: "IB Math Exploration Ideas — Correlation and Regression (Housing Focus)"
author: "Chris Huson"
date: 2025-10-31
---

## IB Math Exploration Ideas — Correlation and Regression (Housing Focus)

1. **Manhattan Housing Prices vs. Floor Height**  
   **Research Goal:** Determine whether higher floors in Manhattan apartment buildings command price premiums and whether that premium follows a consistent trend.  
   **Step-by-Step Plan:**  
   1. **Data Source Search:** Identify reliable online data sets (e.g., Zillow, StreetEasy, Redfin, or NYC Open Data) that include apartment sale prices, floor numbers, and locations.  
   2. **Sample Selection:** Search for buildings where multiple comparable apartments are listed or sold on different floors. Record price, floor level, unit size, and location.  
   3. **Data Cleaning:** Remove outliers (e.g., penthouses or recently renovated units) and ensure that comparisons are within the same building or building type.  
   4. **Metric Definition:** Compute a *price premium per floor* metric—such as the percentage increase in price for each floor of elevation.  
   5. **Graph Construction:** Plot floor differential (independent variable, x-axis) versus percent price difference (dependent variable, y-axis).  
   6. **Regression Analysis:** Perform a linear regression to test correlation strength. Record slope, R², and interpret whether the relationship is statistically meaningful.  
   7. **Conclusion and Interpretation:** Evaluate whether higher floors consistently yield higher prices. Discuss causes and limitations.

2. **Latitude vs. House Values in Italy**  
   **Research Goal:** Test whether housing prices decrease with decreasing latitude (moving south) across Italy.  
   **Step-by-Step Plan:**  
   1. **Data Source Review:** Identify consistent sources for house prices or rents by locality. Candidate sources include national stats (ISTAT), portal aggregates (e.g., Idealista, Immobiliare.it), and regional reports. Prioritize data with clear definitions (€/m², median price, or median rent).  
   2. **Standardize the Asset:** Choose a comparable unit to reduce heterogeneity. Options: price per square meter for resale apartments, new-build price per square meter, or median rent for a 60–70 m² apartment. Fix one metric and one property type.  
   3. **Geographic Sampling Strategy:** Decide the spatial unit. Use cities (provincial capitals) for broad coverage. Target at least 30 cities from north to south to support regression.  
   4. **Latitude Extraction:** For each selected city, record latitude. Method: use a city-level latitude table or geocode city names once and cache coordinates.  
   5. **Data Collection Table:** Build a dataset with columns: City, Region, Latitude (°N), PriceMetric (€/m² or €/month), Population (optional control), and Year/Quarter.  
   6. **Cleaning and Filters:** Ensure the same time period across cities. Remove cities with missing or unreliable price data. Winsorize or drop top/bottom 1–2% if outliers dominate. Convert all prices to the same unit and currency.  
   7. **Exploratory Graph:** Scatter plot of Latitude (x) vs PriceMetric (y). Add a simple linear fit for visual inspection. Consider coloring by macro-region (North, Center, South/Islands) for context.  
   8. **Baseline Regression:** Run \( \text{Price} = \beta_0 + \beta_1 \cdot \text{Latitude} + \varepsilon \). Report \(\hat\beta_1\), \(R^2\), standard error, and p-value. Interpret sign and magnitude (e.g., €/m² per degree of latitude).  
   9. **Robustness Checks (optional):**  
      - Log-linear model: \(\log(\text{Price})\) on Latitude to interpret % change per degree.  
      - Add controls: Region fixed effects or a dummy for metro size to see if latitude remains significant.  
      - Check nonlinearity with a quadratic term or piecewise fit (North vs South).  
   10. **Conclusion and Interpretation:** Summarize findings on the north–south gradient. Discuss alternative drivers (income levels, tourism intensity, industry mix). State limitations and next steps.

3. **Interest Rates vs. Home Sales Volume in New York State (2000–2025)**  
   Explore how mortgage rates correlate with real estate activity using time-series regression.

4. **Income vs. Rent Burden by Borough in NYC**  
   Examine the correlation between median household income and the share of income spent on rent.

5. **Rent vs. Subway Distance in New York City**  
   Analyze how monthly rent changes with distance from the nearest subway station across boroughs.

6. **Apartment Size vs. Price per Square Meter in Rome and Milan**  
   Compare linear regressions for two Italian cities and discuss regional housing market differences.

7. **Airbnb Price vs. Walking Distance to Major Attractions in Florence or Venice**  
   Quantify price sensitivity to proximity to cultural landmarks using mapping data.

8. **Historic Trend: NYC Apartment Prices vs. Year Built**  
   Investigate whether older buildings are cheaper or more expensive after adjusting for location.

9. **Commuting Time vs. Housing Cost in the New York Metropolitan Area**  
   Test the “urban sprawl” hypothesis using regression on census or transit data.

10. **Seaside Proximity and Home Prices in Liguria or the Amalfi Coast**  
    Quantify how distance from the sea affects house price per square meter.

11. **Green Space Access vs. Apartment Cost in Milan or Brooklyn**  
    Correlate proximity to parks with rent or sale price.
