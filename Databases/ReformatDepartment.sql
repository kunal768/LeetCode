SELECT
    id,
    SUM(Jan_Revenue) Jan_Revenue,
    SUM(Feb_Revenue) Feb_Revenue,
    SUM(Mar_Revenue) Mar_Revenue,
    SUM(Apr_Revenue) Apr_Revenue,
    SUM(May_Revenue) May_Revenue,
    SUM(Jun_Revenue) Jun_Revenue,
    SUM(Jul_Revenue) Jul_Revenue,
    SUM(Aug_Revenue) Aug_Revenue,
    SUM(Sep_Revenue) Sep_Revenue,
    SUM(Oct_Revenue) Oct_Revenue,
    SUM(Nov_Revenue) Nov_Revenue,
    SUM(Dec_Revenue) Dec_Revenue
FROM (
    SELECT
        id,
        CASE WHEN month LIKE 'Jan' THEN revenue ELSE null END Jan_Revenue,
        CASE WHEN month LIKE 'Feb' THEN revenue ELSE null END Feb_Revenue,
        CASE WHEN month LIKE 'Mar' THEN revenue ELSE null END Mar_Revenue,
        CASE WHEN month LIKE 'Apr' THEN revenue ELSE null END Apr_Revenue,
        CASE WHEN month LIKE 'May' THEN revenue ELSE null END May_Revenue,
        CASE WHEN month LIKE 'Jun' THEN revenue ELSE null END Jun_Revenue,
        CASE WHEN month LIKE 'Jul' THEN revenue ELSE null END Jul_Revenue,
        CASE WHEN month LIKE 'Aug' THEN revenue ELSE null END Aug_Revenue,
        CASE WHEN month LIKE 'Sep' THEN revenue ELSE null END Sep_Revenue,
        CASE WHEN month LIKE 'Oct' THEN revenue ELSE null END Oct_Revenue,
        CASE WHEN month LIKE 'Nov' THEN revenue ELSE null END Nov_Revenue,
        CASE WHEN month LIKE 'Dec' THEN revenue ELSE null END Dec_Revenue
    FROM Department
)
GROUP BY id
