# ComponentX

Proyecto de estructuras de datos II.
Un sistema que maneja clientes, productos, usuarios, pedidos y tiendas sin base de datos:
todo se guarda en archivos txt y las operaciones CRUD se hacen mediante python.

En esta etapa aplicamos dos formas de acceso a archivos que vimos en clase y investigando aparte:

- **Acceso secuencial**: se lee el archivo línea por línea de principio a fin.
- **Acceso directo**: los registros tienen un tamaño fijo, entonces con `seek()` se va
  directamente a la posición del registro que se necesita.

## Qué se puede hacer

El menú principal tiene 8 opciones:

1. **Clients** – CRUD de clientes
2. **Products** – CRUD de productos
3. **Users** – CRUD de usuarios
4. **Orders** – CRUD de pedidos y sus árboles binarios (opciones 5 a 10)
5. **Shops** – CRUD de tiendas
6. **Sort** – ordena la entidad que elijas por el campo que quieras
7. **Categories** – árbol de categorías de productos
8. **Roles** – árbol de áreas y roles de los usuarios
9. `0` – salir

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

## Árboles

Un **árbol** guarda datos en forma de jerarquía: hay un elemento arriba de todo y de él
salen los demás, como las carpetas de un computador. Cada elemento se llama **nodo**.

Palabras que se usan en esta sección:

| Palabra | Qué significa |
|---|---|
| **Raíz** | El primer nodo, el de arriba. No tiene padre. |
| **Hijo / padre** | Si de A sale B, B es hijo de A y A es padre de B. |
| **Hoja** | Un nodo que no tiene hijos. |
| **Nivel** | Cuántos pasos hay desde la raíz hasta el nodo. La raíz está en el nivel 0. |
| **Altura** | El nivel de la hoja más profunda. Un árbol de un solo nodo tiene altura 0. |
| **Subárbol** | Un nodo junto con todo lo que cuelga de él. |

Todas las operaciones son **recursivas**: la función hace el trabajo con un nodo y
después se llama a sí misma con los hijos de ese nodo, hasta llegar a las hojas.

En el proyecto hay dos tipos de árbol: el **genérico** y el **binario**.

### Árbol genérico (`arboles/tree.py`)

En un árbol genérico (también llamado n-ario) **cada nodo puede tener cualquier número
de hijos**: 0, 1, 2, 10... Por eso el nodo guarda sus hijos en una lista.

```python
class Node:
    def __init__(self, data):
        self.data = data        # el nombre guardado en el nodo
        self.children = []      # lista de hijos (vacía = es una hoja)

    def add_child(self, child):
        self.children.append(child)
```

Operaciones que tiene:

| Operación | Función | Cómo funciona |
|---|---|---|
| Insertar | `add_child(child)` | Agrega el nodo al final de la lista de hijos del padre. |
| Mostrar | `show(node)` | Imprime el nodo y luego sus hijos, cada nivel con más espacios. |
| Recorrido preorden | `preorder(node)` | Primero el nodo y después sus hijos. |
| Recorrido postorden | `postorder(node)` | Primero los hijos y al final el nodo. |
| Buscar | `search(node, data)` | Revisa el nodo; si no es, busca dentro de cada hijo. Retorna el nodo o `None`. |
| Nivel | `level_of(node, data)` | Igual que buscar, pero suma 1 cada vez que baja a un hijo. Retorna -1 si no existe. |
| Contar nodos | `count_nodes(node)` | 1 por el nodo + los nodos de cada hijo. |
| Contar hojas | `count_leaves(node)` | Si no tiene hijos es 1; si tiene, suma las hojas de los hijos. |
| Altura | `height(node)` | Una hoja mide 0; los demás miden 1 + la altura de su hijo más alto. |
| Eliminar | `delete(node, data)` | El padre quita al nodo de su lista de hijos. Se borra con todo su subárbol. |

**Cómo se guarda en un archivo.** Cada nodo se escribe en una línea con el formato
`nivel;nombre`, en preorden (`save_tree`). Para leerlo (`load_tree`) se usa una regla
simple: **el padre de un nodo es el último nodo que se leyó en el nivel anterior**.

```
0;ComponentX          <- raíz
1;Componentes         <- hijo de ComponentX
2;Procesadores        <- hijo de Componentes (último nodo de nivel 1)
2;Memoria RAM         <- hijo de Componentes
1;Perifericos         <- hijo de ComponentX
2;Mouse               <- hijo de Perifericos (ahora es el último de nivel 1)
```

