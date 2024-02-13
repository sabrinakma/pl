import _plotly_utils.basevalidators


class HeightValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="height", parent_name="layout", **kwargs):
        super(HeightValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 10),
            **kwargs,
        )
