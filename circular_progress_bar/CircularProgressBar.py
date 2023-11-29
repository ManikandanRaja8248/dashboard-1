# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CircularProgressBar(Component):
    """A CircularProgressBar component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- pathColor (string; required):
    this help to change path color.

- textColor (string; required):
    this help to change text color.

- textSize (string; required):
    this help to change text size.

- trailColor (string; required):
    this help to change color  trail.

- value (string; required):
    this value is for percentage."""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, value=Component.REQUIRED, textColor=Component.REQUIRED, textSize=Component.REQUIRED, pathColor=Component.REQUIRED, trailColor=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'pathColor', 'textColor', 'textSize', 'trailColor', 'value']
        self._type = 'CircularProgressBar'
        self._namespace = 'circular_progress_bar'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'pathColor', 'textColor', 'textSize', 'trailColor', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id', 'pathColor', 'textColor', 'textSize', 'trailColor', 'value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CircularProgressBar, self).__init__(**args)
