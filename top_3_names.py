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


def get_unique_names(names):
    unique_names = set(names)
    return unique_names


def get_count_names(unique_names):
    name_and_count = []
    for name in unique_names:
        name_and_count.append([name, names.count(name)])
    return name_and_count


def sort_counted_names(name_and_count):
    name_and_count.sort(key=lambda x: x[1], reverse=True)
    return name_and_count


def get_top_3(sorted_name_and_count):
    top_3 = []
    for element in sorted_name_and_count[:3]:
        top_3.append(f'{element[0]}: {element[1]} раз(а)')
    return top_3


def print_result(top_3):
    print(", ".join(top_3))


if __name__ == '__main__':
    flat_list = get_flat_list(mentors)
    names = get_names(flat_list)
    unique_names = get_unique_names(names)
    name_and_count = get_count_names(unique_names)
    sorted_name_and_count = sort_counted_names(name_and_count)
    top_3 = get_top_3(sorted_name_and_count)
    print_result(top_3)
