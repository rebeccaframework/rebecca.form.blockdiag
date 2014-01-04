#
import colander as c
from .types import BlockDiagDiagram


class BlockDiag(object):
    def serialize(self, node, appstruct):
        if appstruct is None:
            return ""
        if appstruct == c.null:
            return ""
        diag = appstruct.diag
        if diag is None:
            return ""
        return diag

    def deserialize(self, node, cstruct):
        if cstruct == c.null:
            return BlockDiagDiagram("")
        return BlockDiagDiagram(cstruct)
