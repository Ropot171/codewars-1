import math


def get_distance(point1, point2):
    (x1, y1), (x2, y2) = point1, point2
    xs = x2 - x1
    ys = y2 - y1

    return math.sqrt(xs ** 2 + ys ** 2)

def get_the_nearest_location(locations, point):
    if not locations:
        return None
    distance = get_distance(locations[0][1], point)
    nearest_location = locations[0]
    for location in locations:
        if get_distance(location[1], point) < distance:
            distance = get_distance(location[1], point)
            nearest_location = location
    return nearest_location






def test_get_the_nearest_location():
    locations = [
        ['Park', [10, 5]],
        ['Sea', [1, 3]],
        ['Museum', [8, 4]],
    ]

    currentPoint = [5, 5]

    result = get_the_nearest_location([], currentPoint)
    assert result is None

    result2 = get_the_nearest_location(locations, currentPoint)
    assert result2 == ['Museum', [8, 4]]

    currentPoint2 = [1, 3]
    result3 = get_the_nearest_location(locations, currentPoint2)
    assert result3 == ['Sea', [1, 3]]

    locations2 = [
        ['Hotel', [7, 3]],
        ['Square', [5, 6]],
    ]

    result4 = get_the_nearest_location(locations2, currentPoint2)
    assert result4 == ['Square', [5, 6]]

    locations3 = [
        ['Hotel', [1, 2]],
        ['Square', [5, 6]],
    ]
    result5 = get_the_nearest_location(locations3, currentPoint2)
    assert result5 == ['Hotel', [1, 2]]


