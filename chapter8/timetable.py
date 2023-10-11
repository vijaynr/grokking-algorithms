def sort_classes(classes):
    sorted_classes = sorted(classes.items(), key=lambda x:x[1][1])
    return sorted_classes


def pick_classes(classes):
    timetable = []
    sorted_classes = sort_classes(classes)
    last_cls = ""
    i = 0
    for item in sorted_classes:
        if i == 0:
            last_cls = item[0]
            timetable += [last_cls]
            i += 1
            continue
        last_cls_time = classes[last_cls]
        if item[1][0] >= last_cls_time[1]:
            last_cls = item[0]
            timetable += [last_cls]
        i += 1
    print(timetable)


# How to structure the input?
classes = {
    "art": [9, 10],
    "eng": [9.5, 10.5],
    "math": [10, 11],
    "cs": [10.5, 11.5],
    "music": [11, 12]
}


pick_classes(classes)