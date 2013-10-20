from zope.publisher.browser import BrowserView

class Example(BrowserView):
    
    def getJS_Song(self):
        portal = self.context.portal_url.getPortalObject()
        song = portal.portal_skins.midijs.examples['AcrossTheBlackRiver1.mid']
        TEMPLATE = '<script type="text/javascript" class="javascript-settings">'
        TEMPLATE = TEMPLATE + "var song = '" + song.absolute_url() + "'; </script>"
        return TEMPLATE
        