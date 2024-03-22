CREATE TYPE unit_type_enum AS ENUM ( 
    'штуки', 'литры', 'миллилитры', 'декалитры', 'граммы', 'метры', 'квадратные метры ', 'кубические метры',
    'миллиметры', 'сантиметры', 'дециметры','гектары', 'тонны', 'галлоны', 'пинты', 'фунты', 'унции', 'километры',
    'квадратные километры', 'килограммы'
);
CREATE TABLE price (
    name VARCHAR(200),
    categories TEXT,
    price DECIMAL(10, 4),
    price_ext_id VARCHAR(40),
    vat DECIMAL(4, 2),
    unit_type unit_type_enum,
    unit_ratio DECIMAL(10, 4)
);
CREATE TABLE inventory (
    store_ext_id VARCHAR(40),
    price_ext_id VARCHAR(40),
    snapshot_datetime TIMESTAMP WITH TIME ZONE,
    in_matrix BOOLEAN,
    qty DECIMAL(13, 4),
    sell_price DECIMAL(12, 4),
    prime_cost DECIMAL(12, 4),
    min_stock_level DECIMAL(13, 4),
    stock_in_days SMALLINT,
    in_transit DECIMAL(13, 4)
);