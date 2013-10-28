from zope.publisher.browser import BrowserView
from base64 import b16encode
import logging
logger = logging.getLogger('collective.js.midijs')

class Example(BrowserView):
    
    def getJS_Song(self):
        portal = self.context.portal_url.getPortalObject()
        song = portal.portal_skins.midijs.examples['AcrossTheBlackRiver1.mid']
        song_b64 = b16encode(song._readFile(song))
        song_data = song._readFile(song)
        TEMPLATE = '<script type="text/javascript" class="javascript-settings">'
        # TEMPLATE = TEMPLATE + "var song = '" + song_data + "'; </script>"
        TEMPLATE = TEMPLATE + "var song = '" + song.absolute_url() + "'; </script>"
        # TEMPLATE = TEMPLATE + "var song = 'data:audio/midi;base64," + song_b64 + "'; </script>"
        logger.info(TEMPLATE)
        # import pdb;pdb.set_trace()
        return TEMPLATE
        