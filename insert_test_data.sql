--

INSERT INTO product_types VALUES
  (1, "Компьютеры", 12132, "Компьютеры, планшеты, ноутбуки..."),
  (2, "Электроника", 19911, "Телевизоры, фото и видеокамеры, сотовые телефоны,..."),
  (3, "Бытовая техника", 14121, "Холодильники, стиральные машины, микроволновки,..."),
  (4, "Детские товары", 6121, ""),
  (5, "Зоотовары", 5234, ""),
  (6, "Дом, дача, ремонт", 6234, ""),
  (7, "Одежда и обувь", 9342, "Обувь, верхняя одежда, спортивная одежда..."),
  (8, "Красота и здоровье", 2324, ""),
  (9, "Авто", 4232, "Новые и подержанные автомобили"),
  (10, "Досуг и развлечения", 2322, ""),
  (11, "Спорт и отдых", 456, "");

INSERT INTO computer_product_types VALUES
  (1, "Ноутбуки", 1211, ""),
  (2, "Планшеты", 777, ""),
  (3, "Персональные компьютеры", 543, ""),
  (4, "Сетевое оборудование", 343, "");

insert into desktops values  -- computer_product_types: 3
  (1, "IBM 280", 3281.55, 4.8, "", '{"cpu_number": 4, "graphics_card": "AMD Radeon 530", "hard_drive_type": "HDD", "weight": 3.221, "screen_resolution": 17.5, "cpu_model": "Core i5", "frequency": 2000, "hard_drive_size": "1500Gb"}'),
  (2, "Toshiba 341", 2381.12, 3.2, "", '{"cpu_number": 2, "graphics_card": "AMD Radeon 500", "hard_drive_type": "HDD", "weight": 3.221, "screen_resolution": 17.5, "cpu_model": "Core i7", "frequency": 2200, "hard_drive_size": "500Gb"}'),
  (3, "Zx12 RT", 1111.12, 1.8, "", '{"cpu_number": 4, "graphics_card": "AMD Radeon 530", "hard_drive_type": "HDD", "weight": 3.221, "screen_resolution": 17.5, "cpu_model": "Core i5", "frequency": 1400, "hard_drive_size": "2500Gb"}');

INSERT INTO laptops VALUES -- computer_product_types: 1
  (1, "Samsung 01", 2222.12, 4.2, "", '{"cpu_number": 4, "graphics_card": "AMD Radeon 530", "hard_drive_type": "HDD", "weight": 3.221, "screen_resolution": 17.5, "cpu_model": "Core i5", "frequency": 2000, "hard_drive_size": "800Gb"}'),
  (2, "Samsung 02", 3333.12, 3.2, "", '{"cpu_number": 4, "graphics_card": "AMD Radeon 530", "hard_drive_type": "HDD", "weight": 3.221, "screen_resolution": 17.5, "cpu_model": "Core i5", "frequency": 2200, "hard_drive_size": "3500Gb"}'),
  (3, "RedRaptorX", 4444.12, 1.8, "", '{"cpu_number": 4, "graphics_card": "AMD Radeon 530", "hard_drive_type": "HDD", "weight": 3.221, "screen_resolution": 17.5, "cpu_model": "Core i5", "frequency": 1000, "hard_drive_size": "1500Gb"}');

INSERT INTO shops VALUES
  (1, "Eldorado", "Moscow Golovlev Street 28", 4.2),
  (2, "Electro-shop", "Moscow Tverskaja Street 18", 3.25),
  (3, "Pleer.ru", "Moscow Levoberejnaja naberezhnaja 1", 3.77);

INSERT INTO sale_variants VALUES
  (1, 1, 3, 1, 1, 19000.00, 100),
  (2, 1, 3, 1, 2, 19500.00, 2),
  (3, 1, 3, 1, 3, 22500.00, 23),
  (4, 1, 3, 2, 1, 23300.00, 10),
  (5, 1, 3, 2, 3, 21500.00, 10),
  (6, 1, 3, 3, 1, 17300.00, 1),
  (7, 1, 3, 3, 2, 17300.00, 23),
  (8, 1, 3, 3, 3, 17700.00, 2);

