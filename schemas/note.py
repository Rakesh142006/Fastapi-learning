def noteEntity(item) -> dict :
    return {
        "id" : str(item["_id"]),
        "title" : item["title"],
        "disc" : item["disc"],
        "imoortant" : item["imoortant"],
    } 


def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]
