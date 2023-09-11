# SGV Home Prices
***
## General Info
This project involves the analysis of the prices of homes located in several cities in the San Grabriel Valley.
First, home data is scraped from zillow.com and saved to disk as a csv file.
Then, the relationships between various home features are explored and visualized.
Finally, a regression model is built and optimzed in order to predict the values of homes not included in the data set.

## 1. Retrieve Data from Zillow
The first three files are Python scripts intended to be run on the local machine. The first script retrieves the desired
JSON pages from zillow.com and saves them to disk as a Pickle. The second script loads the saved json pages, extracts the desired
features for each house, and saves them to disk as a CSV file. Since the JSON pages do not include the years the homes were built,
a third script is needed to retrieve this information. The third script extracts the year built from the url of each home and saves
the list of years to disk as a new CSV file.  
  
After running these first three scipts in order*, there should be one new Pickle file and two new CSV files saved to disk.  

*Note, the Zillow urls, user agents, and proxy network names were removed from the scripts. In order to run them properly, one needs to
fill them in with new ones.

## 2. Clean the Data
The fourth file is a Jupyter Notebook that merges the two CSV files, cleans the data, and saves it to a new CSV file that can be used
for effectively analyzing the data and fitting a regression model to it.

## 3. Analyze the Data
The fifth file is a Jupyter Notebook that loads the cleaned home data for analysis. The following is then analyzed:
- the location and variability of home prices
- the strength and nature of the correlations between price and predictor variables
- the stasticial significance of the differences in price between feature groups

## 4. Fit a Regression Model to the Data
The sixth and final file is a Jupyter Notebook that loads the cleaned home data for regression modeling. Various groups of features
are used to fit a linear regression model and their performance is compared using various metrics in order to determine which feature
set yields the most accurate predictions. One such model is then analyzed in more detail and adjusted in an attempt to maximize
its prediction accuracy.
