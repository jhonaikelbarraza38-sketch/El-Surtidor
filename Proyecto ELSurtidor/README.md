# Sistema de Gestión El Surtidor

Sistema de escritorio para la gestión de inventario y ventas de la Distribuidora ElSurtidor, un negocio familiar de distribución de productos de consumo masivo que abastece tiendas y supermercados de barrio.

---

## Descripción

El sistema permite registrar y gestionar productos, proveedores, clientes, pedidos de venta e inventario, reemplazando el registro manual en cuadernos y archivos sueltos por una solución digital centralizada. Incluye validaciones de negocio, control de stock automático y reportes de ventas.

---

## Módulos del Sistema

| Módulo | Descripción |
|--------|-------------|
| Acceso al Sistema | Login con validación de usuario y contraseña |
| Gestión de Usuarios | Administrar cuentas de acceso al sistema |
| Gestión de Productos | CRUD de productos con categoría, proveedor y unidad de medida |
| Gestión de Categorías | CRUD de categorías de productos |
| Gestión de Proveedores | CRUD de proveedores con información de contacto |
| Gestión de Clientes | CRUD de clientes con nombre, dirección y teléfono |
| Pedidos y Ventas | Registro de pedidos con múltiples productos y control de stock |
| Inventario | Consulta de stock actual y registro de entradas de mercancía |
| Consultas y Reportes | Reportes de ventas por cliente, por producto y stock bajo mínimo |

---

## Herramientas Utilizadas

- **Python 3.13**
- **Tkinter** — Interfaz gráfica de escritorio
- **MySQL 8.0** — Base de datos relacional
- **mysql-connector-python** — Conector de base de datos

---

## Arquitectura

El proyecto implementa el patrón **MVC (Modelo - Vista - Controlador)** usando exclusivamente funciones, sin clases ni decoradores.

```
sistema-gestion-elsurtidor/
│
├── main.py                  # Punto de entrada
├── elsurtidor.sql           # Script SQL completo
├── README.md
│
├── config/
│   └── db.py                # Conexión a la base de datos
│
├── models/
│   ├── usuario_model.py
│   ├── categoria_model.py
│   ├── proveedor_model.py
│   ├── cliente_model.py
│   ├── producto_model.py
│   ├── unidad_medida_model.py
│   ├── pedido_model.py
│   ├── detalle_pedido_model.py
│   └── reporte_model.py
│
├── controllers/
│   ├── usuario_controller.py
│   ├── categoria_controller.py
│   ├── proveedor_controller.py
│   ├── cliente_controller.py
│   ├── producto_controller.py
│   ├── unidad_medida_controller.py
│   ├── pedido_controller.py
│   └── reporte_controller.py
│
└── views/
    ├── login_view.py
    ├── menu_view.py
    ├── usuario_view.py
    ├── categoria_view.py
    ├── proveedor_view.py
    ├── cliente_view.py
    ├── producto_view.py
    ├── unidad_medida_view.py
    ├── pedido_view.py
    ├── inventario_view.py
    └── reporte_view.py
```

---

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/jhonaikelbarraza38-sketch/sistema-gestion-elsurtidor.git
```

### 2. Instalar dependencias
```bash
pip install mysql-connector-python
```

### 3. Configurar la base de datos
- Crear la base de datos ejecutando el archivo `elsurtidor.sql` en MySQL Workbench
- Editar el archivo `config/db.py` con tus credenciales de MySQL:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="elsurtidor"
)
```

### 4. Ejecutar el sistema
```bash
python main.py
```

### 5. Credenciales de acceso
```
Usuario: jhonaikel
Contraseña: 1028
```

---

## Reglas de Negocio

- No se puede registrar un pedido si algún producto no tiene stock suficiente
- Al cancelar un pedido despachado no se restaura el inventario
- El precio de venta debe ser mayor al precio de compra
- Un producto solo puede pertenecer a una categoría
- No se puede eliminar un proveedor con productos activos asociados

---

## Autor

**Jhonaikel Barraza Noguera**  
Tecnología en Desarrollo de Software  
2026
