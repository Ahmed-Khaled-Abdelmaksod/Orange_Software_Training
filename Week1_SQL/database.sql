-- User Table
CREATE TABLE User (
	UserId INT ,
  	Fname VARCHAR(20) NOT NULL,
  	Mname CHAR(1),
  	Lname VARCHAR(20),
  	Email VARCHAR(25),
  	Age INT NOT NULL,
  	Date_of_birth DATE,
 	Phone VARCHAR(11) NOT NULL,
  	Password VARCHAR(20),
  	Ssn CHAR(14) UNIQUE,
  	PRIMARY KEY (UserId)
);

-- Admin Table
CREATE TABLE Admin (
	AdminId INT ,
  	Salary FLOAT NOT NULL,
  	Date_of_join DATE,
 	UserId INT,
    PRIMARY KEY (AdminId),
  	FOREIGN KEY (UserId) REFERENCES User(UserId)
);

-- Customer Table
CREATE TABLE Customer (
	CustomerId INT,
  	Bank_card INT NOT NULL,
  	UserId INT,
  	CartId INT,
  	PRIMARY KEY(CustomerId),
  	FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE , 
  	FOREIGN KEY (CartId) REFERENCES Cart(CartId) ON DELETE CASCADE  
);

-- Cart Table
CREATE TABLE Cart (
	CartId Int,
  	Total_cost FLOAT,
  	PRIMARY KEY (CartId)
);

-- Cart_Items Table
CREATE TABLE Cart_Items (
	CartId INT,
  	ItemId INT,
  	PRIMARY KEY(CartId,ItemId),
  	FOREIGN KEY(CartId) REFERENCES Cart(CartId) ON DELETE CASCADE,
  	FOREIGN KEY(ItemId) REFERENCES Item(ItemId) ON DELETE CASCADE

);

-- Orderr Table
CREATE TABLE Orderr (
	OrderId INT,
  	CustomerId INT,
  	Order_Date DATE NOT NULL,
  	OrderDetailsId INT,
  	PRIMARY KEY (OrderId),
  	FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId),
  	FOREIGN KEY (OrderDetailsId) REFERENCES Order_Details(OrderDetailsId)
);

-- Payment_Information Table
CREATE TABLE Payment_Information (
	CustomerId INT,
  	OrderId INT,
  	Payment_date Date NOT NULL,
  	Payment_method VARCHAR (20) CHECK (Payment_method IN ('Cash','Visa')),
  	PRIMARY KEY (CustomerId,OrderId),
  	FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId) ON DELETE CASCADE,
  	FOREIGN KEY (OrderId) REFERENCES Orderr(OrderId) ON DELETE CASCADE
);

-- Order_Details Table
CREATE TABLE Order_Details (
	OrderDetailsId INT,
  	Taxes FLOAT,
  	Discount FLOAT,
  	PRIMARY KEY (OrderDetailsId)
);

-- Item Table 
CREATE TABLE Item (
	ItemId INT,
  	OrderDetailsId INT,
  	Quantity INT,
  	ProductId INT,
  	PRIMARY KEY (ItemId),
  	FOREIGN KEY (OrderDetailsId) REFERENCES Order_Details(OrderDetailsId) ON DELETE SET NULL ,
  	FOREIGN KEY (ProductId) REFERENCES Product(ProductId) ON DELETE CASCADE
);

-- Product Table
CREATE TABLE Product (
	ProductId INT,
  	Name VARCHAR(30),
  	Description VARCHAR(1000),
  	Price FLOAT NOT NULL,
  	Average_rate FLOAT,
  	CategoryId INT,
  	PRIMARY KEY (ProductId) ,
  	FOREIGN KEY (CategoryId) REFERENCES Category(CategoryId) ON DELETE CASCADE
);

-- Product_Image Table
CREATE TABLE Product_Image (
	ImageId INT,
  	image VARCHAR(100) NOT NULL,
  	ProductId INT,
  	PRIMARY KEY (ImageId) ,
  	FOREIGN KEY (ProductId) REFERENCES Product(ProductId) ON DELETE CASCADE
);

-- Category Table
CREATE TABLE Category (
	CategoryId INT,
  	name VARCHAR(30),
  	Description VARCHAR(1000) NOT NULL,
  	ParentCategory INT,
  	PRIMARY KEY (CategoryId) ,
  	FOREIGN KEY (ParentCategory) REFERENCES Category(CategoryId) ON DELETE CASCADE
);

-- Review Table
CREATE TABLE Review (
	ReviewId INT,
  	CustomerId INT,
  	ProductId INT,
  	Comment VARCHAR(300),
  	Rate FLOAT,
  	PRIMARY KEY (ReviewId),
  	FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId) ON DELETE CASCADE,
  	FOREIGN KEY (ProductId) REFERENCES Product(ProductId) ON DELETE CASCADE
);