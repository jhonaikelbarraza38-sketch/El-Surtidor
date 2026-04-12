create database if not exists elsurtidor 
CHARACTER SET utf8mb4
COLLATE utf8mb4_spanish_ci;
#Imagina que buscas un cliente llamado "josé" pero en la base de datos está guardado como "José". Con utf8mb4_spanish_ci MySQL los trata como iguales y lo encuentra. Sin esto, no lo encontraría porque distinguiría mayúsculas de minúsculas.

use elsurtidor;

create table usuario (
id_usuario int not null auto_increment primary key,
username varchar(50) not null unique,
password varchar(255) not null
);

create table categoria (
id_categoria int not null auto_increment primary key,
nombre varchar(100) not null unique
);

create table proveedor (
id_proveedor int not null auto_increment primary key,
nombre varchar(100) not null,
telefono varchar(20),
direccion varchar(255),
email varchar(100) unique 
);

create table unidad_medida (
id_unidad_medida int auto_increment primary key,
nombre varchar(50) not null unique
);

create table cliente (
id_cliente int not null auto_increment primary key,
nombre varchar(100) not null,
telefono varchar(20),
direccion varchar(255),
email varchar(100) unique 
);

create table producto (
id_producto int not null auto_increment primary key,
nombre varchar(100) not null,
descripcion text,
precio_compra decimal(10,2) not null,
precio_venta decimal(10,2) not null,
stock int not null default 0,
stock_minimo int not null default 0,
id_categoria int not null,
id_proveedor int not null,
id_unidad_medida int not null,

constraint fk_producto_categoria
foreign key (id_categoria) references categoria(id_categoria)
on update cascade 
on delete restrict,

constraint fk_producto_proveedor
foreign key (id_proveedor) references proveedor(id_proveedor)
on update cascade 
on delete restrict,

constraint fk_producto_unidad_medida
foreign key (id_unidad_medida) references unidad_medida(id_unidad_medida)
on update cascade
on delete restrict,

index (id_categoria),
index (id_proveedor),
index (id_unidad_medida)
);

create table pedido (
id_pedido int not null auto_increment primary key,
fecha datetime not null default current_timestamp, 
estado enum('pendiente', 'despachado', 'cancelado') not null default 'pendiente',
id_cliente int not null,
constraint fk_pedido_cliente
foreign key (id_cliente) references cliente (id_cliente)
on update cascade 
on delete restrict,

index (id_cliente)

);


create table detalle_pedido (
id_detalle_pedido int not null auto_increment primary key,
id_pedido int not null,
id_producto int not null,
cantidad int not null,
precio_unitario decimal(10,2) not null,
subtotal decimal(10,2) not null,
constraint fk_detalle_pedido_pedido
foreign key (id_pedido) references pedido (id_pedido)
on update cascade 
on delete cascade,

constraint fk_detalle_pedido_producto
foreign key (id_producto) references producto (id_producto)
on update cascade 
on delete restrict,

index (id_pedido),
index (id_producto)
);

#constraint:
#No puedes crear un producto si no existe categoria o proveedor
#Y como detalle_pedido depende de producto, indirectamente tampoco

#on update cascade actualiza en cascada
#on delete restrict

#RESTRICT →  No borres si está en uso (datos asociados)
#CASCADE →  Si borras, borra todo lo que depende

#CASCADE → limpia detalles automáticamente
# pedido → detalle_pedido

#index acelera las busquedas en los join 
#default current_timestamp (pone fecha y hora actual)

#con la tabla unidad medida manejamos (kg listros (especificaciones de los productos))


-- ============================================================
-- USUARIOS
-- ============================================================
INSERT INTO usuario (username, password) VALUES
('jhonaikel', '1028');


-- ============================================================
-- CATEGORÍAS 
-- ============================================================
INSERT INTO categoria (nombre) VALUES
('Arroces'),('Bebidas'),('Snacks'),('Aseo'),('Granos'),
('Lácteos'),('Enlatados'),('Carnes'),('Panadería'),('Congelados'),
('Bebidas alcohólicas'),('Limpieza'),('Mascotas'),('Dulces'),
('Cereales'),('Salsas'),('Huevos'),
('Aceites y grasas'),('Condimentos'),('Pastas'),
('Jabones'),('Papel y desechables'),('Bebidas calientes'),
('Endulzantes'),('Conservas');

