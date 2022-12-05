CREATE_TABLES_QUERY = """
    CREATE TABLE Shops (
    id serial,
    PRIMARY KEY (id),
    name varchar,
    address varchar NULL,
    staff_amount integer
    );
    CREATE TABLE Departments (
    id serial,
    PRIMARY KEY (id),
    sphere varchar,
    staff_amount integer,
    shop_id integer,
    FOREIGN KEY (shop_id) REFERENCES Shops (id)
    );
    CREATE TABLE Items (
    id serial,
    PRIMARY KEY (id),
    name varchar,
    description varchar NULL,
    price integer,
    department_id integer,
    FOREIGN KEY (department_id) REFERENCES Departments (id)
    );
    """

INSERT_INTO_TABLES_QUERY = """
    INSERT INTO Shops (name, address, staff_amount) VALUES
     ('Auchan', default, 250),
     ('IKEA', 'Street Žirnių g. 56, Vilnius, Lithuania.', 500);
    INSERT INTO Departments (sphere, staff_amount, shop_id) VALUES
     ('Furniture', 250, 1),
     ('Furniture', 300, 2),
     ('Dishes', 200, 2);
    INSERT INTO Items (name, description, price, department_id) VALUES
     ('Table', 'Cheap wooden table', 300, 1),
     ('Table', default, 750, 2),
     ('Bed', 'Amazing wooden bed', 1200, 2),
     ('Cup', default, 10, 3),
     ('Plate', 'Glass plate', 20, 3);
    """

QUERY_3_1 = "SELECT * FROM Items WHERE description IS NOT NULL;"

QUERY_3_2 = "SELECT DISTINCT sphere FROM Departments WHERE staff_amount > 200;"

QUERY_3_3 = "SELECT address FROM Shops WHERE name ILIKE 'i%';"

QUERY_3_4 = """
            SELECT DISTINCT name FROM Items i 
            JOIN Departments d ON i.department_id = d.id
            WHERE d.sphere = 'Furniture';
"""

QUERY_3_5 = """
            SELECT DISTINCT s.name FROM Shops s JOIN Departments d ON s.id = d.shop_id 
            JOIN Items i ON d.id = i.department_id WHERE i.Description IS NOT NULL;
"""

QUERY_3_6 = """
            SELECT i.name, i.description, i.price,
            d.sphere as department_sphere, d.staff_amount as department_staff_amount,
            s.name AS shop_name, s.address AS shop_address, s.staff_amount as shop_staff_amount
            FROM Items i
            JOIN Departments d ON d.Id = i.department_id
            JOIN Shops s ON d.shop_id = s.id;
"""

QUERY_3_7 = "SELECT Items.id FROM Items ORDER BY name LIMIT 4 OFFSET 3;"

QUERY_3_8 = """
            SELECT i.name, d.sphere FROM Items i
            JOIN Departments d ON i.department_id=d.id;
"""

QUERY_3_9 = """
            SELECT i.name, d.sphere FROM Items i
            LEFT JOIN Departments d ON i.department_id=d.id;
"""

QUERY_3_10 = """
            SELECT i.name, d.sphere FROM Departments d
            LEFT JOIN Items i ON i.department_id=d.id;
"""

QUERY_3_11 = """
            SELECT i.name, d.sphere FROM Items i
            LEFT JOIN Departments d ON i.department_id=d.id
            UNION
            SELECT i.name, d.sphere FROM Departments d
            LEFT JOIN Items i ON i.department_id=d.id;
"""


QUERY_3_12 = "SELECT i.name, d.sphere FROM Items i CROSS JOIN Departments d;"

QUERY_3_13 = """
            SELECT count(i.id), sum(i.price), max(i.price), min(i.price), avg(i.price)
            FROM Shops s JOIN Departments d ON s.id = d.shop_id 
            JOIN Items i ON d.id = i.department_id 
            GROUP BY s.id 
            HAVING count(i) > 1;
"""

QUERY_5_1 = "DELETE FROM Items WHERE price > 500 AND description IS NULL;"

QUERY_5_2 = """
            DELETE FROM Items i 
            WHERE i.id IN (
            SELECT i.id FROM Items i 
            JOIN Departments d ON d.id = i.department_id 
            JOIN Shops s ON s.id = d.shop_id 
            WHERE s.address IS NULL
            );
"""

QUERY_5_3 = """
            DELETE FROM Items i 
            WHERE i.id IN (
            SELECT d.id FROM Departments d 
            WHERE d.staff_amount < 225 OR d.staff_amount > 275
            );
"""


QUERY_5_4 = "TRUNCATE TABLE Shops, Departments, Items;"
