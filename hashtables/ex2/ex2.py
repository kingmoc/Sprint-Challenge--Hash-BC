#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    # stopper = True
    # i = 0

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    # print(hashtable.storage[0].key)

    # while i < length:
    #     route.append(hash_table_retrieve(hashtable, 'NONE'))
    #     route.append(hash_table_retrieve(hashtable, route[i]))
    #     i += 1
    #     route.append(hash_table_retrieve(hashtable, route[i]))
        

    for i in range(length):
        route[0] = hash_table_retrieve(hashtable, 'NONE')
        if route[i] is None:
            route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))
