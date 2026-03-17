from typing import Any, Optional

# Debemos poner cualquier parametro.
# sin embargo no acepta vacio.
def sample_optional(name :Optional[str]) -> None:
    if name is None:
        return "Hey random person!"
    else:
        return f"Hi there, {name}"

# siempre retorna cualer valor 
# puede tambien ser vacio.
def sample_Any(value: Any) -> None:
    return value


if __name__ =='__main__':
    test = sample_optional("wilderd")
    test = sample_Any()
    print(test)