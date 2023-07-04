def minimum_time_to_send_groups(groups, planes):
    groups.sort(reverse=True)
    planes.sort(reverse=True)
    time = 0

    while groups:
        if not planes:
            break

        group = groups[0]
        plane = planes[0]

        time += max(group, plane)
        groups[0] -= min(group, plane)
        planes[0] -= min(group, plane)

        if groups[0] == 0:
            groups.pop(0)

        if planes[0] == 0:
            planes.pop(0)

    return time

groups = [8, 1, 6, 9]
planes = [7, 3, 2]
min_time = minimum_time_to_send_groups(groups, planes)
print(min_time)
