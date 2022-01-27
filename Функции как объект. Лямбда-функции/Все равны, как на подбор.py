def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2
