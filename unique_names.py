from const import mentors


def get_flat_list(list_):
    flat_list = []
    for sub_list in list_:
        if isinstance(sub_list, list):
            flat_list.extend(sub_list)
        else:
            return None
    return flat_list


def get_names(full_names):
    names = []
    for full_name in full_names:
        split_name = full_name.split()
        if len(split_name) == 2:
            names.append(full_name.split()[0])
        else:
            return None
    return names


def get_unique_sorted_names(names):
    unique_names = sorted(set(names))
    return unique_names


def print_result(unique_names):
    intro = 'Уникальные имена преподавателей: '
    print(intro + ', '.join(unique_names))


if __name__ == '__main__':
    flat_list = get_flat_list(mentors)
    names = get_names(flat_list)
    unique_sorted_names = get_unique_sorted_names(names)
    print_result(unique_sorted_names)
