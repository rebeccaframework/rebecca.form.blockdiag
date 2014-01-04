from blockdiag.parser import parse_string, ParseException
class BlockDiagDiagram(object):
    def __init__(self, diag):
        self.diag = diag

    def is_valid(self):
        try:
            parse_string(self.diag)
            return True
        except ParseException:
            return False

    @property
    def diagram(self):
        return parse_string(self.diag)
