from Plugins.Plugin import PluginDescriptor
from os import system
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.Button import Button
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox



class pinggoogel(Screen):
    skin = """<screen position="center,center" size="430,100" title="PingGoogle (v1.0)" >
	<ePixmap pixmap="skin_default/buttons/red.png" position="0,0" size="140,40" alphatest="on" />
	<ePixmap pixmap="skin_default/buttons/green.png" position="140,0" size="140,40" alphatest="on" />
	<ePixmap pixmap="skin_default/buttons/yellow.png" position="280,0" size="140,40" alphatest="on" />
	<widget name="key_red" position="0,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#9f1313" transparent="1" />
	<widget name="key_green" position="140,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#1f771f" transparent="1" />
	<widget name="key_yellow" position="280,0" zPosition="1" size="140,40" font="Regular;20" halign="center" valign="center" backgroundColor="#18188b" transparent="1" />
	</screen>"""


    def __init__(self, session, args = None):
        self.skin = pinggoogel.skin
        Screen.__init__(self, session)
        self['key_red'] = Button(_('cancel'))		
        self['key_green'] = Button(_('Start Ping'))
        self['key_yellow'] = Button(_('Stop Ping'))
        self['setupActions'] = ActionMap(['SetupActions', 'ColorActions'], {'green': self.startlog,
         'red': self.cancel,
         'yellow': self.stoplog}, -2)


    def cancel(self):
        self.close(False)

    def startlog(self):
		system(' ping 8.8.8.8 > /dev/null & exit')
		self.session.open(MessageBox,_("Dauerping auf Google wurde gestartet"), MessageBox.TYPE_INFO)
	
    def stoplog(self):
		system('killall ping')
		self.session.open(MessageBox,_("Dauerping auf Google wurde gestoppt"), MessageBox.TYPE_INFO)
	
	
		
def main(session, **kwargs):
    session.open(pinggoogel)


def Plugins(**kwargs):
    return [PluginDescriptor(name='PingGoogle', description=_('Dauerping auf Google'), where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main, icon='plugin.png')]

