import json


def validate_json(json_str: str) -> bool:
    """
    Validate a json string.

    Parameters
    ----------
    json_str : str
        The json string to validate.

    Returns
    -------
    bool
        True if the json is valid, False otherwise.
    """
    print(json_str)
    json_str = json_str.replace("`", "").replace("'", "")
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        return False
    return True