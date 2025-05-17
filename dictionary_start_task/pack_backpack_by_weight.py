def pack_backpack_by_weight(weight):
    things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
              'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
              'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
    weight_correct = weight * 1000
    sorted_things = list(sorted(things.items(), key=lambda item: item[1], reverse=True))
    total_weight = 0
    result_things = ''

    for k,v in sorted_things:
        if total_weight + v <= weight_correct:
            total_weight += v
            result_things += k + ' '
    return result_things.strip()

def test_pack_backpack_by_weight():
    assert pack_backpack_by_weight(10) == 'палатка брезент удочка брюки пила карандаш спички'





