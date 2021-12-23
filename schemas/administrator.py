def administratorEntity(item) -> dict:
    return {
            "email": item["email"],
            "contraseña": item["contraseña"],
            "nombre": item["nombre"],
            "apellido": item["apellido"]
    }


def administratorsEntity(entity) -> list:
    return [administratorEntity(item) for item in entity]
