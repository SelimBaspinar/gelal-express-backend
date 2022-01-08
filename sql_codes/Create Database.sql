DROP SCHEMA IF EXISTS gelal_express_database;
CREATE SCHEMA gelal_express_database;
USE gelal_express_database;

CREATE TABLE users (
	uid INT AUTO_INCREMENT PRIMARY KEY,
    uuuid VARCHAR(36) DEFAULT (uuid()) UNIQUE,
    name VARCHAR(128) NOT NULL,
    surname VARCHAR(128) NOT NULL,
    email VARCHAR(320) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    phone_number VARCHAR(10) NOT NULL UNIQUE,
    address VARCHAR(128) NOT NULL
);

CREATE TABLE role (
	rid INT AUTO_INCREMENT PRIMARY KEY,
    ruuid VARCHAR(36) DEFAULT (uuid()) UNIQUE,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE permission (
	pid INT AUTO_INCREMENT PRIMARY KEY,
    puuid VARCHAR(36) DEFAULT (uuid()) UNIQUE,
    name VARCHAR(128) NOT NULL,
    permissionGranted boolean NOT NULL
);

CREATE TABLE category (
	cid INT AUTO_INCREMENT PRIMARY KEY,
    cuuid VARCHAR(36) DEFAULT (uuid()) UNIQUE,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE subCategory (
	scid INT AUTO_INCREMENT PRIMARY KEY,
    scuuid VARCHAR(36) DEFAULT (uuid()) UNIQUE,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE product (
	pid INT AUTO_INCREMENT PRIMARY KEY,
    puuid VARCHAR(36) DEFAULT (uuid()) UNIQUE,
    name VARCHAR(128) NOT NULL,
    price INT NOT NULL,
    description VARCHAR(1024) NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE hasRole (
	uuuid VARCHAR(36) UNIQUE,
    ruuid VARCHAR(36) UNIQUE,
    FOREIGN KEY(uuuid) REFERENCES users(uuuid),
    FOREIGN KEY(ruuid) REFERENCES role(ruuid)
);

CREATE TABLE can (
	ruuid VARCHAR(36) UNIQUE,
	puuid VARCHAR(36) UNIQUE,
    FOREIGN KEY(ruuid) REFERENCES role(ruuid),
    FOREIGN KEY(puuid) REFERENCES permission(puuid)
);

CREATE TABLE sub (
	cuuid VARCHAR(36) UNIQUE,
	scuuid VARCHAR(36) UNIQUE,
    FOREIGN KEY(cuuid) REFERENCES category(cuuid),
    FOREIGN KEY(scuuid) REFERENCES subCategory(scuuid)
);

CREATE TABLE productCategory (
	puuid VARCHAR(36) UNIQUE,
	scuuid VARCHAR(36) UNIQUE,
    FOREIGN KEY(puuid) REFERENCES product(puuid),
    FOREIGN KEY(scuuid) REFERENCES subCategory(scuuid)
);

CREATE TABLE chatTable (
	muuid VARCHAR(36) DEFAULT (uuid()) UNIQUE,
	uuuid VARCHAR(36) NOT NULL,
	ouuuid VARCHAR(36) NOT NULL,
    FOREIGN KEY(uuuid) REFERENCES users(uuuid),
    FOREIGN KEY(ouuuid) REFERENCES users(uuuid)
);

CREATE TABLE message (
	mid INT AUTO_INCREMENT PRIMARY KEY,
    muuid VARCHAR(36) NOT NULL,
	message VARCHAR(1024) NOT NULL,
	senderUuid VARCHAR(36) NOT NULL,
	date DATE NOT NULL,
    FOREIGN KEY(senderUuid) REFERENCES users(uuuid),
    FOREIGN KEY(muuid) REFERENCES chatTable(muuid)
);