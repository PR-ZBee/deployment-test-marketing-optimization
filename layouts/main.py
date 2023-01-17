from dash import html
from layouts.inputs import layout_inputs
from layouts.visualization import layout_visualization

# Main Layout (Two columns: Inputs / Chart)
main_layout = html.Div(
    [
        html.Div(
            [
                html.Div([html.H1("Marketing Optimization Toolkit")]),
            ],
            className="row",
        ),
        html.Div(
            [
                html.Div([layout_inputs], className="col-4"),
                html.Div([layout_visualization], className="col-8"),
            ],
            className="row",
        ),
    ],
    className="container",
)
