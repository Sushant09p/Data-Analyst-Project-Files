CREATE DATABASE IF NOT EXISTS hr_analytics;

USE hr_analytics;

DESCRIBE data;

SELECT * FROM data LIMIT 10;

SELECT COUNT(*) FROM data;

-- Key Statistics Summary of numeric columns  
SELECT
	AVG(Age) AS Avg_age,
    AVG(DailyRate) AS Avg_daily_rate,
    AVG(DistanceFromHome) AS Avg_distancefromhome,
    AVG(MonthlyIncome) AS Avg_monthlyincome,
    AVG(PercentSalaryHike) AS Avg_percentsalaryhike,
    AVG(TotalWorkingYears) AS Avg_totalworkingyear
FROM data;

-- Count of different job roles
SELECT JobRole, COUNT(*) AS Total_employees
FROM data
GROUP BY JobRole;

-- Count of attrition cases 
SELECT Attrition, COUNT(*) AS Attrition_count
FROM data
GROUP BY Attrition;

-- Attrition Analysis
-- Attrition Based on Age and Job Satisfaction 
SELECT
	AVG(JobSatisfaction) AS Avg_Job_Satisfaction,
    AVG(WorkLifeBalance) AS Avg_Work_life_Balance,
    AVG(Age) AS Avg_Age
FROM data
WHERE Attrition = 'Yes';

-- Attrition and Monthly Income
SELECT 
	Attrition,
    AVG(MonthlyIncome) AS avg_monthly_income
FROM data
GROUP BY Attrition;

-- Department wise Analysis
SELECT 
	Department,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Total_Attrition,
    COUNT(*) AS Total_employees,
    (SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS attrition_rate
FROM data
GROUP BY Department;

-- Job Satisfaction by Department 
SELECT
	Department,
    AVG(JobSatisfaction) AS Avg_Job_Satisfaction
FROM data
GROUP BY Department;

-- Performance by Salary Trends
SELECT
	PerformanceRating,
    AVG(PercentSalaryHike) AS Avg_Salary_Hike
FROM data
GROUP BY PerformanceRating;

-- Monthly Income by Job Role
SELECT 
	JobRole,
    AVG(MonthlyIncome) AS Avg_Monthly_Income
FROM data
GROUP BY JobRole;

-- Correlation of Work Life Balance and Job Involvement
SELECT
	AVG(JobInvolvement) AS Avg_JobInvolvement,
    AVG(JobSatisfaction) AS Avg_JobSatisfaction
FROM data
GROUP BY WorkLifeBalance;

-- Retention Factors
-- Factors Affecting Attrition 
SELECT 
	AVG(DistanceFromHome) AS Avg_DistanceFromHome,
    SUM(CASE WHEN Overtime = 'Yes' THEN 1 ELSE 0 END) AS Overtime_Count,
    AVG(TotalWorkingYears) As Avg_Work_Years,
    AVG(YearsAtCompany) AS Avg_Years_at_Company
FROM data
WHERE Attrition = 'Yes';
 

 