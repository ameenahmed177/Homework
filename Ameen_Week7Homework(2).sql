-- 7.3 HW Questions
-- 1. Using EVCharging, Which day of the week has the highest average charging time? Round the answer to 2 decimal points.
SELECT weekday, round(avg(chargeTimeHrs), 2) AS AverageTime
FROM EVCharging
GROUP BY weekday
ORDER BY AverageTime DESC;
-- 2. Using EV charging, Find the total power consumed from charging EV's by each User. Return the userId and name the calculated column, totalPower. Round the answer to 2 decimal points and list the out put in highest to lowest order. Limit the order to the top 15 users.
SELECT userId, round(sum(kwhTotal), 2) AS totalPower
FROM EVCharging
GROUP BY userId
ORDER BY totalPower DESC
LIMIT 15;
-- 3. Using dimfacility and factCharge, write a query to find out which type of facility (GROUP BY) has the most amount of charging stations. Return type Facility and name the calculated column numStation. Order the result set from highest to lowest number of charging stations.
SELECT dimFacility.typeFacility, count(stationId) AS numStation
FROM dimFacility
INNER JOIN factCharge
ON dimFacility.FacilityKey = factCharge.facilityID
GROUP BY dimFacility.typeFacility
ORDER BY numStation DESC;
-- 4. In your own words, Briefly explain Primary Keys and Foreign Keys.
-- Primary keys are unique identifiers for each row in a table. They are used to ensure that each row in a table is unique and can be used to reference a specific row in a table. Foreign keys are used to create relationships between tables. They are used to link a column in one table to a column in another table. This is done to ensure that the data in the column in the first table is valid and that it matches the data in the column in the second table. Foreign keys are used to enforce referential integrity between tables.
-- 5. Using EV Charging, For the folks who charged longer than one hour, show the min and max of the charging time for each user. Your output columns should be userid, minTime, and maxTime. Order this result set by the last two columns respectively. HINT: USE HAVING
SELECT userId, min(chargeTimeHrs) AS minTime, max(chargeTimeHrs) AS maxTime
FROM EVCharging
GROUP BY userId
HAVING min(chargeTimeHrs)> 1
ORDER BY minTime, maxTime;