`get_or_build(archivo, funcion)` carga el árbol si el archivo existe. Si no existe, crea
el árbol inicial con la función que se le pasa y lo guarda.

#### Dónde se usa el árbol genérico

**1. Árbol de categorías** (`arboles/categories.py`, menú 7, archivo `Categories.txt`).
Representa el catálogo: una categoría puede tener 2, 3 o ninguna subcategoría, por eso
es genérico.

```
ComponentX                    nivel 0 (raíz)
|-- Componentes               nivel 1
|   |-- Procesadores          nivel 2 (hoja)
|   |-- Memoria RAM           nivel 2 (hoja)
|-- Perifericos               nivel 1
|   |-- Mouse                 nivel 2 (hoja)
|   |-- Teclados              nivel 2 (hoja)
|   |-- Monitores             nivel 2 (hoja)
|-- Almacenamiento            nivel 1 (hoja, no tiene subcategorías)

Altura: 2 · Nodos: 9 · Hojas: 6
```

`add_category(root, padre, nueva)` busca el padre y agrega la nueva categoría como su
hijo. No deja repetir nombres.

**2. Árbol de roles** (`arboles/roles.py`, menú 8, archivo `Roles.txt`).
Representa cómo se organiza la empresa: áreas y dentro de cada área sus roles.
Aquí **el nivel dice qué es cada nodo**:

```
ComponentX                    nivel 0: raíz
|-- Administracion            nivel 1: área
|   |-- admin                 nivel 2: rol
|   |-- gerente               nivel 2: rol
|-- Ventas                    nivel 1: área
|   |-- vendedor              nivel 2: rol
|-- Bodega                    nivel 1: área
    |-- empleado              nivel 2: rol

Altura: 2 · Nodos: 8 · Hojas: 4 (los roles)
```

- `is_valid_role(rol)` revisa que el rol esté en el nivel 2. Se usa al crear o actualizar
  un usuario, así un usuario no puede tener un rol que no existe (ni un área como rol).
- `add_role(root, area, nombre)` solo agrega un rol si el padre es un área (nivel 1) y el
  nombre tiene máximo 15 caracteres (el tamaño del campo `rol` en `Users_direct.txt`).
- `delete_role(root, nombre)` no deja borrar un rol (o un área) si algún usuario activo
  lo tiene.
- `build_roles_with_users(root)` hace una copia del árbol con los usuarios colgando de su
  rol, solo para mostrarla. En esa copia la altura es 3.

### Árbol binario (`arboles/binary_tree.py`)

En un árbol binario **cada nodo tiene como máximo dos hijos**: uno a la izquierda
(`left`) y otro a la derecha (`right`). Si no hay hijo, el valor es `None`.

```python
class BinaryNode:
    def __init__(self, key, value=None):
        self.key = key          # lo que identifica al nodo (un nombre o el ID del pedido)
        self.value = value      # datos extra (en pedidos: los campos de la línea)
        self.left = None        # hijo izquierdo
        self.right = None       # hijo derecho
```

Operaciones generales (sirven para cualquier árbol binario):

| Operación | Función | Cómo funciona |
|---|---|---|
| Mostrar | `show(node)` | Imprime cada nodo indicando si es `Raiz`, `Izq` o `Der`. |
| Preorden | `preorder(node)` | Nodo, izquierda, derecha. |
| Inorden | `inorder(node)` | Izquierda, nodo, derecha. |
| Postorden | `postorder(node)` | Izquierda, derecha, nodo. |
| Buscar | `find(node, key)` | Busca por los dos lados (sirve para árboles sin orden). |
| Contar nodos | `count_nodes(node)` | 1 + los nodos de la izquierda + los de la derecha. |
| Contar hojas | `count_leaves(node)` | Un nodo sin `left` ni `right` es una hoja. |
| Altura | `height(node)` | 1 + la altura del lado más alto. Un árbol vacío mide -1 y una hoja 0. |

#### Árbol binario de estados (`arboles/orders_tree.py`)

Clasifica los estados de un pedido. Cada división es una pregunta de dos opciones
(¿el pedido sigue en curso o ya terminó?), por eso es binario:

```
                 Pedidos                    nivel 0
              /           \
        En curso         Finalizados        nivel 1
        /      \          /        \
  pendiente   activo  entregado  cancelado  nivel 2 (hojas)

Altura: 2 · Nodos: 7 · Hojas: 4
```

- Solo las hojas son estados válidos (`is_valid_status`). Se usa al crear o actualizar
  un pedido.
