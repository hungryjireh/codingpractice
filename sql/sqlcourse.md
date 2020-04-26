## SQLCOURSE

The following exercises were taken from [SQLCourse](http://www.sqlcourse2.com/).

## SELECT

1. From the items_ordered table, select a list of all items purchased for customerid 10449. Display the customerid, item, and price for this customer.

`SELECT customerid, item, price FROM items_ordered WHERE customerid = 10449;`

2. Select all columns from the items_ordered table for whoever purchased a Tent.

`SELECT * FROM items_ordered WHERE item = 'Tent';`

3. Select the customerid, order_date, and item values from the items_ordered table for any items in the item column that start with the letter "S".

`SELECT customerid, order_date, item FROM items_ordered WHERE item LIKE 'S%';`

4. Select the distinct items in the items_ordered table. In other words, display a listing of each of the unique items from the items_ordered table.

`SELECT DISTINCT(item) FROM items_ordered;`

## AGGREGATE FUNCTIONS

1. Select the maximum price of any item ordered in the items_ordered table. Hint: Select the maximum price only.

`SELECT MAX(price) FROM items_ordered;`

2. Select the average price of all of the items ordered that were purchased in the month of Dec.

`SELECT avg(price) FROM items_ordered WHERE order_date LIKE '%Dec%';`

3. What are the total number of rows in the items_ordered table?

`SELECT COUNT(*) FROM items_ordered;`

4. For all of the tents that were ordered in the items_ordered table, what is the price of the lowest tent? Hint: Your query should return the price only.

`SELECT MIN(price) FROM items_ordered WHERE item = 'Tent';`

## GROUP BY

1. How many people are in each unique state in the customers table? Select the state and display the number of people in each. Hint: count is used to count rows in a column, sum works on numeric data only.

`SELECT DISTINCT(state), count(*) FROM customers GROUP BY state;`

2. From the items_ordered table, select the item, maximum price, and minimum price for each specific item in the table. Hint: The items will need to be broken up into separate groups.

`SELECT item, min(price), max(price) FROM items_ordered GROUP BY item;`

3. How many orders did each customer make? Use the items_ordered table. Select the customerid, number of orders they made, and the sum of their orders.

`SELECT customerid, count(customerid), sum(price) FROM items_ordered GROUP BY customerid;`

## HAVING

1. How many people are in each unique state in the customers table that have more than one person in the state? Select the state and display the number of how many people are in each if it's greater than 1.

`SELECT state, count(*) as num_people FROM customers GROUP BY state HAVING num_people > 1; `

2. From the items_ordered table, select the item, maximum price, and minimum price for each specific item in the table. Only display the results if the maximum price for one of the items is greater than 190.00.

`SELECT item, MIN(price), MAX(price) FROM items_ordered GROUP BY item HAVING MAX(price) > 190;`

3. How many orders did each customer make? Use the items_ordered table. Select the customerid, number of orders they made, and the sum of their orders if they purchased more than 1 item.

`SELECT DISTINCT(customerid), COUNT(*) as num_orders, SUM(price) FROM items_ordered GROUP BY customerid HAVING num_orders > 1;`

## ORDER BY
1. Select the lastname, firstname, and city for all customers in the customers table. Display the results in Ascending Order based on the lastname.

`SELECT lastname, firstname, city FROM customers ORDER BY lastname ASC;`

2. Same thing as exercise #1, but display the results in Descending order.

`SELECT lastname, firstname, city FROM customers ORDER BY lastname DESC;`

3. Select the item and price for all of the items in the items_ordered table that the price is greater than 10.00. Display the results in Ascending order based on the price.

`SELECT item, price FROM items_ordered WHERE price > 10 ORDER BY price;`

## Combining Conditions & Boolean Operators

1. Select the customerid, order_date, and item from the items_ordered table for all items unless they are 'Snow Shoes' or if they are 'Ear Muffs'. Display the rows as long as they are not either of these two items.

`SELECT customerid, order_date, item FROM items_ordered WHERE item <> 'Ear Muffs' AND item <> 'Snow Shoes';`

2. Select the item and price of all items that start with the letters 'S', 'P', or 'F'.

`SELECT item, price FROM items_ordered WHERE item LIKE 's%' or item LIKE 'p%' or item LIKE 'F%';`

## IN & BETWEEN

1. Select the date, item, and price from the items_ordered table for all of the rows that have a price value ranging from 10.00 to 80.00.

`SELECT order_date, item, price FROM items_ordered WHERE price BETWEEN 10 AND 80;`

2. Select the firstname, city, and state from the customers table for all of the rows where the state value is either: Arizona, Washington, Oklahoma, Colorado, or Hawaii.

`SELECT firstname, city, state FROM customers WHERE state in ('Arizona', 'Washington', 'Oklahoma', 'Colorado', 'Hawaii');`

## Mathematical Functions

1. Select the item and per unit price for each item in the items_ordered table. Hint: Divide the price by the quantity.

`SELECT item, ROUND(price/quantity, 2) AS unit_price FROM items_ordered;`

## Table Joins, a must

1. Write a query using a join to determine which items were ordered by each of the customers in the customers table. Select the customerid, firstname, lastname, order_date, item, and price for everything each customer purchased in the items_ordered table.

`SELECT customers.customerid, customers.firstname, customers.lastname, items_ordered.order_date, items_ordered.item, items_ordered.price FROM customers INNER JOIN items_ordered ON customers.customerid = items_ordered.customerid;`

2. Repeat exercise #1, however display the results sorted by state in descending order.

`SELECT customers.state, customers.customerid, customers.firstname, customers.lastname, items_ordered.order_date, items_ordered.item, items_ordered.price FROM customers INNER JOIN items_ordered ON customers.customerid = items_ordered.customerid ORDER BY customers.state DESC;`