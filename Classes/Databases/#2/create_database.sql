CREATE TABLE EmployeeStatus(
    EmployeeStatusId INT PRIMARY KEY,
    StatusDescription VARCHAR(45)
);


CREATE TABLE Technican(
    EmployeeId INT PRIMARY KEY,
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    EmailAddress VARCHAR(45) NOT NULL,
    AnnualSalary INT NOT NULL,
    SpecialSkill VARCHAR(45),
    EmployeeStatusId INT NULL,
    CONSTRAINT fk_EmployeeStatus FOREIGN KEY (EmployeeStatusId) REFERENCES EmployeeStatus(EmployeeStatusId)
);


CREATE TABLE SerivceStatus(
    ServiceStatusId INT PRIMARY KEY,
    StatusDescription VARCHAR(45)
);


CREATE TABLE City(
   CityId INT PRIMARY KEY,
   CityName VARCHAR(45)
);
 

CREATE TABLE Building(
   BuildingId INT PRIMARY KEY,
   CityId INT NULL,
   CONSTRAINT fk_CityId FOREIGN KEY (CityId) REFERENCES City(CityId),
   Floors INT
);


CREATE TABLE ElevatorType(
   ElevatorTypeId INT PRIMARY KEY,
   TypeName VARCHAR(45)
);


CREATE TABLE ElevatorModel(
   ElevatorModelId INT PRIMARY KEY,
   ModelName INT,
   Speed INT,
   MaxWeight INT,
   PeopleLimit INT,
   ElevatorTypeId INT NULL,
   CONSTRAINT fk_ElevatorTypeId FOREIGN KEY (ElevatorTypeId) REFERENCES ElevatorType(ElevatorTypeId)
);

CREATE TABLE Elevator(
    ElevatorId INT PRIMARY KEY,
    ElevatorModelId INT NULL,
    CONSTRAINT fk_ElevatorModelId FOREIGN KEY (ElevatorModelId) REFERENCES ElevatorModel(ElevatorModelId),
    BuildingId INT NULL,
    CONSTRAINT fk_BuildingId FOREIGN KEY (BuildingId) REFERENCES Building(BuildingId),
    InstallationDate DATE
);


CREATE TABLE ServiceActivity(
    ServiceActivityId INT PRIMARY KEY,
    EmployeeId INT NULL,
    CONSTRAINT fk_EmployeeId FOREIGN KEY (EmployeeId) REFERENCES Technican(EmployeeId),
    ElevatorId INT NULL,
    CONSTRAINT fk_ElevatorId FOREIGN KEY (ElevatorId) REFERENCES Elevator(ElevatorId),
    ServiceDateTime DATE,
    ServiceDescription VARCHAR(45),
    ServiceStatusId INT NULL,
    CONSTRAINT fk_ServiceStatusId FOREIGN KEY (ServiceStatusId) REFERENCES SerivceStatus(ServiceStatusId)
);