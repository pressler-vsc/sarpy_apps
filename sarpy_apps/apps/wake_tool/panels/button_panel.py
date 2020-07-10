from tk_builder.panels.widget_panel.widget_panel import AbstractWidgetPanel
from tk_builder.widgets import basic_widgets


class ButtonPanel(AbstractWidgetPanel):
    def __init__(self, parent):
        AbstractWidgetPanel.__init__(self, parent)
        self.rect_draw = basic_widgets.Button
        self.line_draw = basic_widgets.Button
        self.point_draw = basic_widgets.Button
        self.zoom_in = basic_widgets.Button
        self.zoom_out = basic_widgets.Button

        widget_list = ["line_draw", "point_draw", "zoom_in", "zoom_out"]
        self.init_w_box_layout(widget_list, 2, column_widths=8, row_heights=2)
        self.set_label_text("wake tool buttons")
