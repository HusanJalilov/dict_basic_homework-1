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
            return y 
        
oldest({"Javohir": 23, "Sharof": 34, "Tolib": 34, "Rustam": 16})