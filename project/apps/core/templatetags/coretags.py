from django import template

register = template.Library()


@register.filter('field_type')
def field_type(field):
    """
    Get the name of the field class.
    """
    if hasattr(field, 'field'):
        field = field.field
    s = (type(field.widget).__name__).replace('Input', '').lower()
    return s

@register.filter('get_form_field')
def get_form_field(form, field):
    return form[field]

@register.filter('all_fields_hidden')
def all_fields_hidden(form):
    return all([field.is_hidden for field in form])

@register.inclusion_tag('core/form_fieldset_fields.html')
def form_as_fieldset_fields(form, fieldsets):
    """
    Render the form as a fieldset form. 
    Example usage in template with 'myform' and 'myfieldsets as context attributes: 
        {% form_as_fieldset_fields myform myfieldsets %}
    Sample fieldset:
    MY_FIELDSETS = (
        (
            'info', 
            ('first_name', 'middle_name', 'last_name', 'is_published')
        ),
        (
            'image', 
            ('profile_image', 'avatar_image', 'profile_image_crop')
        ),
        (
            'profile', 
            ('title', 'location', 'profile_full', 'profile_brief', 
            'website_url', 'average_artwork_cost', 'born_year', 
            'deceased_year')
        ),
    )
    """
    return {'form': form, 'fieldsets' : fieldsets}
