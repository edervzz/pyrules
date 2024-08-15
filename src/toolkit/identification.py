def get_identification(_id: str, id_type: str) -> tuple:
    """ return object identification """

    if id_type is None or id_type == "__internal" or id_type == "__default":
        return int(_id), ""
    elif id_type == "__external":
        return 0, str(_id)
