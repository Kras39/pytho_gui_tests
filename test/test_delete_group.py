import random

def test_del_group(app):
    if len(app.group.get_groups_list()) < 2:
        app.group.add_new_group("my group")
    old_list = app.group.get_groups_list()
    group = random.choice(old_list)
    group_number = old_list.index(group)
    app.group.delete_group(group_number)
    new_list = app.group.get_groups_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)
