# donation-analytics-InsightDataEngineering
Coding challenge for Insight Data Engineering Fellowship application.

Written as a single python script using the numpy and collections libraries.

The code reads the itcont.txt file and goes through it one line at a time. It identifies whether a given line represents a repeat donor or a new donor. If it is a repeat donor, it then determines the recipient ID of the donation, zipcode, and year. If there are other donations from this zipcode and year to the same recipient, it then calculates the sum of all donations and the donation for the ith percentile, where the ith percentile is given by the file percentile.txt. It ouputs the results along with the total number of donations to the recipient ID for that zipcode and calendar year.
