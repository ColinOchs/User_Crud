
--creates a user database table:

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);
--create a vehicle_type table
CREATE TABLE vehicle_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

--CREATES A VEHICLE TABLE
CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(45) NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    v_type INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY (owner_id) REFERENCES user(id)
);

--insert dummy data:
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Ned",
    "Flanders",
    "Stuff"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jefferson",
    "D'Arcy",
    "Other Stuff"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Glenn",
    "Quagmire",
    "Lots of Stuff"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Cosmo",
    "Kramer",
    "All kinds of stuff"
);
--create some dummy data for vehicle types:
INSERT INTO vehicle_type (description) VALUES ('Car');
INSERT INTO vehicle_type (description) VALUES ('Truck');
INSERT INTO vehicle_type (description) VALUES ('SUV');
INSERT INTO vehicle_type (description) VALUES ('Motorcycle');
INSERT INTO vehicle_type (description) VALUES ('Van');
--CREATE SOME DUMMY DATA FOR VEHICLES:
INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "white",
    "ECTO-1",
    1,
    1
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "red",
    "ASSMAN",
    4,
    2
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "silver",
    "OUTATIME",
    1,
    3
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "yellow",
    "TODFTHR",
    3,
    2
);
--join two tables: user and vehicle:

SELECT user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle.v_type as vehicle_type
FROM user INNER JOIN vehicle
ON user.id = vehicle.owner_id;

--join three tables: user, vehicle and vehicle_type:

SELECT user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle_type.description
FROM user
INNER JOIN vehicle ON user.id = vehicle.owner_id
INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;