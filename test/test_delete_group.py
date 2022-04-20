def test_delete_group(app):
    app.groups.open_group_editor()
    old_groups = app.groups.get_group_list()
    if len(old_groups) == 0:
        app.groups.add_new_group("New Group")
    app.groups.delete_group(1)

import random

def test_del_group(app):
    if len(app.groups.get_group_list()) < 2:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    group_number = old_list.index(group)
    app.groups.delete_group(group_number)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)
