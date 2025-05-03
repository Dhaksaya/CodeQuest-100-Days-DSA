def main(a):
    if not isinstance(a,list):
        return 0
    return 1 + max((main(list)for t in a),default=0)[1,[2,3]]