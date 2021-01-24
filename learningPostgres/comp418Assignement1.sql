CREATE TABLE comp418assignement1;

CREATE TABLE IF NOT EXISTS student (
    sid serial PRIMARY KEY,
    name VARCHAR (50) NOT NULL,
    address VARCHAR (255) NOT NULL,
    telephone INTEGER NOT NULL,
    age SMALLINT NOT NULL
);
CREATE TABLE IF NOT EXISTS course (
    courseno serial PRIMARY KEY,
    title VARCHAR ( 50 ) NOT NULL,
    department VARCHAR ( 50 ) NOT NULL,
    numberofcredits SMALLINT NOT NULL,
    coursefees SMALLINT NOT NULL
);-- course fee is small int

CREATE TABLE IF NOT EXISTS registration (
    fk_student SMALLINT REFERENCES student(sid) NOT NULL,
    fk_courseno SMALLINT REFERENCES course(courseno) NOT NULL,
    startdate DATE NOT NULL,
    completedate DATE NOT NULL,
    grade SMALLINT NOT NULL
);

-- we made a mistake in the data. preferable to store telephone # as varchar than integer (size)
ALTER TABLE student 
ALTER COLUMN telephone TYPE VARCHAR ( 50 );


-- sudo su postgres
-- \c {database name} to connect db
-- \dt+ list database's table + for more info
-- \d {tablename} shows table

-- GRANT ALL PRIVILEGES ON DATABASE comp418assignement1 TO root;
-- psql postgresql://root:PASSWORD@127.0.0.1:5432/comp418assignement1
-- sudo pg_dump -U root comp418assignement1 > practicedb.pgsql
-- querry one
EXPLAIN ANALYSE SELECT s.SID, s.name
FROM student s
JOIN registration r
    ON s.SID = r.fk_student
WHERE r.fk_courseno = 51 AND r.grade >= 70;
-- querry two
EXPLAIN ANALYSE SELECT c.courseno,c.title,COUNT(r.fk_student) as blwAvg
FROM course c
JOIN registration r
    ON r.fk_courseno = c.courseno
WHERE r.grade <50
GROUP BY c.courseno
-- querry three
SELECT c.courseno,c.title
FROM course c
WHERE c.coursefees BETWEEN 400 AND 600;
-- querry four 
SELECT *
FROM course;
-- querry five
UPDATE course
   SET coursefees = coursefees + 6;

-- EXPLAIN ANALYZE /EXPLAIN VERBOSE
-- https://www.youtube.com/watch?v=Kdjz2e8HYPU