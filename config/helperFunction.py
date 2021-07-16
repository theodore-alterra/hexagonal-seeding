def filterParameter(params):
    condition = []
    val_condition = []
    for key, value in params.items():
        if value is not None:
            if isinstance(value, int):
                text = (str(key) + " = %s ")
                val_condition.append(value)
            else:
                text = (str(key) + " LIKE %s ")
                val_condition.append("%"+value+"%")
            condition.append(text)
    return condition, val_condition