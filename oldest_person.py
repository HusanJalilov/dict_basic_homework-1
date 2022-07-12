def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    old=[]
    for x in people:
        old.append(people[x])
    z=max(old)
    for y in people:
        if people[y]==z:
            print(y)  
        
oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16})