CREATE DATABASE restaurant;
USE restaurant;
drop database restaurant;
CREATE TABLE orders (
    bill_no VARCHAR(255),
    customer_name VARCHAR(255),
    phone VARCHAR(255),
    starter_total VARCHAR(255),
    main_total VARCHAR(255),
    snacks_total VARCHAR(255),
    total_amount DECIMAL(10, 2)
);
select * from orders;