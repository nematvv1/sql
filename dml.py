
create table categories (
    category_id serial primary key,
    category_name varchar(50) not null,
    description varchar(100) not null
);

insert into categories (category_name, description) values
('Beverages', 'Soft drinks'),
('Condiments', 'Sweet sauces'),
('Confections', 'Desserts'),
('Dairy Products', 'Milk products'),
('Grains/Cereals', 'Bread and grains');

select * from categories;

-- UPDATE
update categories
set category_name = 'Updated Beverages'
where category_id = 1;

-- DELETE
delete from categories
where category_id = 5;


create table suppliers (
    supplier_id serial primary key,
    company_name varchar(50) not null,
    contact_name varchar(50) not null,
    contact_title varchar(30) not null,
    address varchar(50) not null,
    city varchar(30) not null,
    region varchar(20),
    country varchar(35) not null,
    phone varchar(24) not null
);

insert into suppliers values
(1,'Exotic Liquids','Charlotte','Manager','Street 1','London',null,'UK','111'),
(2,'New Orleans','Shelley','Admin','Street 2','New Orleans','LA','USA','222'),
(3,'Grandma Kelly','Regina','Sales','Street 3','Ann Arbor','MI','USA','333'),
(4,'Tokyo Traders','Yoshi','Marketing','Street 4','Tokyo',null,'Japan','444'),
(5,'Test Supplier','Ali','Owner','Street 5','Tashkent',null,'Uzbekistan','555');


select * from suppliers;

-- SUPPLIERS jadvaliga muallif ustuni qo‘shish
alter table suppliers add column muallif varchar(50);

-- muallif ustunini update qilish
update suppliers
set muallif = 'Admin'
where supplier_id = 1;


create table products (
    product_id serial primary key,
    product_name varchar(40) not null,
    supplier_id int references suppliers(supplier_id),
    category_id int references categories(category_id),
    quantity_per_unit varchar(50) not null,
    unit_price numeric(10,2) not null,
    units_in_stock smallint not null,
    units_on_order smallint not null,
    discontinued boolean not null
);

insert into products values
(1,'Chai',1,1,'10 boxes',18.00,39,0,false),
(2,'Chang',1,1,'24 bottles',19.00,17,40,true),
(3,'Aniseed Syrup',2,2,'12 bottles',10.00,13,70,false),
(4,'Chef Anton',3,2,'48 jars',22.00,53,0,false),
(5,'Ikura',4,4,'12 packs',31.00,31,0,false);

-- SELECT
select * from products;

-- 3 ustun update qilish
update products
set product_name='Updated Chai',
    unit_price=20.00,
    units_in_stock=50
where product_id=1;

-- yangi ustun qo‘shish
alter table products add column created_at date;

-- ustun nomini o‘zgartirish
alter table products rename column created_at to created_date;

-- 5-mahsulotni o‘chirish
delete from order_details where product_id = 5;  -- avval order_details dan
delete from products where product_id = 5;       -- keyin products dan


create table orders (
    order_id serial primary key,
    customer_id varchar(30) not null,
    order_date date not null,
    required_date date not null,
    shipped_date date
);

insert into orders values
(1,'C001','1997-01-01','1997-01-05','1997-01-10'),
(2,'C002','1997-03-01','1997-03-10','1997-03-15'),
(3,'C003','1997-05-01','1997-05-10','1997-05-20'),
(4,'C004','1997-07-01','1997-07-10','1997-08-01'),
(5,'C005','1997-09-01','1997-09-10','1997-09-25');

select * from orders;


create table order_details (
    order_id int references orders(order_id),
    product_id int references products(product_id),
    unit_price numeric(10,2),
    quantity smallint,
    discount numeric(3,2),
    primary key (order_id, product_id)
);

insert into order_details values
(1,1,18.00,5,0.1),
(1,2,19.00,3,0),
(2,3,10.00,7,0.05),
(3,4,22.00,4,0.2),
(4,1,18.00,6,0);


select * from order_details;

-- 1 ta ORDER_DETAILS update misol
update order_details
set quantity=10
where order_id=1 and product_id=1;

-- 1 ta ORDER_DETAILS delete misol
delete from order_details
where order_id=4 and product_id=1;
