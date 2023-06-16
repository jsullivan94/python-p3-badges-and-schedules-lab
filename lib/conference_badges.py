names = ['kev', 'john']


def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    room = 1
    assignments = []
    for name in names:
        assignments.append(f"Hello, {name}! You'll be assigned to room {room}!")
        room += 1
    return assignments


def printer(names):
    [print(badge) for badge in batch_badge_creator(names)]
    [print(assignment) for assignment in assign_rooms(names)] 
