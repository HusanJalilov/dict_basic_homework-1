def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    latter=0
    number=0
    for x in txt:
        if x.isdigit():
            number+=1
        else:
            latter+=1
    all={"LATTERS":latter,"NUMBER":number}
    print(all)
count_all("husan 22")


