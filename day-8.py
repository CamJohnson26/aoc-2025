# Part 1: 6:08 paused 6:33
import math

points = []
with open('inputs/day-8.txt', 'r') as f:
    lines = f.readlines()
    points = [[int(num) for num in l.split(',')] for l in lines]

def get_distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2 + (point_b[2] - point_a[2])**2)

def get_closest_point(point, points):
    closest = (-1,-1,-1)
    closest_distance = -1
    for test_point in points:
        if test_point[0] == point[0] and test_point[1] == point[1] and test_point[2] == point[2]:
            continue
        d = get_distance(point, test_point)
        if d < closest_distance or closest_distance == -1:
            closest_distance = d
            closest = test_point
    return closest, closest_distance

def get_cluster_closest_point(cluster_a, cluster_b):
    closest = (-1,-1,-1)
    closest_distance = -1
    for p_a in cluster_a:
        for p_b in cluster_b:
            d = get_distance(p_a, p_b)
            if d < closest_distance or closest_distance == -1:
                closest_distance = d
                closest = (p_a, p_b)
    return closest, closest_distance


def join_closest_clusters(clusters):
    closest_pair = None
    closest_distance = -1
    for c in clusters:
        for test_cluster in clusters:
            if c == test_cluster:
                continue
            test_closest, test_closest_distance = get_cluster_closest_point(c, test_cluster)
            if test_closest_distance < closest_distance or closest_distance == -1:
                closest_distance = test_closest_distance
                closest_pair = (c, test_cluster)
    joined_clusters = []
    for c in clusters:
        if c != closest_pair[0] and c != closest_pair[1]:
            joined_clusters.append(c)
    joined_clusters.append(closest_pair[0] + closest_pair[1])
    return joined_clusters

# clusters = [[p] for p in points]
# for x in range(18):
#     print(x)
#     clusters = join_closest_clusters(clusters)
#
# lengths = []
# for c in clusters:
#     print(len(c))
#     lengths.append(len(c))

# Have to consider all pairs, so have to do this brute force
all_pairs = []
found = {}
index = 0
for p in points:
    for p_b in points:
        if p != p_b and not hash(tuple([tuple(p), tuple(p_b)])) in found and not hash(tuple([tuple(p_b), tuple(p)])) in found:
            all_pairs.append([p, p_b])
            found[hash(tuple([tuple(p), tuple(p_b)]))] = True

all_pairs.sort(key=lambda pair: get_distance(pair[0], pair[1]))

index = 0
limit = -1

print(all_pairs[:limit])

# count = 0
# for p in points:
#     found = False
#     for a in all_pairs[:1000]:
#         if p in a:
#             found = True
#             break
#     if not found:
#         print(p)
#         count+=1
# print(count)

#53148
#41127

clusters = [[p] for p in points]
for pair in all_pairs[:limit]:
    p_a = pair[0]
    p_b = pair[1]
    cluster_a = [c for c in clusters if p_a in c][0]
    cluster_b = [c for c in clusters if p_b in c][0]

    if cluster_a == cluster_b:
        continue
    else:
        clusters = [c for c in clusters if c != cluster_a and c != cluster_b]
        clusters.append(cluster_a + cluster_b)

    if len(clusters) == 1:
        print('DONE', p_a, p_b)
        break
    index += 1


lengths = []
for c in clusters:
    # print(len(c))
    lengths.append(len(c))

print(sorted(lengths,reverse=True))

