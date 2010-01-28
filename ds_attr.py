def show_attr(type_name, obj, indent=''):
    for attr in AdminConfig.attributes(type_name).split('\n'):
        print attr
        item, object_type = attr.split(' ')[0], attr.split(' ')[1]
        value = AdminConfig.showAttribute(obj,item)
        if object_type.find('String')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('boolean')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('Boolean')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('int')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('long')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('Property')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('ENUM')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('ConnectionTest')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('J2EEResourceProperty')>=0:
            print indent, item, value, object_type
            continue
        if object_type.find('None')>=0:
            print indent, item, value, object_type
            continue
        if value == '[]':
            print indent, item, value, object_type
            continue
        else:
            object_type = strip_object(object_type)
            value = strip_object(value)
            indent += '  '
            show_attr(object_type, value, indent)

def strip_object(name):
    if name.find('*')>=0:
        return name[:-1]
    elif name.find('@')>=0:
        return name[:-1]
    elif name.find('[')==0 and name.find(']')==len(name)-1:
        return name[1:-1]
    else:
        return name

show_attr('DataSource',ds)
