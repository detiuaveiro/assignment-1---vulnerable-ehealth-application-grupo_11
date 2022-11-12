DROP TABLE IF EXISTS app_user;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS appointment;
DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS feedback;


CREATE TABLE app_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(40),
    password_ VARCHAR(20) NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    UNIQUE (email)
);

CREATE TABLE doctor (
    id INTEGER NOT NULL,
    speciality VARCHAR(30) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(id) REFERENCES app_user (id) ON DELETE CASCADE
);

CREATE TABLE appointment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    date_ DATE NOT NULL,
    time_ TIME NOT NULL,
    patient_id VARCHAR(30) NOT NULL,
    type_ VARCHAR(30) NOT NULL,
    status_ VARCHAR(30) NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES app_user (id),
    FOREIGN KEY(doctor_id) REFERENCES doctor (id)
);

CREATE TABLE test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES app_user (id)
);

CREATE TABLE feedback (
    test_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    description_ VARCHAR(100) NOT NULL,
    date_time DATETIME NOT NULL,
    FOREIGN KEY(test_id) REFERENCES test (id),
    FOREIGN KEY(doctor_id) REFERENCES doctor (id),
    PRIMARY KEY (test_id, doctor_id)
);
