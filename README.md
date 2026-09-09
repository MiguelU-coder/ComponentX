# ComponentX

Proyecto de estructuras de datos II.
Un sistema que maneja clientes, productos, usuarios, pedidos y tiendas sin base de datos:
todo se guarda en archivos txt y las operaciones CRUD se hacen mediante python.

En esta etapa aplicamos dos formas de acceso a archivos que vimos en clase y investigando aparte:

- **Acceso secuencial**: se lee el archivo línea por línea de principio a fin.
- **Acceso directo**: los registros tienen un tamaño fijo, entonces con `seek()` se va
  directamente a la posición del registro que se necesita.

## Qué se puede hacer

El menú principal tiene 7 opciones:

1. **Clients** – CRUD de clientes
2. **Products** – CRUD de productos
3. **Users** – CRUD de usuarios
4. **Orders** – CRUD de pedidos
5. **Shops** – CRUD de tiendas
6. **Sort** – ordena la entidad que elijas por el campo que quieras
7. `0` – salir

Cada entidad tiene su CRUD completo: crear, leer, actualizar y eliminar.
Los datos se validan entre entidades (por ejemplo, un producto no se puede crear si
la tienda a la que pertenece no existe, y una tienda necesita un usuario administrador).

## Cómo se guarda la información

Decidimos separar las entidades en dos grupos según el tipo de acceso:

| Entidad | Acceso | Archivo | Formato del registro |
|---|---|---|---|
| Clients | Directo | `Clients_direct.txt` | 60 bytes fijos |
| Users | Directo | `Users_direct.txt` | 75 bytes fijos |
| Shops | Directo | `Shops_direct.txt` | 90 bytes fijos |
| Products | Secuencial | `Products.txt` | texto separado por comas |
| Orders | Secuencial | `Orders.txt` | texto separado por comas |

### Registros de longitud (acceso directo)

En los archivos directos cada registro ocupa siempre el mismo tamaño y empieza con el estado:
- `1` → registro activo
- `0` → registro eliminado (se "borra", no se quita del archivo)

Por ejemplo, un cliente ocupa 60 bytes: `1` (estado) + 4 (id) + 30 (nombre) + 20 (mail)
+ 4 (tienda) + 1 (salto de línea). Como todos los registros miden lo mismo, se calcula
la posición del registro `n` con `(n - 1) * longitud`.

Los archivos solo se crean cuando se ejecuta la primera acción de CRUD.

### Archivos secuenciales

Los productos y pedidos guardan cada registro como una línea con campos separados por
coma. El primer campo también es la bandera `0/1` (activo/eliminado).

## Ordenamiento (opción 6)

El menú de `Sort` deja elegir la entidad y el campo por el que se quiere ordenar, y
según la entidad usa un algoritmo diferente:

- **Merge sort directo** (`sorting/direct_sorting.py`) para Clients, Users y Shops.
  Lee los registros activos del archivo, los ordena con merge sort y escribe
  el resultado en un archivo `*_sorted.txt`.
- **Ordenamiento externo** (`sorting/external_sorting.py`) para Products y Orders.
  Busca el registro, lo copia al archivo ordenado, y lo marca  Repite hasta terminar.

## Cómo correrlo

Solo necesita Python 3 (no usa ninguna librería externa):

```bash
python main.py
```

Los archivos de datos se leen y escriben en la misma carpeta donde se ejecuta el
programa.

## Estructura del proyecto

```
ComponentX/
├── main.py                  # menús y punto de entrada
├── direct/                  # CRUD con acceso directo
│   ├── clients.py
│   ├── users.py
│   └── shops.py
├── sequential/              # CRUD con acceso secuencial
│   ├── products.py
│   └── orders.py
└── sorting/                 # algoritmos de ordenamiento
    ├── direct_sorting.py    # merge sort sobre archivos directos
    └── external_sorting.py  # ordenamiento externo secuencial
```
## Posibles mejoras

- Validar y ordenar correctamente por valores `float`.
- Separar cada entidad en su propio directorio de datos.
- Reusar el código de los CRUD para no repetir la misma lógica en cada módulo.
```