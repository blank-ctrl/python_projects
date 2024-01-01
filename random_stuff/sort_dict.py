def sort_dict(d):
    d = sorted(d.items(), key=lambda x:x[1], reverse=True)
    d = dict(d)
    return d