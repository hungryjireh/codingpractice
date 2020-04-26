1. Select Query

| Field       | Type        |
| ------------| ------------|
| ID          | NUMBER      |
| NAME        | VARCHAR2(17)|
| COUNTRYCODE | VARCHAR2(3) |
| DISTRICT    | VARCHAR2(20)|
| POPULATION  | NUMBER      |

"Query all columns for all American cities in CITY with populations larger than 100000. The CountryCode for America is USA."

`SELECT * FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;`

2. Group By

"Query the two cities in STATION with the longest CITY name, as well as the respective lengths (i.e.: number of characters in the name). If there is more than one longest city, choose the one that comes first when ordered alphabetically."

`SELECT CITY, LENGTH(CITY) AS CITY_LENGTH FROM STATION GROUP BY CITY ORDER BY CITY_LENGTH DESC, CITY ASC LIMIT 1;`

3. Like and Distinct

"Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates."

`SELECT DISTINCT(CITY) FROM STATION WHERE CITY LIKE 'a%' OR CITY LIKE 'e%' OR CITY LIKE 'i%' OR CITY LIKE 'o%' OR CITY LIKE 'u%';`

REGEXP: "Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates."

`SELECT DISTINCT(CITY) FROM STATION WHERE CITY RLIKE '^[aeiouAEIOU].*[aeiouAEIOU]$';`

- "^" refers to the position just before the first character of the string
- "." refers to matching any character except for newline
- "*" refers to any number of times (zero or more)

REGEXP NOT: "Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates."

`SELECT DISTINCT(CITY) FROM STATION WHERE CITY RLIKE '^[^aeiouAEIOU](\w|\s)*.';`

- "[^aeiouAEIOU]" means NOT match.

REGEXP ending string: "Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates."

`SELECT DISTINCT(CITY) FROM STATION WHERE CITY RLIKE '(\w|\s)*.[^aeiouAEIOU]$';`

- "$" refers to the position just after the last character of the string.

4. Aggregate functions

| Name     | Description                                             |
| ---------| --------------------------------------------------------|
| MIN      | returns the smallest value in a given column            |
| MAX      | returns the largest value in a given column             |
| SUM      | returns the sum of the numeric values in a given column |
| AVG      | returns the average value of a given column             |
| COUNT    | returns the total number of values in a given column    |
| COUNT(*) | returns the number of rows in a table                   |

5. Having

The HAVING clause allows you to specify conditions on the rows for each group AFTER the initial query.

6. Arithmetic operators

| Name     | Description                                             |
| ---------| --------------------------------------------------------|
| ABS(x)      | returns the absolute value of x                                 |
| SIGN(x)     | returns the sign of input x as -1, 0, or 1 (negative, zero, or positive respectively) |
| MOD(x,y)      | modulo - returns the integer remainder of x divided by y (same as x%y) |
| FLOOR(x)      | returns the largest integer value that is less than or equal to x            |
| CEILING(x)    | returns the smallest integer value that is greater than or equal to x      |
| POWER(x,y) | returns the value of x raised to the power of y                 |
| ROUND(x) | returns the value of x rounded to the nearest whole integer          |
| ROUND(x,d) | returns the value of x rounded to the number of decimal places specified by the value d  |
| SQRT(x,y) | returns the square-root value of x                   |