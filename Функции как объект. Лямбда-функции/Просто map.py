def simple_map(transformation, values):
    res = []
    for i in values:
        res.append(transformation(i))
    return res