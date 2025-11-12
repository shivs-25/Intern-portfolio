# Checking if the sample employee DB from Git Hub has been loaded accurately.
USE employees;
SELECT COUNT(*) FROM departments; # Output = 9.
SELECT COUNT(*) FROM employees; # Output = 300,024.
SELECT COUNT(*) FROM salaries; # Output = 2844047.

# SET 1
# 1. Retrieve the first and last names of all employees from the 'employees' table.

SELECT first_name, last_name
FROM employees;

# 2. Find all departments with the name "Sales".

SELECT *
FROM departments
WHERE dept_name = 'Sales';

# 3. List all the job titles in the 'titles' table

SELECT DISTINCT title
FROM titles;

# 4. Show the 'emp_no', 'from_date' and 'to_date' for employees working in the 'Sales' department.

SELECT de.emp_no, de.from_date, de.to_date
FROM dept_emp de
JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Sales';

# 5. Display the employee number and their corresponding department number from the 'dept_emp' table.

SELECT emp_no, dept_no
FROM dept_emp;

# 6. Find the birth dates of all employees whose first name is 'John'

SELECT birth_date
FROM employees
WHERE first_name = 'John';

# 7. Show all department managers along with their department numbers

SELECT emp_no, dept_no
FROM dept_manager;

# 8. Retrieve the enployee number and title of employees whose title starts with 'Senior'

SELECT emp_no, title
FROM titles
WHERE title LIKE 'Senior%';

# 9. List the employee numbers and salaries from the salary table where the salary is greater than 50,000

SELECT emp_no, salary
FROM salaries
WHERE salary > 50000;

# 10. Find all employees who were hired after January 1, 2000

SELECT *
FROM employees
WHERE hire_date > '2000-01-01';


# SET 2
# 1. Find the highest salary for each employee

SELECT emp_no, MAX(salary) AS highest_salary
FROM salaries
GROUP BY emp_no;

# 2. List all the departments along with the number of employees in each department

SELECT dept_no, COUNT(emp_no) AS num_employees
FROM dept_emp
GROUP BY dept_no;

# 3. Retrieve the current department of each employee using the 'current_dept_emp' view

SELECT *
FROM current_dept_emp;

# 4. Show the number of employees who hold the title 'Manager'

SELECT COUNT(*) AS num_managers
FROM titles
WHERE title = 'Manager';

# 5. Find the employees who have worked in multiple departments

SELECT emp_no
FROM dept_emp
GROUP BY emp_no
HAVING COUNT(DISTINCT dept_no) > 1;

# 6. List the employee numbers and the total number of departments they have managed in their career
SELECT emp_no, COUNT(dept_no) AS managed_departments
FROM dept_manager
GROUP BY emp_no;

# 7. Display the employees whose salary was below 40,000 at any point

SELECT DISTINCT emp_no
FROM salaries
WHERE salary < 40000;

# 8. Find all the employees who are currently in a department but were previously in a different one

SELECT emp_no
FROM dept_emp
GROUP BY emp_no
HAVING COUNT(DISTINCT dept_no) > 1;

# 9. Get the department managers who have managed more than one department

SELECT emp_no
FROM dept_manager
GROUP BY emp_no
HAVING COUNT(DISTINCT dept_no) > 1;

# 10. Retreive the titles of employees who have held the same tiitle more than once

SELECT emp_no, title
FROM titles
GROUP BY emp_no, title
HAVING COUNT(*) > 1;