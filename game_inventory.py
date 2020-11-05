
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.

invent = {'rope': 1, 'sznrek': 2, 'kosa': 3}
add = {'rope': 1, 'sznrek': 1, 'kosa': 1, 'pajak': 2}
remove = ['sznrek', 'kosa', 'pajak']


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for new_item in added_items:
        if new_item in inventory:
            inventory[new_item] += added_items[new_item]  # dodaje
        else:
            inventory[new_item] = added_items[new_item]  # dopisuje
    return inventory


print(add_to_inventory(invent, add))


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    print('INVENTORY')
    for key, value in inventory.items():
        print(key, '___________', value)


print(display_inventory(invent))


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        inventory.pop(item, None)

    return inventory


print(remove_from_inventory(invent, remove))


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    print('INVENTORY REMOVE ITEMS ')
    for key, value in inventory.items():
        print(key, '___________', value)


print(display_inventory(invent))


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    result = []
    with open(filename) as file:
        for line in file.readlines():
            result = line.strip().split(',')

    dict_inventory = {}
    for i in result:
        if i in dict_inventory:
            dict_inventory[i] += 1
        else:
            dict_inventory[i] = 1

    inventory = add_to_inventory(inventory, dict_inventory)

    return inventory


print(import_inventory(invent, 'test_inventory.csv'))


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    print(' ADD INVENTORY ')
    for key, value in inventory.items():
        print(key, '___________', value)


print(display_inventory(invent))


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""
    result = []
    with open(filename,'w') as data_file:
        for item in inventory:
            result.append([item]*inventory[item])

        data_file.write(str(result).replace('[','').replace(']','').replace('\'',''))
        print(result)

print(export_inventory(invent,'test.csv'))