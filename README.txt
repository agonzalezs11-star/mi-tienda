NOVA COMERCIAL - SISTEMA DJANGO

REQUISITOS: Python 3.10 o superior.

INSTALACIÓN EN WINDOWS:
1. Extrae el ZIP.
2. Abre la carpeta comercial_nova en VS Code.
3. Abre Terminal > New Terminal.
4. Ejecuta:
   py -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   py manage.py makemigrations
   py manage.py migrate
   py manage.py createsuperuser
   py manage.py runserver
5. Abre http://127.0.0.1:8000/
6. Inicia sesión con el usuario que creaste.

GESTIÓN:
- El panel permite CRUD de clientes, proveedores, marcas, categorías, productos,
  compras y ventas.
- Para agregar productos a cada compra o venta, entra en Administración:
  http://127.0.0.1:8000/admin/
  Abre Compras o Ventas y agrega los detalles en la sección inferior.

IMPORTANTE:
- Este proyecto crea una base de datos nueva db.sqlite3; no modifica tu archivo original.
- Esta es una base funcional inicial para practicar. Los totales y movimientos de stock
  deben completarse en una siguiente etapa antes de usarlo en un negocio real.
