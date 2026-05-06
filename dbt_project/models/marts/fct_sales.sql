select
    o.order_id,
    o.order_date,
    c.customer_id,
    c.customer_name,
    sum(oi.line_total) as total_amount,
    count(distinct oi.product_id) as unique_products
from {{ ref('stg_orders') }} o
join {{ ref('dim_customers') }} c on o.user_id = c.customer_id
join {{ ref('int_order_items') }} oi on o.order_id = oi.order_id
group by 1, 2, 3, 4