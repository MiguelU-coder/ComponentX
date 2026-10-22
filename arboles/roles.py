from arboles.tree import Node, search, level_of, delete, get_or_build

ROLES_FILE = "Roles.txt"

# Levels of the roles tree:
# 0 = root (ComponentX), 1 = area, 2 = role
AREA_LEVEL = 1
ROLE_LEVEL = 2


def build_roles():
    root = Node("ComponentX")
    administration = Node("Administracion")
    sales = Node("Ventas")
    warehouse = Node("Bodega")

    root.add_child(administration)
    root.add_child(sales)
    root.add_child(warehouse)

    administration.add_child(Node("admin"))
    administration.add_child(Node("gerente"))
    sales.add_child(Node("vendedor"))
    warehouse.add_child(Node("empleado"))
    return root


def get_roles_tree():
    return get_or_build(ROLES_FILE, build_roles)


## Function for getting the names of all the roles (level 2 nodes)
## @params: root
## @return: list with the role names
def list_roles(root):
    roles = []
    for area in root.children:
        for role in area.children:
            roles.append(role.data)
    return roles


## Function for checking if a rol exists in the roles tree
## Only level 2 nodes are roles (areas and root are not valid roles)
## @params: rol
## @return: True if the rol is valid, False otherwise
def is_valid_role(rol):
    root = get_roles_tree()
    return level_of(root, rol) == ROLE_LEVEL


def add_area(root, name):
    if search(root, name) is not None:
        print("That name already exists in the roles tree")
        return False

    root.add_child(Node(name))
    return True


def add_role(root, area, name):
    area_node = search(root, area)
    if area_node is None or level_of(root, area) != AREA_LEVEL:
        print("The area does not exist")
        return False

    # The rol field of a user register has 15 characters
    if len(name) > 15:
        print("The role name can have at most 15 characters")
        return False

    if search(root, name) is not None:
        print("That name already exists in the roles tree")
        return False

    area_node.add_child(Node(name))
    return True


## Function for deleting a role or an area (with its roles)
## It is not allowed if an active user has that role
## @params: root, name
## @return: True if it was deleted, False otherwise
def delete_role(root, name):
    from direct.users import get_active_users

    if name == root.data:
        print("The root can not be deleted")
        return False

    node = search(root, name)
    if node is None:
        print("Role not found")
        return False

    # Roles that would be deleted: the node itself or the roles of the area
    if level_of(root, name) == AREA_LEVEL:
        deleted_roles = [role.data for role in node.children]
    else:
        deleted_roles = [name]

    for user_id, user_name, rol in get_active_users():
        if rol in deleted_roles:
            print(f"Can not delete: user {user_id} ({user_name}) has the rol '{rol}'")
            return False

    return delete(root, name)


## Function for building a copy of the roles tree with the users as children of their role
## The copy is only for showing, it is not saved
## @params: root
## @return: root of the new tree
def build_roles_with_users(root):
    from direct.users import get_active_users

    users = get_active_users()
    new_root = Node(root.data)

    for area in root.children:
        new_area = Node(area.data)
        new_root.add_child(new_area)

        for role in area.children:
            new_role = Node(role.data)
            new_area.add_child(new_role)

            for user_id, user_name, rol in users:
                if rol == role.data:
                    new_role.add_child(Node(f"{user_id} - {user_name}"))

    return new_root
