from django import template
register=template.Library()
def is_lower(s):
    for i in s:
        if 'A'<=i<='Z':
            return False
    return True
def is_upper(s):
    for i in s:
        if 'a'<=i<='z':
            return False
    return True
register.filter('is_lower',is_lower)
register.filter('is_upper',is_upper)

@register.filter(name="plural")
def plural(n,s):
    if n>1:
        return str(n)+" "+s+"s"
    else:
        return str(n)+" "+s