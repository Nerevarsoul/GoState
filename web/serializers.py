from .server import ma

from .models import Title


class TitleSchema(ma.ModelSchema):
    class Meta:
        model = Title

