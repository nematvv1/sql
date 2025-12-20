-- 1
-- select c.category_name,sum(od.quantity) from categories c
-- join products p on c.category_id=p.category_id
-- join order_details od on p.product_id=od.product_id
-- group by c.category_name

-- 2
-- select e.employee_id,e.first_name,e.last_name, count(o.order_id) from employees e
-- join orders o on e.employee_id=o.employee_id
-- where e.country='USA'
-- group by e.employee_id,e.first_name,e.last_name

-- 3
-- select e.country, count(o.order_id) from employees e
-- join orders o on e.employee_id=o.employee_id
-- group by e.country

-- -- 4
-- select c.customer_id,c.company_name,c.contact_name,c.contact_title,c.country,c.city,c.phone,sum(od.unit_price * od.quantity),count(distinct o.order_id) from customers c
-- join orders o on c.customer_id = o.customer_id
-- join order_details od on o.order_id = od.order_id
-- where to_char(o.order_date, 'YYYY') = '1997'
-- group by c.customer_id,c.company_name,c.contact_name,c.contact_title,c.country,c.city,c.phone


-- 5
-- select  p.product_id,p.product_name,sum(od.quantity) as total_quantity from products p
-- join order_details od on p.product_id = od.product_id
-- group by p.product_id, p.product_name

-- 6
-- select p.product_id,p.product_name,p.unit_price,c.company_name,o.order_id,o.order_date from products p
-- join order_details od on p.product_id = od.product_id
-- join orders o on od.order_id = o.order_id
-- join customers c on o.customer_id = c.customer_id
-- join shippers s on o.ship_via = s.shipper_id
-- where p.category_id = 1
-- group by p.product_id,p.product_name,p.unit_price,c.company_name,o.order_id,o.order_date
-- order by p.unit_price desc limit 10;