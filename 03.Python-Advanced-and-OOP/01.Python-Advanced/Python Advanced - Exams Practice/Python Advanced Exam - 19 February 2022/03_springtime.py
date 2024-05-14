def start_spring(**kwargs):
    objects = {}

    for name, object_type in kwargs.items():

        if object_type not in objects:
            objects[object_type] = []

        objects[object_type].append(name)

    for key, value in objects.items():
        objects[key] = sorted(value)
    objects = dict(sorted(objects.items(), key=lambda x: (-len(x[-1]), x[0])))

    output = ""
    for key, values in objects.items():
        output += f"\n{key}:"
        for value in values:
            output += f"\n-{value}"

    return output


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
