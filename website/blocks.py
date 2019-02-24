from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomepagePanelBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    material_icon_name = blocks.CharBlock()
    body = blocks.TextBlock()

    link_url = blocks.URLBlock(required=False)
    link_text = blocks.CharBlock(required=False)
    link_is_external = blocks.BooleanBlock(required=False)

    background_image = ImageChooserBlock()
    overlay_css_background_color = blocks.CharBlock()

    class Meta:
        template = 'website/blocks/homepage_panel_block.html'
