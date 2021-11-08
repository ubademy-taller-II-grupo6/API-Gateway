def userEntity(item) -> dict:
    return {
        "email": str(item["email"]),
        "contraseña": item["contraseña"]
    }
