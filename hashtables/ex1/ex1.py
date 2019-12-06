#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length <= 1:
        return None

    if length == 2:
        if weights[0] + weights[1] == limit:
            return (1,0)
        else:
            return None

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    for i in range(length):
        diff = limit - weights[i]

        if hash_table_retrieve(ht, diff):
            answer = (hash_table_retrieve(ht, diff), i)
            return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
