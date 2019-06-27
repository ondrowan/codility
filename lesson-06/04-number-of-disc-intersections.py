# def solution(array):
#     ranges = []

#     for index, radius in enumerate(array):
#         ranges.append({
#             'diameter': range(index - radius, index + radius + 1),
#             'forward_radius': range(index, index + radius + 1)
#         })

#     intersections = 0

#     for index, r in enumerate(ranges):
#         forward_radius = index + 1 + r['forward_radius'][-1] + 1
#         forward_radius = len(array) if forward_radius > len(array) else forward_radius

#         for fr in ranges[index+1:forward_radius]:
#             if set(r['forward_radius']) & set(fr['diameter']):
#                 intersections = intersections + 1

#                 if intersections == 10_000_000:
#                     return -1

#     return intersections

def solution(array):
    intersections = 0

    for index, radius in enumerate(array):
        print("Index {}, radius {}".format(index, radius))
        forward_radius_index = index + radius + 1

        for i, fr in enumerate(array[index + 1:forward_radius_index]):
            print("Checking index {} with radius {}".format(index + i + 1, fr))
            if (index + radius) - (i + index + 1) - fr <= 0:
                intersections = intersections + 1
                print("intersects")

        print("\n")

    return intersections




print(solution([1, 5, 2, 1, 4, 0]))
# assert(solution([1, 5, 2, 1, 4, 0]) == 11)
# assert(solution([1, 2147483647, 0]) == 3)