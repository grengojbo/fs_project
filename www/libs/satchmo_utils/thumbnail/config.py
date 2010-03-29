from livesettings import ConfigurationGroup, config_register_list, IntegerValue, BooleanValue, StringValue
from django.utils.translation import ugettext_lazy as _

THUMB_GROUP = ConfigurationGroup('THUMBNAIL', _('Thumbnail Settings'))

config_register_list(
    IntegerValue(THUMB_GROUP, 
        'IMAGE_QUALITY', 
        description= _("Thumbnail quality"), 
        help_text = _("Use a 1-100 value here, which will change the quality of JPG thumbnails created for products and categories."),
        default=75,
        ordering=0),
    StringValue(THUMB_GROUP, 
        'IMAGE_SMALL_SIZE', 
        description= _("Thumbnail Small size"), 
        help_text = _("The width/height of the thumbnail small image. [width]x[height]"),
        default="85x85",
        ordering=0),
    StringValue(THUMB_GROUP, 
        'IMAGE_LARGE_SIZE', 
        description= _("Thumbnail Large size"), 
        help_text = _("The width/height of the thumbnail large image. [width]x[height]"),
        default="280x280",
        ordering=0),
        
    BooleanValue(THUMB_GROUP,
        'RENAME_IMAGES',
        description=_("Rename product images?"),
        help_text=_("Automatically rename product images on upload?"),
        default=True)
)
