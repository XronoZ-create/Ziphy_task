
def get_children(all_names: dict, parents: list) -> dict:
    expected = {}

    for one_parent in parents:
        children = all_names[one_parent]
        if len(children) == 0:  # Если нет детей
            expected[one_parent] = {}
        else:  # Если есть дети
            expected[one_parent] = get_children(all_names, children)
    return expected


def to_tree(source_list: list) -> dict:
    all_names = {}
    #  Пишем все названия узлов
    for one_obj in source_list:
        if not one_obj[0] is None and list(all_names.keys()).count(one_obj[0]) == 0:
            all_names[one_obj[0]] = []
        if list(all_names.keys()).count(one_obj[1]) == 0:
            all_names[one_obj[1]] = []

    #  Пишем прямых родственников для полученных узлов
    for one_obj in source_list:
        if one_obj[0] is None:
            pass
        else:
            all_names[one_obj[0]].append(one_obj[1])

    expected = {}
    for one_obj in source_list:
        if one_obj[0] is None:  # Выбираем только элементы корневого узла
            expected[one_obj[1]] = get_children(all_names=all_names, parents=all_names[one_obj[1]])

    return expected


if __name__ == '__main__':
    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]

    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }

    print(to_tree(source))
    assert to_tree(source) == expected