-- ============================================================
-- PROVEEDORES (
-- ============================================================
INSERT INTO proveedor (nombre, telefono, direccion, email) VALUES
('Alpina','3001234567','Zona Industrial Calle 13 #45-20, Bogotá','contacto@alpina.com'),
('Postobón','3009876543','Av. Industrial #10-50, Medellín','ventas@postobon.com'),
('Diana Corporación','3014567890','Calle 80 #22-10, Bogotá','info@diana.com'),
('Grupo Nutresa','3021112233','Carrera 43A #7-50, Medellín','contacto@nutresa.com'),
('Colanta','3032223344','Zona Rural Km 2 vía Guarne, Antioquia','info@colanta.com'),
('Quala','3045556677','Calle 26 #68-42, Bogotá','info@quala.com'),
('Bavaria','3051112233','Av. Boyacá #64-45, Bogotá','info@bavaria.com'),
('Colombina','3062223344','Zona Industrial Yumbo, Valle','contacto@colombina.com'),
('Zenú','3073334455','Calle 30 #55-10, Medellín','ventas@zenu.com'),
('Bimbo','3084445566','Autopista Norte #230-40, Bogotá','info@bimbo.com'),
('Nestlé Colombia','3095556677','Km 3 vía Siberia, Bogotá','contacto@nestle.com'),
('D1 Proveedores','3106667788','Zona Logística Calle 80, Bogotá','proveedores@d1.com'),
('Ara Proveedores','3117778899','Calle 13 #50-20, Bogotá','info@ara.com'),
('La Vaquita','3128889900','Carrera 65 #45-12, Medellín','contacto@lavaquita.com'),
('Ramo','3139990011','Calle 17 #68-20, Bogotá','info@ramo.com'),
('Team Foods','3140001122','Zona Industrial Calle 13 #90-10, Bogotá','contacto@teamfoods.com'),
('Pastas Doria','3151112233','Calle 13 #45-10, Bogotá','info@doria.com'),
('Goya Foods','3162223344','Zona Industrial Calle 80, Bogotá','info@goya.com'),
('Condimentos El Rey','3173334455','Carrera 30 #20-10, Medellín','info@elrey.com'),
('Familia','3184445566','Calle 10 #30-20, Medellín','info@familia.com');
-- NOTA: team foods y goyaa foods  no tiene productos → se puede eliminar para probar

-- ============================================================
-- UNIDADES DE MEDIDA
-- ============================================================
INSERT INTO unidad_medida (nombre) VALUES
('unidad'),('kg'),('litro'),('paquete'),('caja'),
('docena'),('gramos'),('mililitros'),('bolsa'),('tarro'),
('lata'),('botella'),('canasta'),('saco'),('bulto');

-- ============================================================
-- CLIENTES 
-- ============================================================
INSERT INTO cliente (nombre, telefono, direccion, email) VALUES
('Tienda La Esquina','3201234567','Calle 30 #12-45, Barrio Las Nieves, Barranquilla','tienda1@gmail.com'),
('Supermercado El Ahorro','3219876543','Carrera 45 #20-10, Barrio Boston, Barranquilla','ahorro@gmail.com'),
('Minimarket Don José','3224567890','Calle 58 #14-33, Barrio Las Nieves, Soledad','donjose@gmail.com'),
('Tienda El Progreso','3231112233','Carrera 10 #5-22, Barrio Centro, Malambo','progreso@gmail.com'),
('Autoservicio Central','3242223344','Calle 72 #30-15, Barrio El Prado, Barranquilla','central@gmail.com'),
('Tienda El Sol','3251112233','Carrera 21 #18-40, Barrio Las Nieves, Barranquilla','elsol@gmail.com'),
('MiniMarket Express','3262223344','Calle 84 #9-12, Barrio Villa Santos, Soledad','express@gmail.com'),
('Super Tienda Norte','3273334455','Carrera 53 #25-60, Barrio Norte, Barranquilla','norte@gmail.com'),
('Tienda Familiar','3284445566','Calle 33 #11-08, Barrio Las Nieves, Malambo','familiar@gmail.com'),
('Autoservicio La 14','3295556677','Carrera 38 #40-22, Barrio Recreo, Barranquilla','la14@gmail.com'),
('Tienda Central','3306667788','Calle 50 #22-18, Barrio Centro, Soledad','central2@gmail.com'),
('MiniMarket Plus','3317778899','Carrera 15 #8-30, Barrio Las Nieves, Barranquilla','plus@gmail.com'),
('Tienda Caribe','3328889900','Calle 100 #45-10, Barrio Puerto Colombia Centro','caribe@gmail.com'),
('Supermercado Popular','3339990011','Carrera 60 #33-21, Barrio Boston, Barranquilla','popular@gmail.com'),
('Tienda Rápida','3340001122','Calle 25 #17-09, Barrio Las Nieves, Soledad','rapida@gmail.com'),
-- Clientes nuevos con múltiples pedidos
('Minimarket La 45','3351112233','Carrera 45 #30-10, Barrio El Carmen, Barranquilla','la45@gmail.com'),
('Tienda Don Pedro','3362223344','Calle 17 #8-20, Barrio Las Flores, Soledad','donpedro@gmail.com'),
('Supermercado Familiar','3373334455','Carrera 38 #15-30, Barrio Boston, Barranquilla','superfamiliar@gmail.com'),
('Minimarket La Mejor','3384445566','Calle 45 #20-10, Barrio El Prado, Barranquilla','lamejor@gmail.com'),
('Tienda El Vecino','3395556677','Carrera 21 #10-15, Barrio Las Nieves, Malambo','elvecino@gmail.com'),
-- Clientes SIN pedidos → se pueden eliminar para probar
('Tienda Nueva','3400001111','Calle 5 #10-20, Barrio Centro, Barranquilla','nueva@gmail.com'),
('Minimarket Recién','3400002222','Carrera 10 #5-10, Barrio Las Nieves, Soledad','recien@gmail.com'),
('Autoservicio Moderno','3400003333','Calle 20 #15-30, Barrio Boston, Barranquilla','moderno@gmail.com'),
('Tienda El Futuro','3400004444','Carrera 30 #25-40, Barrio El Prado, Barranquilla','futuro@gmail.com'),
('Supermercado Express','3400005555','Calle 50 #30-20, Barrio Norte, Barranquilla','express2@gmail.com');

-- ============================================================
-- PRODUCTOS (72 productos)
-- ============================================================
INSERT INTO producto
(nombre, descripcion, precio_compra, precio_venta, stock, stock_minimo, id_categoria, id_proveedor, id_unidad_medida)
VALUES
-- ORIGINALES
('Arroz Diana','Arroz blanco de grano largo, ideal para cocción rápida',3000,3800,100,20,1,3,2),
('Arroz Roa','Arroz premium de grano extra largo, textura suave',3200,4000,90,20,1,3,2),
('Coca Cola','Gaseosa sabor cola, presentación familiar',4000,5000,80,15,2,2,12),
('Pepsi','Gaseosa sabor cola, refrescante y burbujeante',3800,4800,70,15,2,2,12),
('Papas Margarita','Papas fritas onduladas, sabor original crujiente',1500,2200,60,10,3,4,4),
('Chocoramo','Ponqué cubierto de chocolate, snack clásico colombiano',1800,2500,75,15,9,15,1),
('Leche Colanta','Leche entera pasteurizada, alto contenido de calcio',2800,3500,70,15,6,5,3),
('Yogurt Alpina','Yogurt semidescremado con cultivos activos, sabor fresa',2000,2800,60,10,6,1,1),
('Lentejas','Lenteja verde seleccionada, libre de impurezas',2500,3200,90,20,5,3,2),
('Frijol','Frijol cargamanto rojo, grano grueso de primera calidad',3000,3800,85,20,5,3,2),
('Atún en lata','Atún en agua con sal, alto contenido de proteína',3500,4500,50,10,7,6,11),
('Detergente','Detergente en polvo multiusos, aroma limón concentrado',5000,6500,40,10,4,6,2),
('Galletas Festival','Galletas dulces rellenas de crema de vainilla',1200,1800,100,20,3,4,4),
('Jugo Hit','Jugo de fruta natural con vitamina C, sabor mango',2500,3200,80,15,2,6,3),
('Aceite','Aceite vegetal 100% girasol, sin colesterol',7000,8500,60,10,18,6,12),
('Azúcar','Azúcar blanca refinada de caña, grano fino',2800,3500,90,20,5,3,2),
('Sal','Sal refinada yodada y fluorizada, uso doméstico',1500,2000,70,15,5,6,2),
('Jabón Rey','Jabón en barra para ropa, fórmula antigrasa',1200,1800,100,20,21,6,1),
('Avena Alpina','Avena en hojuelas integral, rica en fibra y proteína',2200,3000,60,10,6,1,4),
('Sardinas','Sardinas en salsa de tomate, fuente de omega 3',2800,3500,50,10,7,6,11),
('Pan tajado','Pan blanco tajado suave, ideal para sándwiches',3000,3800,40,10,9,10,1),
('Café Sello Rojo','Café molido tostado tradicional, sabor intenso colombiano',8000,10000,30,5,23,4,1),

-- PRODUCTOS CON STOCK BAJO MÍNIMO → para probar reporte de inventario
('Maicena','Almidón de maíz para espesar salsas y sopas',1800,2500,3,15,19,6,2),
('Panela','Panela redonda 100% caña de azúcar colombiana',2000,2800,2,10,5,3,1),
('Chocolate Corona','Chocolate en polvo para preparar bebidas calientes',5500,7000,4,20,23,4,1),
('Crema de leche','Crema de leche entera para cocinar y repostería',3500,4500,1,10,6,1,1),
('Mantequilla','Mantequilla con sal elaborada con leche entera',4000,5200,2,15,6,1,1),
('Aceite de oliva','Aceite de oliva extra virgen importado',12000,15000,3,10,18,6,12),
('Gelatina Royal','Gelatina en polvo sabor fresa y mora',1500,2000,5,20,14,4,4),
('Masmelos','Masmelos de colores para postres y chocolatadas',2000,2800,4,15,14,8,4),

-- PRODUCTOS CON STOCK NORMAL → para contraste
('Pasta Doria','Pasta espagueti de trigo semolado, cocción perfecta',2200,3000,80,20,20,17,2),
('Pasta Fusilli','Pasta tornillo ideal para ensaladas y guisos',2200,3000,75,20,20,17,2),
('Atún Van Camps','Atún en aceite vegetal, sabor suave',3800,4800,60,15,7,6,11),
('Salsa de tomate','Salsa de tomate natural para pastas y carnes',3000,4000,50,15,16,6,12),
('Mayonesa','Mayonesa cremosa con limón, sabor suave',4500,5800,45,15,16,6,12),
('Mostaza','Mostaza amarilla estilo americano',2500,3500,40,10,16,6,12),
('Kétchup','Kétchup de tomate natural sin conservantes',3000,4000,55,15,16,6,12),
('Arroz integral','Arroz integral de grano largo, alto en fibra',3500,4500,70,20,1,3,2),
('Quinua','Quinua blanca orgánica, rica en proteínas',8000,10000,30,10,5,3,2),
('Lentejas rojas','Lentejas rojas peladas de cocción rápida',3000,4000,60,15,5,3,2),
('Garbanzo','Garbanzo blanco seleccionado sin impurezas',3500,4500,55,15,5,3,2),
('Harina de trigo','Harina de trigo todo uso para repostería',2500,3200,80,20,9,10,2),
('Levadura','Levadura seca instantánea para pan casero',1500,2200,40,10,9,10,4),
('Bicarbonato','Bicarbonato de sodio para cocina y repostería',1200,1800,50,10,19,6,2),
('Canela','Canela en rama para bebidas y postres',2000,2800,35,10,19,6,4),
('Pimienta negra','Pimienta negra molida para condimentar',2500,3500,30,10,19,6,4),
('Comino','Comino molido tradicional colombiano',1800,2500,45,10,19,6,4),
('Ajo en polvo','Ajo en polvo deshidratado para condimentar',2200,3000,40,10,19,6,4),
('Caldo de pollo','Caldo de pollo en cubos para sopas y guisos',2000,2800,60,15,19,6,4),
('Toallas de cocina','Toallas de cocina doble hoja absorbente',3500,4500,50,15,22,20,4),
('Papel higiénico','Papel higiénico triple hoja suave',8000,10500,40,15,22,20,4),
('Servilletas','Servilletas de papel doble hoja blancas',2500,3500,55,15,22,20,4),
('Bolsas basura','Bolsas de basura negras resistentes paquete x10',3000,4000,45,10,22,20,4),
('Blanqueador','Blanqueador líquido para ropa blanca y desinfección',3500,4500,35,10,12,6,12),
('Suavizante','Suavizante de ropa aroma lavanda',4000,5200,30,10,12,6,12),
('Limpiapisos','Limpiapisos multiusos aroma pino',3800,5000,40,10,12,6,12),
('Shampoo','Shampoo anticaspa con zinc',8500,11000,25,10,4,6,12),
('Crema dental','Crema dental con flúor protección total',4500,6000,30,10,4,6,1),
('Desodorante','Desodorante roll-on protección 48 horas',6000,8000,20,10,4,6,1),
('Alimento perro','Alimento seco para perros adultos sabor res',18000,23000,15,5,13,11,2),
('Alimento gato','Alimento seco para gatos adultos sabor atún',16000,21000,12,5,13,11,2),
('Cerveza Club Colombia','Cerveza rubia colombiana de malta premium',3500,4500,100,20,11,7,12),
('Cerveza Águila','Cerveza rubia colombiana refrescante',2800,3800,120,25,11,7,12),
('Ron Medellín','Ron añejo colombiano con sabor suave',35000,45000,20,5,11,7,12),
('Aguardiente Antioqueño','Aguardiente sin azúcar típico colombiano',22000,28000,25,5,11,7,12),
('Huevos AA','Huevos frescos de gallina tamaño AA docena',8000,10000,50,15,17,5,6),
('Huevos A','Huevos frescos de gallina tamaño A docena',7000,9000,60,15,17,5,6),
('Leche en polvo','Leche en polvo entera para preparar',12000,15000,30,10,6,5,2),
('Leche de coco','Leche de coco natural para cocinar',5000,6500,25,10,6,5,12),
('Stevia','Stevia en polvo endulzante natural sin calorías',8000,10500,20,10,24,6,4),
('Miel de abeja','Miel de abeja natural 100% pura',12000,16000,15,5,24,6,12),
('Mermelada fresa','Mermelada de fresa sin conservantes',4500,6000,30,10,25,4,12),
('Atún ahumado','Atún ahumado en lata sabor intenso',4500,5800,25,10,25,6,11),
('Maní','Maní tostado y salado snack saludable',2000,2800,50,15,3,4,4),
('Chitos','Snack de maíz sabor queso crujiente',1500,2200,80,20,3,4,4);

-- ============================================================
-- PEDIDOS
-- Cubre todos los estados: pendiente, despachado, cancelado
-- Diferentes fechas para probar reportes por rango
-- Clientes con múltiples pedidos
-- ============================================================
INSERT INTO pedido (fecha, estado, id_cliente) VALUES
-- Enero 2026
('2026-01-05 08:15:22','pendiente',6),
('2026-01-20 12:45:10','despachado',7),
('2026-01-15 10:30:00','despachado',16),
('2026-01-25 14:20:00','cancelado',17),    -- pedido cancelado
('2026-01-28 09:00:00','despachado',18),
-- Febrero 2026
('2026-02-14 16:30:00','pendiente',8),
('2026-02-28 09:10:45','despachado',9),
('2026-02-10 11:00:00','despachado',16),   -- cliente 16 con múltiples pedidos
('2026-02-20 15:30:00','cancelado',19),    -- pedido cancelado
('2026-02-25 08:45:00','despachado',20),
-- Marzo 2026
('2026-03-05 11:25:33','pendiente',10),
('2026-03-18 14:55:12','despachado',11),
('2026-03-25 17:05:50','pendiente',12),
('2026-03-10 10:00:00','despachado',17),   -- cliente 17 con múltiples pedidos
('2026-03-15 13:30:00','cancelado',18),    -- pedido cancelado
('2026-03-20 16:00:00','despachado',16),   -- cliente 16 tercer pedido
-- Abril 2026
('2026-04-02 19:40:20','despachado',13),
(NOW(),'pendiente',14),
(NOW(),'despachado',15),
(NOW(),'pendiente',19),                    -- cliente 19 con múltiples pedidos
(NOW(),'despachado',20);                   -- cliente 20 con múltiples pedidos

-- ============================================================
-- DETALLE PEDIDO
-- Pedidos con múltiples productos
-- Cubre productos de diferentes categorías
-- ============================================================
INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario, subtotal) VALUES
-- Pedido 1 (cliente 6 - pendiente - enero)
(1,1,5,3800,19000),
(1,3,3,5000,15000),
(1,13,4,1800,7200),
-- Pedido 2 (cliente 7 - despachado - enero)
(2,5,4,2200,8800),
(2,7,2,3500,7000),
(2,16,3,3500,10500),
-- Pedido 3 (cliente 16 - despachado - enero)
(3,2,6,4000,24000),
(3,6,3,2500,7500),
(3,31,2,3000,6000),
-- Pedido 4 (cliente 17 - cancelado - enero)
(4,9,5,3200,16000),
(4,11,2,4500,9000),
-- Pedido 5 (cliente 18 - despachado - enero)
(5,15,3,8500,25500),
(5,12,2,6500,13000),
(5,18,4,1800,7200),
-- Pedido 6 (cliente 8 - pendiente - febrero)
(6,1,10,3800,38000),
(6,16,5,3500,17500),
(6,17,8,2000,16000),
-- Pedido 7 (cliente 9 - despachado - febrero)
(7,4,3,4800,14400),
(7,14,4,3200,12800),
(7,3,2,5000,10000),
-- Pedido 8 (cliente 16 - despachado - febrero - segundo pedido)
(8,32,3,3000,9000),
(8,33,2,3000,6000),
(8,34,4,4800,19200),
-- Pedido 9 (cliente 19 - cancelado - febrero)
(9,10,3,3800,11400),
(9,20,2,3500,7000),
-- Pedido 10 (cliente 20 - despachado - febrero)
(10,22,2,10000,20000),
(10,19,3,3000,9000),
(10,8,4,2800,11200),
-- Pedido 11 (cliente 10 - pendiente - marzo)
(11,37,2,4500,9000),
(11,38,3,4000,12000),
(11,39,2,4500,9000),
-- Pedido 12 (cliente 11 - despachado - marzo)
(12,50,2,4500,9000),
(12,51,3,3500,10500),
(12,52,4,2500,10000),
-- Pedido 13 (cliente 12 - pendiente - marzo)
(13,63,5,4500,22500),
(13,64,3,3800,11400),
-- Pedido 14 (cliente 17 - despachado - marzo - segundo pedido)
(14,65,6,9000,54000),
(14,66,4,8000,32000),
(14,40,3,3200,9600),
-- Pedido 15 (cliente 18 - cancelado - marzo)
(15,67,2,45000,90000),
(15,68,3,22000,66000),
-- Pedido 16 (cliente 16 - despachado - marzo - tercer pedido)
(16,1,8,3800,30400),
(16,2,5,4000,20000),
(16,7,6,3500,21000),
-- Pedido 17 (cliente 13 - despachado - abril)
(17,53,3,4500,13500),
(17,54,2,3500,7000),
(17,55,4,3000,12000),
-- Pedido 18 (cliente 14 - pendiente - hoy)
(18,56,2,5200,10400),
(18,57,3,4500,13500),
-- Pedido 19 (cliente 15 - despachado - hoy)
(19,71,4,10000,40000),
(19,72,3,9000,27000),
-- Pedido 20 (cliente 19 - pendiente - hoy)
(20,31,5,3000,15000),
(20,32,3,3000,9000),
(20,14,4,3200,12800),
-- Pedido 21 (cliente 20 - despachado - hoy)
(21,63,3,4500,13500),
(21,64,2,3800,7600),
(21,22,2,10000,20000);