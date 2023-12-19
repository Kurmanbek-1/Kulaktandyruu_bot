CREATE_TABLE_ADVERTISING = """
    CREATE TABLE IF NOT EXISTS all_advertising
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    tariff VARCHAR(255),
    photo_check TEXT,
    user_id VARCHAR(255),
    user_name VARCHAR(255) NULL,
    info VARCHAR(255),
    info_photo TEXT NULL,
    social_network VARCHAR(255)
    )
"""

INSERT_INTO_TABLE_ADVERTISING = """
    INSERT INTO all_advertising(tariff, photo_check, user_name, user_id, info, info_photo, social_network) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""


SELECT_CHECKS_ALL = """
    SELECT * FROM all_advertising
"""