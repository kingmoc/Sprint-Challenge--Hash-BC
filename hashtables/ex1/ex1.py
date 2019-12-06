#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # l = len(weights)
    j = 0 
    k = 1
    stopper = True

    if length <= 1:
        return None

    if length == 2:
        if weights[0] + weights[1] == limit:
            return (1,0)
        else:
            return None

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    while stopper:
        print("in while")
        if weights[j] + weights[k] != limit:
            k += 1
        if k == length - 1:
            j += 1
            k = 0
        if j == length - 1 and k == length - 1:
            return None
        else:
            # answer = (hash_table_retrieve(ht, weights[j+1]), hash`_table_retrieve(ht, weights[k+1]))
            answer = (hash_table_retrieve(ht, weights[k+1]), hash_table_retrieve(ht, weights[j+1]))
            return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# print_answer(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
# print(get_indices_of_item_weights([4, 4], 2, 8))
print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
