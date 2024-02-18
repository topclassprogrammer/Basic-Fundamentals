from const import courses, mentors, durations


def make_courses_list_dict(courses, mentors, durations):
    courses_list_dict = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor,
                       "duration": duration}
        courses_list_dict.append(course_dict)
    return courses_list_dict


def make_durations_dict(courses_list_dict):
    durations_dict = {}
    for id, course in enumerate(courses_list_dict):
        durations_dict.setdefault(course['duration'], []).append(id)
    return durations_dict


def sort_durations_dict(durations_dict):
    sorted_durations_dict = dict(sorted(durations_dict.items()))
    return sorted_durations_dict


def print_result(durations_dict, courses_list_dict):
    for duration, ids in durations_dict.items():
        for id in ids:
            print(f'{courses_list_dict[id]["title"]} - {duration} месяцев')


if __name__ == '__main__':
    courses_list_dict = make_courses_list_dict(courses, mentors, durations)
    durations_dict = make_durations_dict(courses_list_dict)
    sorted_durations_dict = sort_durations_dict(durations_dict)
    print_result(sorted_durations_dict, courses_list_dict)
