Nombre del proyecto
Gestión de Procesos Productivos Industriales con PySide6 y PostgreSQL

Descripción

Esta aplicación de escritorio está diseñada para gestionar los procesos productivos de los productos fabricados en una empresa industrial. Permite almacenar y organizar productos, sus familias y sus atributos, así como definir procesos de fabricación con sus operaciones, máquinas, tiempos y secuencias, favoreciendo la planificación previa a la producción.

El sistema soporta relaciones jerárquicas entre productos, permitiendo representar conjuntos ensamblados, y gestiona dos tipos de procesos: estándar (aplicables a rangos de atributos para varios productos) y propios (específicos de un producto). También mantiene revisiones históricas de los procesos para permitir control y mejora continua.

Tecnologías usadas

Python 3.x para la lógica y backend.

PySide6 para la interfaz gráfica de escritorio basada en Qt.

PostgreSQL como base de datos relacional, con un esquema diseñado para reflejar jerarquías y atributos complejos.

Modelo de arquitectura Clean Architecture + DDD para un código modular, mantenible y escalable.

Funcionalidades principales

Gestión de familias de productos con sus atributos (tipos, unidades, obligatoriedad).

Creación y organización de productos, con soporte para jerarquías de subproductos.

Definición y revisión de procesos productivos, con operaciones específicas, maquinaria, secuencias y tiempos.

Dashboard con estadísticas y visualización tipo Kanban.

Control de acceso con roles y permisos para limitar edición según usuario.

Funcionalidad avanzada para búsqueda de productos por atributos con ajuste de similitud.

Capacidad para clonar productos o procesos como base para nuevos ítems.

Posible integración futura con IA para recomendar procesos de fabricación basados en similitudes y datos históricos.

Instalación y uso
Clonar este repositorio.

Crear una base de datos PostgreSQL usando el script schema.sql.

Instalar dependencias con pip install -r requirements.txt (incluyendo PySide6 y psycopg2).

Ejecutar la aplicación con python main.py.

Contribuciones
Se aceptan contribuciones para ampliar funcionalidades, mejorar la interfaz, integrar módulos IA o adaptar a nuevos entornos productivos.

Este proyecto es ideal para empresas industriales que buscan planificar y estandarizar sus procesos productivos con soporte tecnológico moderno y flexible.