from general_utls.src.io.file_helpers import Files
from mako.template import Template


class TemplateRenderer:
    @classmethod
    def render(cls, path, **params):
        template = Template(filename=Files.get_absolute_path(path))
        return template.render(**params)


