from general_utls.src.io.file_helpers import Files
from mako.template import Template


class TemplateRenderer:
    @classmethod
    def render(cls, path, strict=False, **params):
        template = Template(filename=Files.get_absolute_path(path), strict_undefined=strict)
        return template.render(**params)


