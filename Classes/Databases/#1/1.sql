--1. Create a simple table countries with columns country_id, country_name, and region_id:
CREATE TABLE countries (
    country_id INT,
    country_name VARCHAR(100),
    region_id INT
);
--2. Create the structure of a table dup_countries similar to countries:
CREATE TABLE dup_countries LIKE countries;
--3. Create a table countries with a constraint NOT NULL on each column:
CREATE TABLE countries (
    country_id INT NOT NULL,
    country_name VARCHAR(100) NOT NULL,
    region_id INT NOT NULL
);
--4. Insert a record with your own values into the table countries:
INSERT INTO countries (country_id, country_name, region_id) 
VALUES (1, 'MyCountry', 101);
--5. Insert 3 rows by a single INSERT statement:
INSERT INTO countries (country_id, country_name, region_id) 
VALUES 
(2, 'CountryA', 102),
(3, 'CountryB', 103),
(4, 'CountryC', 104);
--6. Insert a record into the table countries ensuring that a combination of country_id and region_id is unique:
CREATE TABLE countries (
    country_id INT NOT NULL,
    country_name VARCHAR(100) NOT NULL,
    region_id INT NOT NULL,
    UNIQUE(country_id, region_id)
);
-- Inserting record with unique country_id and region_id
INSERT INTO countries (country_id, country_name, region_id) 
VALUES (5, 'CountryD', 105);