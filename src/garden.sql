PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE people (
	ID INT,
	name TEXT,
	email TEXT,
	phone INT
);

CREATE TABLE plants (
	ID INT,
	name TEXT,
	type TEXT,
	owner INT,
	FOREIGN KEY(owner) REFERENCES people(ID)
);

CREATE TABLE plant_log (
	ROWID INT,
	plant_ID INT,
	moist INT,
	time TIMESTAMP,
	FOREIGN KEY(plant_ID) REFERENCES plants(ID)
);

CREATE TABLE office_log (
	ROWID INT,
	humidity INT,
	temp INT,
	time TIMESTAMP
);

COMMIT;
