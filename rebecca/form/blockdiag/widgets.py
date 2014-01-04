#
from deform.widget import Widget, TextAreaWidget
import colander as c
from webhelpers2.html import literal

class BlockDiagWidget(TextAreaWidget):

    def __init__(self, diag_parser_url, *args, **kwargs):
        super(BlockDiagWidget, self).__init__(*args, **kwargs)
        self.diag_parser_url = diag_parser_url

    def serialize(self, field, cstruct=None, readonly=False):
        html = field.render_template('textarea', field=field, cstruct=cstruct)
        return html + '<div></div>'

    def deserialize(self, field, pstruct=None):
        return pstruct
