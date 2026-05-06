select
    order_id,
    product_id,
    quantity,
    price,
    quantity * price as line_total
from (values
    (1, 101, 2, 50.0),
    (1, 102, 1, 50.0),
    (2, 101, 3, 60.0),
    (3, 103, 1, 100.0)
) as t(order_id, product_id, quantity, price)