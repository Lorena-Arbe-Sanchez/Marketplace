# Proyecto Web SGE - Egibide Community Market

## 📋 Información del Proyecto
* **Asignatura:** Sistemas de Gestión Empresarial (SGE)
* **Curso:** 2025/2026
* **Fecha de Entrega:** 28/05/2026
* **Grupo:** Grupo 5
* **Integrantes:**
    * [Lorena Arbé Sánchez](https://github.com/Lorena-Arbe-Sanchez)
    * [Aitor Amaury Farinango Rojas](https://github.com/AitorAmaury)

---

## 🚀 Objetivo General
Desarrollo de una aplicación web funcional utilizando el framework **Django**. El proyecto consiste en la creación de un Marketplace interno que fomenta la reutilización y la compraventa de productos entre miembros de una comunidad o empresa, aplicando conceptos de modelado de datos, lógica de negocio, persistencia y usabilidad.

## 🎯 Reto Seleccionado: Reto 6 - Marketplace Interno
La empresa **Egibide Community Market S.L.** requiere una plataforma donde los usuarios puedan:
1. Publicar artículos para su venta o reutilización.
2. Gestionar solicitudes de interés por parte de otros usuarios.
3. Controlar el ciclo de vida de un producto (Disponible, Reservado, Vendido).

### 🏗️ Modelo de Datos
El sistema se basa en las siguientes entidades principales:
* **Producto:** Información del artículo, precio, estado y propietario.
* **Usuario:** Datos de contacto y perfil de los participantes.
* **Solicitud:** Conecta a un usuario interesado con un producto específico.
* **Categoría:** Clasificación jerárquica de los productos.

---

## ✨ Funcionalidades Implementadas

### Gestión de Contenido (CRUD)
- [ ] **Gestión de Productos:** Alta, listado tipo tarjetas (cards), vista detalle, edición y eliminación.
- [ ] **Gestión de Usuarios:** Registro y mantenimiento de perfiles.
- [ ] **Gestión de Solicitudes:** Sistema para que los usuarios interesados contacten con los propietarios.

### Lógica de Negocio
- [ ] **Estados del Producto:** Transiciones entre Disponible, Reservado y Vendido.
- [ ] **Filtros Avanzados:** Búsqueda por categoría, estado y usuario propietario.
- [ ] **Historial:** Seguimiento de solicitudes recibidas por cada producto.
- [ ] **Valoraciones:** Sistema de feedback entre usuarios.

### Interfaz y Experiencia (UX/UI)
- [ ] Diseño responsive adaptado a diferentes dispositivos.
- [ ] Uso de CSS y JavaScript para mejorar la interactividad.
- [ ] Galería de productos visual y navegación intuitiva.

---

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.x, Django Framework.
* **Frontend:** HTML5, CSS3, JavaScript.
* **Base de Datos:** SQLite (desarrollo).
* **Control de Versiones:** GitHub.

---

## ⚙️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Lorena-Arbe-Sanchez/Marketplace.git
    ```

2.  **Crear y activar entorno virtual:**
    ```bash
    python -m venv venv

    # En Windows:
    .\venv\Scripts\activate

    # En Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install django
    ```

4.  **Ejecutar migraciones (preparar base de datos):**
    ```bash
    python manage.py migrate
    ```

5.  **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

---

## 📂 Documentación Adicional
* **Repositorio GitHub:** [Enlace directo al repositorio](https://github.com/Lorena-Arbe-Sanchez/Marketplace.git)
* **Esquema de BD:** El archivo con la imagen del esquema se encuentra en la raíz del proyecto.
* **Planificación:** El seguimiento de tareas detallado se encuentra en el archivo "Organizacion_Trabajo.xlsx".
* **Datos mínimos:** La base de datos incluye al menos 8 registros por cada entidad principal para la demo.

---

## ⚠️ Incidencias y Estado del Proyecto
* **Funcionalidades no operativas:** Ninguna / [Listar si alguna no funciona]
* **Incidencias conocidas:** [Describir brevemente errores menores si los hay]

---

## 👨‍💻 Organización del Equipo
El trabajo se ha desarrollado de forma colaborativa siguiendo la metodología de trabajo en Git. Cada integrante ha realizado un mínimo de 3 commits significativos. El reparto de tareas específico y la evolución cronológica pueden consultarse en el documento Excel adjunto en la entrega.