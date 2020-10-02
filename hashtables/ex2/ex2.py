#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    lookup = {}
    route = []
    # build lookup
    for i, v in enumerate(tickets):
        lookup[v.source] = v.destination

    flight = lookup['NONE']
    while flight != 'NONE':
        route.append(flight)
        flight = lookup[flight]

    route.append('NONE')
    return route

# # ⬇️ SEE WHAT IS HAPPENING USING PRINT STATEMENTS ⬇️
# def reconstruct_trip(tickets, length):
#     lookup = {}
#     route = []
#     # build the lookup
#     print('-----> Building Lookup: source, destination <-----')
#     for i, v in enumerate(tickets):
#         lookup[v.source] = v.destination

#     print(f'lookup: {lookup}')
#     flight = lookup['NONE']
#     print(f'starting flight: {flight} b/c its source is "NONE"')
#     while flight != 'NONE':
#         route.append(flight)
#         flight = lookup[flight]
#         print(f'next flight: {flight}')

#     route.append('NONE')
#     print(f'returned: {route}\n')
#     return route
