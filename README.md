# Three Scraper

## Description
This is a script built to scrape certain information from Three's roaming support page. 
http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad

## Spec
Write some code to scrape Three’s roaming abroad page for information on all out of allowance rates. Specifically, find the cost of doing each action listed below (DATA POINTS) for each of the countries listed

- ### Data Points
  - Calling back to the UK
  - Texting back to the UK
  - Receiving a call
  - Using internet data.

- ### From Countries
  - Brazil
  - South Africa
  - Portugal
  - Chile
  - Iceland
  - China
  - Madagascar

## Notes on design decisions
- I have included the geckodriver binaries in the project folder for convenience, however to reduce the project size, it could be assumed the relevant driver would be in the PATH, eliminating the need to include the binaries. 

- I opted to use a class mainly due to the driver being used in multiple functions, and I prefer to avoid making the driver a global variable. 

- Within scraper.read_table, I chose to loop over each row of the table, rather than targetting specific rows, to avoid potential issues with rows being in an inconsistent order, or potential changes to order in the future.

- I chose to scrape all urls for the countries at the start, for speed purposes. 
- Some general design decisions would be changed to allow more flexibility, such as being able to search for any country, although this would result in a slower scrape. 
  - This would include accepting a list of countries during initialisation of the class
  - Not getting all urls ahead of time, and instead running the full cost search per country

- The next thing to do would be to write few tests, to check that the data being scraped is consistent, that no data is being missed, and that the pages are loading correctly, however due to time constraints, I've not been able to write them. I intend on experimenting with the TDD approach in the future to avoid this sort of issue in going forward.
