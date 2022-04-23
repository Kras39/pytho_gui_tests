def test_add_group(app):
    old_list = app.group.get_groups_list()
    app.group.add_new_group("my group")
    new_list = app.group.get_groups_list()
    old_list.append("my group")
    assert sorted(old_list) == sorted(new_list)

def test_add_group_from_params(app, data_groups):
    group = data_groups
    old_groups_list = app.group.get_groups_list()
    app.group.add_new_group(group)
    new_groups_list = app.group.get_groups_list()
    old_groups_list.append(group)
    assert sorted(old_groups_list) == sorted(new_groups_list)