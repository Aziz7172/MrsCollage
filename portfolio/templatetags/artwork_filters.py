from django import template

register = template.Library()

@register.filter(name='extract_info')
def extract_info(value, key):
    """يستخرج معلومات محددة من الوصف"""
    if not value:
        return ""
    lines = value.split('\n')
    for line in lines:
        if key in line:
            return line.split(key)[1].strip()
    return ""

@register.filter(name='remove_info')
def remove_info(value):
    """يزيل المعلومات المنسقة من الوصف"""
    if not value:
        return ""
    lines = value.split('\n')
    return '\n'.join([line for line in lines if ':' not in line or not any(k in line for k in ['Medium:', 'Dimensions:', 'Year:', 'Price:'])])