from utils import convert_date, checking_empty_field


PRICE_FORMAT = (
    ('name', str),
    ('categories', str),
    ('price', float),
    ('price_ext_id', str),
    ('vat', float),
    ('unit_type', int),
    ('unit_ratio', float)
)
INVENTORY_FORMAT = (
    ('store_ext_id', str),
    ('price_ext_id', str),
    ('snapshot_datetime', convert_date),
    ('in_matrix', bool),
    ('qty', float),
    ('sell_price', float),
    ('prime_cost', float),
    ('min_stock_level', float),
    ('stock_in_days', checking_empty_field),
    ('in_transit', checking_empty_field)
)
