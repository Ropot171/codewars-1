def unique_in_order(sequence):
    finish_list = []
    for i in sequence:
        if len(finish_list) == 0 or i != finish_list[-1]:
                finish_list.append(i)
    return finish_list