import logging
from pyramid.config import Configurator
from deform import Form, ValidationFailure
import colander as c
from rebecca.form.blockdiag.schema import BlockDiag
from rebecca.form.blockdiag.widgets import BlockDiagWidget


logger = logging.getLogger(__name__)

class DemoSchema(c.Schema):
    name = c.SchemaNode(c.String())
    diag = c.SchemaNode(BlockDiag(),
                        widget=BlockDiagWidget(""))


def demo_form(request):
    form = Form(DemoSchema(), buttons=('Save',))
    if request.method == 'POST':
        controls = request.params.items()
        try:
            params = form.validate(controls)
            logger.debug("OK")
            logger.debug("result = {}".format(params))
            return dict(form=form.render(),
                        result=params)
        except ValidationFailure as e:
            return dict(form=e.render(),
                        result=None)
    return dict(form=form.render(),
                result=None)


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.add_view(demo_form, name="demo", renderer="templates/demo_form.pt")
    return config.make_wsgi_app()
