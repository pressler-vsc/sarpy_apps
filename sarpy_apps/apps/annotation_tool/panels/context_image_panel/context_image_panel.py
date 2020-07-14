from sarpy_apps.apps.annotation_tool.panels.context_image_panel.master_dashboard.context_dashboard import ContextMasterDash
from tk_builder.panels.image_canvas_panel.image_canvas_panel import ImageCanvasPanel
from tk_builder.panel_builder.widget_panel import WidgetPanel


class AppVariables:
    def __init__(self):
        self.image_fname = "None"       # type: str
        self.sicd_metadata = None


class ContextImagePanel(WidgetPanel):
    context_dashboard = ContextMasterDash         # type: ContextMasterDash
    image_canvas_panel = ImageCanvasPanel      # type: ImageCanvasPanel

    def __init__(self, parent):
        # set the master frame
        WidgetPanel.__init__(self, parent)
        self.app_variables = AppVariables()
        widgets_list = ["image_canvas_panel", "context_dashboard"]

        self.init_w_vertical_layout(widgets_list)

        self.context_dashboard.set_spacing_between_buttons(0)
        self.image_canvas_panel.set_canvas_size(600, 400)

        self.context_dashboard.file_selector.set_fname_filters(["*.NITF", ".nitf"])
        # TODO: fix this
        # self.image_canvas_panel.set_labelframe_text("Image View")
