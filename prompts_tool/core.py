"""Original bounded concept exercise with supplied synthetic data only."""


def fields(value, required, optional=()):
    if not isinstance(value, dict) or not set(required) <= value.keys() or not value.keys() <= set(required) | set(optional):
        raise ValueError("Unexpected or missing object fields")


def integer(value, low=0, high=10**12):
    if type(value) is not int or not low <= value <= high:
        raise ValueError("Integer outside the supported range")
    return value


def label(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 80 or any(ord(c) < 32 for c in value):
        raise ValueError("Expected a nonblank label of at most 80 characters")
    return value.strip()


def sequence(value, maximum):
    if not isinstance(value, list) or len(value) > maximum:
        raise ValueError("Expected a bounded list")
    return value


def day(value):
    from datetime import date
    import re
    if not isinstance(value,str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}",value):
        raise ValueError("Use YYYY-MM-DD")
    return date.fromisoformat(value)


def text(value,maximum=10000):
    if not isinstance(value,str) or len(value)>maximum:
        raise ValueError("Expected bounded text")
    return value

def evaluate(data):
    import json
    fields(data,("response","contains","excludes"),("json_keys",))
    response=text(data["response"])
    required=[label(item) for item in sequence(data["contains"],30)]
    forbidden=[label(item) for item in sequence(data["excludes"],30)]
    keys=[label(item) for item in sequence(data.get("json_keys",[]),30)]
    checks=[{"kind":"contains","value":item,"passed":item in response} for item in required]
    checks.extend({"kind":"excludes","value":item,"passed":item not in response} for item in forbidden)
    if keys:
        try:
            payload=json.loads(response)
        except ValueError:
            payload=None
        checks.extend({"kind":"json_key","value":key,"passed":isinstance(payload,dict) and key in payload} for key in keys)
    return {"passed":all(row["passed"] for row in checks),"checks":checks}
