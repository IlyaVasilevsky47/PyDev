from validation import Boolean, Decimal, Smallint, Text, Timestamp, Varchar

# Format table:
PRICE_FORMAT = {
    'name': Varchar(200),
    'categories': Text(null=True),
    'price': Decimal(10, 4, null=True),
    'price_ext_id': Varchar(40, null=True),
    'vat': Decimal(4, 2, null=True),
    'unit_type': Smallint(null=True),
    'unit_ratio': Decimal(10, 4, null=True),
}
INVENTORY_FORMAT = {
    'store_ext_id': Varchar(40),
    'price_ext_id': Varchar(40),
    'snapshot_datetime': Timestamp(),
    'in_matrix': Boolean(null=True),
    'qty': Decimal(13, 4),
    'sell_price': Decimal(12, 4, null=True),
    'prime_cost': Decimal(12, 4, null=True),
    'min_stock_level': Decimal(13, 4, null=True),
    'stock_in_days': Smallint(null=True),
    'in_transit': Decimal(13, 4, null=True),
}
