--Select employees with salary higher than 1000.00, ordered by ID and concatenate names:

SELECT id, 
       CONCAT(first_name, ' ', last_name) AS full_name, 
       job_title, 
       salary
FROM employees
WHERE salary > 1000.00
ORDER BY id;

--Update "Dentist" salaries by 10% and retrieve all salaries in ascending order:

UPDATE employees SET salary = salary * 1.10 WHERE job_title = 'Dentist';

--Retrieve all salaries ordered ascending:

SELECT id, 
       first_name, 
       last_name, 
       job_title, 
       salary
FROM employees
ORDER BY salary ASC;

--Delete employees from department 3 or 4, ordered by ID:

DELETE FROM employees
WHERE department_id IN (3, 4);

SELECT * 
FROM employees
ORDER BY id;