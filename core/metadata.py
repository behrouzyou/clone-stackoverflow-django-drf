from rest_framework.metadata import BaseMetadata


class CustomMetaData(BaseMetadata):
    def determine_metadata(self, request, view):
        return {
            "name":view.get_view_name(),
            "renderers": [renderer.media_type for renderer in view.renderer_classes],
            "parsers": [parser.media_type for parser in view.parser_classes]
        }
