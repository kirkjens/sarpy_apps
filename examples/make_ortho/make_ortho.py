import os

import tkinter
from tkinter.filedialog import askopenfilename
from examples.make_ortho.ortho_button_panel import OrthoButtonPanel
from tk_builder.widgets.axes_image_canvas import AxesImageCanvas
from sarpy_apps.supporting_classes.complex_image_reader import ComplexImageReader
from tk_builder.panel_builder import WidgetPanel
from sarpy_apps.supporting_classes.quick_ortho import QuickOrtho


class Ortho(WidgetPanel):
    button_panel = OrthoButtonPanel         # type: OrthoButtonPanel
    raw_frame_image_panel = AxesImageCanvas     # type: AxesImageCanvas
    ortho_image_panel = AxesImageCanvas         # type: AxesImageCanvas

    fname = "None"  # type: str
    remap_type = "density"  # type: str
    image_reader = None  # type: ComplexImageReader

    def __init__(self, primary):
        primary_frame = tkinter.Frame(primary)
        WidgetPanel.__init__(self, primary_frame)

        widget_list = ["button_panel", "raw_frame_image_panel", "ortho_image_panel"]
        self.init_w_horizontal_layout(widget_list)

        # define panels widget_wrappers in primary frame
        self.button_panel.set_spacing_between_buttons(0)
        self.raw_frame_image_panel.set_canvas_size(600, 400)
        self.raw_frame_image_panel.canvas.rescale_image_to_fit_canvas = True
        self.ortho_image_panel.set_canvas_size(600, 400)
        self.ortho_image_panel.canvas.rescale_image_to_fit_canvas = True

        # need to pack both primary frame and self, since this is the main app window.
        primary_frame.pack()

        # bind events to callbacks here
        self.button_panel.fname_select.on_left_mouse_click(self.callback_set_filename)
        self.button_panel.pan.on_left_mouse_click(self.callback_set_to_pan)
        self.button_panel.display_ortho.on_left_mouse_click(self.callback_display_ortho_image)

    # noinspection PyUnusedLocal
    def callback_set_to_pan(self, event):
        self.raw_frame_image_panel.canvas.set_current_tool_to_pan()
        self.raw_frame_image_panel.canvas.hide_shape(self.raw_frame_image_panel.canvas.variables.zoom_rect_id)

    # noinspection PyUnusedLocal
    def callback_set_filename(self, event):
        image_file_extensions = ['*.nitf', '*.NITF']
        ftypes = [
            ('image files', image_file_extensions),
            ('All files', '*'),
        ]
        new_fname = askopenfilename(initialdir=os.path.expanduser("~"), filetypes=ftypes)
        if new_fname:
            self.fname = new_fname
            self.image_reader = ComplexImageReader(new_fname)
            self.raw_frame_image_panel.set_image_reader(self.image_reader)

    # noinspection PyUnusedLocal
    def callback_display_ortho_image(self, event):
        ortho_object = QuickOrtho(self.raw_frame_image_panel, self.image_reader)
        orthod_image = ortho_object.create_ortho(self.ortho_image_panel.canvas.variables.canvas_height, self.ortho_image_panel.canvas.variables.canvas_width)
        self.ortho_image_panel.canvas.set_image_from_numpy_array(orthod_image)


if __name__ == '__main__':
    root = tkinter.Tk()
    app = Ortho(root)
    root.mainloop()
