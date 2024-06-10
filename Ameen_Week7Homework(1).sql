-- 7.1 HW Questions
-- 1. Using EVre	gistry, Write a query to select the ModelYear, Make, and Model off all of the vehicles in the registry.
	SELECT ModelYear, Make, Model
	FROM EVRegistry;
	-- 2. Using the EVRegistry table, Write a query that lists all of the unique types of EV's. Your result set should have one column, ElectricVehicleType.	
	SELECT DISTINCT ElectricVehicleType
	FROM EVRegistry;
	-- 3. Using the EVRegistry, Write a query that shows all of the information on Battery Electric Vehicles (BEV) that are in the registry.
	SELECT *
	FROM EVRegistry
	WHERE ElectricVehicleType = "Battery Electric Vehicle (BEV)"
	--4. Using the EVRegistry, write a query that returns the Make and Model of all of the EV's that have a BaseMSRP between 20000 and 35000?
	SELECT Make, Model
	FROM EVRegistry
	WHERE BaseMSRP BETWEEN 20000 AND 35000;
	-- 7.2 HW Questions
	-- 1. Using EVRegistry, write a query to find a record where the City attribute is NULL. Return all of the available columns.
	SELECT *
	FROM EVRegistry
	WHERE City IS NULL;
	-- 2. Write a query to find the make, model, and ElectricVehicleType where the VIN number has that ends in '3E1EA1J'.
	SELECT Make, Model, ElectricVehicleType
	FROM EVRegistry
	WHERE VIN like "%3E1EA1J";
	-- 3. Select the ModelYear, make, model, ElectricVehicleType, and range of the Tesla vehicles or Chevrolet vehicles in the registry. Order the result set by Make and Model year in from newest to oldest.
	SELECT ModelYear, Make, Model, ElectricVehicleType, ElectricRange
	FROM EVRegistry
	WHERE Make IN ("TESLA", "CHEVROLET")
	ORDER BY ModelYear DESC;
	-- 4. Using EVCharging, Write a query to find out how many times those stations were used. Order them by the most used to the least used and limit the output to 5 records.
	SELECT stationId, count(sessionID) AS CountUseage
	FROM EVCharging
	GROUP BY stationID
	ORDER BY CountUseage DESC
	LIMIT 5;
	-- 5. Using EVCharging, For the folks who charged longer than 0.5 hours, show the min and max of the charging time for each user. Your output columns should be userid, minTime, and maxTime. Order this result set by the last two columns respectively.
	SELECT userId, min(chargeTimeHrs) AS MinChargeTime, max(chargeTimeHrs) AS MaxChargeTime
	FROM EVCharging
	WHERE chargeTimeHrs > 0.5
	GROUP BY userId
	ORDER BY MinChargeTime, MaxChargeTime;