- `is_in_progress(estado)` busca el estado solo en el lado izquierdo (En curso).
- Este árbol es fijo: se arma a mano en `build_status_tree()` y no se le borran nodos.

#### Árbol binario de búsqueda o ABB (pedidos por ID)

Un ABB es un árbol binario con una regla: **los valores menores van a la izquierda y los
mayores a la derecha**. Gracias a esa regla:

- Para buscar, en cada nodo se elige un solo lado, así que no hay que revisar todos los nodos.
- El nodo más a la izquierda es el menor (`minimum`).
- El recorrido **inorden** devuelve los valores ordenados de menor a mayor.

Ejemplo con los pedidos 4, 2, 6, 1, 3, 5, 7 insertados en ese orden:

```
            4                 nivel 0
          /   \
         2     6              nivel 1
        / \   / \
       1   3 5   7            nivel 2 (hojas)

Inorden:   1, 2, 3, 4, 5, 6, 7
Preorden:  4, 2, 1, 3, 6, 5, 7
Postorden: 1, 3, 2, 5, 7, 6, 4
```

| Operación | Función | Cómo funciona |
|---|---|---|
| Insertar | `insert(node, key, value)` | Baja comparando (menor a la izquierda, mayor a la derecha) hasta encontrar un lugar vacío. No inserta claves repetidas. |
| Buscar | `search(node, key)` | Igual que insertar: compara y baja por un solo lado. Ejemplo: buscar 5 visita 4, 6 y 5. |
| Mínimo | `minimum(node)` | Baja siempre a la izquierda hasta que no haya más. |
| Eliminar | `delete(node, key)` | Busca el nodo y lo quita según el caso (ver abajo). |

Los 3 casos de la eliminación:

1. **El nodo es una hoja**: simplemente se quita.
2. **El nodo tiene un solo hijo**: ese hijo toma su lugar.
3. **El nodo tiene dos hijos**: se reemplaza por el menor de su lado derecho (el
   *sucesor*) y después se borra el sucesor de su lugar original.
   Ejemplo: al borrar 4 en el árbol de arriba, el sucesor es 5 y pasa a ser la raíz.

**Cómo se usa en pedidos.** `load_order_trees()` lee `Orders.txt` y arma **dos ABB**
ordenados por ID: uno con los pedidos en curso y otro con los finalizados. El árbol de
estados decide a cuál va cada pedido. En el menú de pedidos:

| Opción | Qué hace | Operación de árbol |
|---|---|---|
| 5 | Mostrar el árbol de estados | `show`, `count_nodes`, `count_leaves`, `height` |
| 6 | Pedidos en curso ordenados por ID | `inorder` sobre el ABB en curso |
| 7 | Pedidos finalizados ordenados por ID | `inorder` sobre el ABB de finalizados |
| 8 | Siguiente pedido a preparar | `minimum` (el ID más pequeño es el más antiguo) |
| 9 | Finalizar un pedido | `delete` del ABB en curso + `insert` en el de finalizados |
| 10 | Buscar un pedido por ID | `search` en los dos ABB |

### Genérico vs. binario

| | Árbol genérico | Árbol binario |
|---|---|---|
| Hijos por nodo | Cualquier cantidad | Máximo 2 (`left` y `right`) |
| Cómo guarda los hijos | Lista `children` | Dos atributos |
| Recorridos | Preorden y postorden | Preorden, inorden y postorden |
| Altura de una hoja | 0 | 0 (un árbol vacío es -1) |
| Se usa para | Categorías y roles | Estados de pedido y ABB de pedidos |
| Por qué | Las jerarquías tienen un número variable de hijos | Las decisiones son de dos opciones y el ABB permite buscar y ordenar por ID |

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
├── sorting/                 # algoritmos de ordenamiento
│   ├── direct_sorting.py    # merge sort sobre archivos directos
│   └── external_sorting.py  # ordenamiento externo secuencial
└── arboles/                 # árboles
    ├── tree.py              # árbol genérico (Node y sus operaciones)
    ├── categories.py        # árbol de categorías
    ├── roles.py             # árbol de roles
    ├── binary_tree.py       # árbol binario y ABB (BinaryNode y sus operaciones)
    └── orders_tree.py       # árbol de estados y ABB de pedidos
```
## Posibles mejoras

- Validar y ordenar correctamente por valores `float`.
- Separar cada entidad en su propio directorio de datos.
- Reusar el código de los CRUD para no repetir la misma lógica en cada módulo.
```