#================== savollari==================
# 1- savol 1- kategoriyadagi narxi 10$ dan baland bolgan maxsulotlar 96 yilning har bir oyida qanchadan zakas tushgan
# 2- savol 3- kategoriyadagi eng arzon maxsulotga 97-7 oyida yetkazib bergan suplayertlar
# 3- savol 98- yilning mart oyidagi zakaslarni sotib olgan mijozlartga xizmat korsatgan xodimlar
# 4-savol har bir kategoriyadagi eng qimmat maxsulot 96 yilda qanchadan sotilgan
# 5- savol 97- yilda amerikalik kustomerlaga hzmat korsatgan amerikalik suplayerlar korsatilsin
# 6-savol 5- kategopriyadagi maxsulotlarga 97- yilda xizmat korsatgan xozimlar
# 7-amerigalik har bir shaxri 97- yilning har bir oyida qanchadan zakas olgan


1- masala
select to_char(o.order_date,'YYYY-MM') as oy, count(distinct o.order_id) as zakas_soni
from orders o
join order_details od on o.order_id = od.order_id
join products p on od.product_id = p.product_id
where p.category_id = 1 and p.unit_price > 10 and to_char(o.order_date,'YYYY') = '1996'
group by to_char(o.order_date,'YYYY-MM')
order by oy;

2-masala
select distinct s.company_name from suppliers s
join products p on s.supplier_id = p.supplier_id
join order_details od on p.product_id = od.product_id
join orders o on od.order_id = o.order_id
where p.category_id = 3 and p.unit_price = (select min(unit_price)from productswhere category_id = 3)
and to_char(o.order_date,'YYYY-MM') = '1997-07';

3-masala
select distinct e.first_name, e.last_name
from employees e
join orders o on e.employee_id = o.employee_id
where to_char(o.order_date,'YYYY-MM') = '1998-03';



4-masala
select product_name,category_id,od.unit_price,count(o.order_id) from products p
join order_details od on p.product_id=od.product_id
join orders o on od.order_id=o.order_id
where p.unit_price=(select max(unit_price) from products) and to_char(order_date,'YYYY')='1996'
group by p.product_name,p.category_id,od.unit_price;


5-masala
select distinct s.company_name from suppliers s
join products p on s.supplier_id = p.supplier_id
join order_details od on p.product_id = od.product_id
join orders o on od.order_id = o.order_id
join customers c on o.customer_id = c.customer_id
where s.country = 'USA'and c.country = 'USA'and to_char(o.order_date,'YYYY') = '1997';

6 masala
select distinct e.first_name, e.last_name
from employees e
join orders o on e.employee_id = o.employee_id
join order_details od on o.order_id = od.order_id
join products p on od.product_id = p.product_id
where p.category_id = 5 and to_char(o.order_date,'YYYY') = '1997';


-- 7-masala
select  c.city,to_char(o.order_date,'YYYY-MM') as oy,count(*) as zakas_soni
from orders o
join customers c on o.customer_id = c.customer_id
where c.country = 'USA'and to_char(o.order_date,'YYYY') = '1997'
group by c.city, to_char(o.order_date,'YYYY-MM')
order by c.city, oy;

