/*
	Northwind
    Tue Hellstern
    Database - 2024
*/

DROP DATABASE IF EXISTS northwind;
CREATE DATABASE IF NOT EXISTS northwind;
USE northwind;

# ---------------------------------------------------------------------- #
# Tables                                                                 #
# ---------------------------------------------------------------------- #
# ---------------------------------------------------------------------- #
# Add table "Products"                                                   #
# ---------------------------------------------------------------------- #

CREATE TABLE `Products` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `Name` VARCHAR(15) NOT NULL,
    `Category` VARCHAR(15) NOT NULL,
    `Price` MEDIUMTEXT,
    `Brand` MEDIUMTEXT,
    `Description` MEDIUMTEXT,
    `im_url` MEDIUMTEXT,
    CONSTRAINT `PK_Categories` PRIMARY KEY (`ID`)
);
CREATE INDEX `Name` ON `Products` (`Name`);

# ---------------------------------------------------------------------- #
# Add table "Start_inventory"                                            #
# ---------------------------------------------------------------------- #

CREATE TABLE `Start_inventory` (
    `ProductID` VARCHAR(5) NOT NULL,
    `Quantity` VARCHAR(40) NOT NULL
);

# ---------------------------------------------------------------------- #
# Add table "Orders"                                                  #
# ---------------------------------------------------------------------- #

CREATE TABLE `Orders` (
    `OrderID` INTEGER NOT NULL AUTO_INCREMENT,
    `dato` date,
    `CustomerID` VARCHAR(20) NOT NULL,
    `products` VARCHAR(10) NOT NULL,
    `price` VARCHAR(30),
    `status` VARCHAR(25),
    CONSTRAINT `PK_Orders` PRIMARY KEY (`OrderID`)
);

# ---------------------------------------------------------------------- #
# Add table "OrderLines"                                                 #
# ---------------------------------------------------------------------- #

CREATE TABLE `OrderLines` (
    `OrderID` INTEGER NOT NULL,
    `ProductID` VARCHAR(20) NOT NULL
);

# ---------------------------------------------------------------------- #
# Add table "Suppliers"                                                 #
# ---------------------------------------------------------------------- #

CREATE TABLE `Suppliers` (
    `Brand` VARCHAR(255),
    `Priority` VARCHAR(20) NOT NULL
);


# ---------------------------------------------------------------------- #
# Add table "Restocks"                                                     #
# ---------------------------------------------------------------------- #

CREATE TABLE `Restocks` (
    `OrderDate` date,
    `DeliveryDate` date,
    `ProductID` integer,
    `amount`integer,
    `Supplier` varchar(255)
);




