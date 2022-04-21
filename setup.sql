
--creates a user database table:

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);
--insert dummy data:
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Chet",
    "Chetson",
    "Stuff"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Dougie",
    "Benders",
    "Other Stuff"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Bill",
    "Dingleberry",
    "Lots of Stuff"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Carl",
    "Winslow",
    "All kinds of stuff"
);

