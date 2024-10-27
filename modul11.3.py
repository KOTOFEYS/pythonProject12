def introspection_info(obj):
    dict = {}
    dict['type'] = type(obj).__name__
    meaning_attr = []
    for i in dir(obj):
        if not callable(getattr(obj,i)):
            meaning_attr.append(i)
            dict['attributes'] = meaning_attr
    meaning_meth = []
    for i in dir(obj):
        if callable(getattr(obj,i)):
            meaning_meth.append(i)
            dict['methods'] = meaning_meth
    dict['module'] = introspection_info.__module__
    return(dict)

number_info = introspection_info(42)
print(number_info)





