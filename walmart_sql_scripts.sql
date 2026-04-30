CREATE VIEW holiday_sales AS
SELECT 
    holiday_flag,
    AVG(weekly_sales) AS avg_sales,
    SUM(weekly_sales) AS total_sales
FROM walmart_sales
GROUP BY holiday_flag;


CREATE VIEW monthly_sales AS
SELECT 
    store,
    YEAR(date) AS year,
    MONTH(date) AS month,
    SUM(weekly_sales) AS monthly_sales
FROM walmart_sales
GROUP BY store, YEAR(date), MONTH(date);

CREATE VIEW store_performance AS
SELECT 
    store,
    AVG(weekly_sales) AS avg_sales,
    MAX(weekly_sales) AS peak_sales,
    MIN(weekly_sales) AS lowest_sales
FROM walmart_sales
GROUP BY store;

CREATE VIEW economic_sensitivity AS
SELECT 
    high_fuel,
    high_cpi,
    high_unemployment,
    AVG(weekly_sales) AS avg_sales
FROM walmart_sales
GROUP BY high_fuel, high_cpi, high_unemployment;

CREATE VIEW stress_index_view AS
SELECT 
    store,
    date,
    weekly_sales,
    (high_fuel + high_cpi + high_unemployment) AS stress_index
FROM walmart_sales;


CREATE VIEW sales_economic_factors_view AS
SELECT 
    date,
    store,
    weekly_sales,
    fuel_price,
    cpi,
    unemployment,
    temperature
FROM walmart_sales;

CREATE VIEW sales_with_temperature AS
SELECT 
    date,
    store,
    weekly_sales,
    temperature,
    fuel_price,
    cpi,
    unemployment
FROM walmart_sales;

CREATE VIEW sales_temperature_view AS
SELECT 
    date,
    store,
    weekly_sales,
    temperature
FROM walmart_sales;
