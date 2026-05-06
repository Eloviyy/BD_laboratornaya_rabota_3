select
    id as order_id,
    user_id,
    order_date::date as order_date,
    status,
    amount
from (values
    (1, 1, '2024-01-15'::date, 'completed', 150.0),
    (2, 2, '2024-01-16'::date, 'completed', 200.0),
    (3, 1, '2024-01-17'::date, 'pending', 100.0)
) as t(id, user_id, order_date, status, amount)