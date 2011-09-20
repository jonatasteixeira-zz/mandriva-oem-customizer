#!/usr/bin/env python
#  coding: utf-8 

import gtk
import subprocess
import os

class Window(gtk.Window):
    """Main window"""
    def __init__(self):
        """Initialize main program"""
        super(Window, self).__init__()

        self.create_fields()
        self.create_gui()
        
    def create_fields(self):
        """Create fields optimizations files"""

        self.optimizations = {}
        self.optimizations['/boot/gfxmenu'] = None
        self.optimizations['/boot/menu.lst'] = None
        self.optimizations['/etc/sysconfig/network'] = None
        self.optimizations['/etc/xdg/menus/positivo-applications.menu'] = None
        self.optimizations['/usr/local/Discador_Lite/data/'] = None        
        self.optimizations['/usr/share/doc/HTML/index.html'] = None        
        self.optimizations['/usr/share/gfxboot/themes/Mandriva-Positivo/'] = None
        self.optimizations['/usr/share/icons/'] = None
        self.optimizations['/usr/share/mdk/backgrounds/'] = None
        self.optimizations['/usr/share/mdk/backgrounds/default.jpg'] = None
        self.optimizations['/usr/share/mdk/screensaver/'] = None
        self.optimizations['/usr/share/plymouth/themes/Mandriva-Positivo/'] = None
        self.optimizations['/var/lib/oem/desktop/'] = None
        self.optimizations['/var/lib/oem/manual/pdfs/'] = None
        self.optimizations['/tmp/rootpwd'] = None

    def create_gui(self):
        """Create a main window and all your children"""
         
        self.set_title("Mandriva Optimizer")
        self.set_default_size(230, 470)
        self.connect('destroy', gtk.main_quit)

        self.body = self.gui_create_body()
        self.statusbar = self.gui_create_statusbar()

        vbox = gtk.VBox(False, 0)
        vbox.pack_start(self.body, True, True, 0)
        vbox.pack_start(self.statusbar, False, False, 0)
        
        self.add(vbox)
        self.show_all()

    def gui_create_body(self):
        """Create a frame to show logs"""
        frame_title = "Optimize"

        frame = gtk.Frame(frame_title)
        frame.set_border_width(10)

#         scrolled_window = gtk.ScrolledWindow()

        buttons = gtk.VBox()
        
        button_boot = gtk.Button("Boot")
        button_machine_name = gtk.Button("Machine Name")
        button_menu = gtk.Button("Menu")
        button_dialer_theme = gtk.Button("Dialer Theme")
        button_home_page = gtk.Button("Home Page")
        button_bootloader_theme = gtk.Button("Bootloader Theme")
        button_icons = gtk.Button("Icons")
        button_wallpapers = gtk.Button("Wallpapers")
        button_screensavers = gtk.Button("Screensavers")
        button_bootsplash = gtk.Button("Bootsplash")
        button_desktop = gtk.Button("Desktop")
        button_doc = gtk.Button("Documentation")
        button_root_password = gtk.Button("Root Passwords")
        
        button_boot.connect("clicked", self.on_button_boot)
        button_machine_name.connect("clicked", self.on_button_machine_name)
        button_menu.connect("clicked", self.on_button_menu)
        button_dialer_theme.connect("clicked", self.on_button_dialer_theme)
        button_home_page.connect("clicked", self.on_button_home_page)
        button_bootloader_theme.connect("clicked", self.on_button_bootloader_theme)
        button_icons.connect("clicked", self.on_button_icons)
        button_wallpapers.connect("clicked", self.on_button_wallpapers)
        button_screensavers.connect("clicked", self.on_button_screensavers)
        button_bootsplash.connect("clicked", self.on_button_bootsplash)
        button_desktop.connect("clicked", self.on_button_desktop)
        button_doc.connect("clicked", self.on_button_doc)
        button_root_password.connect("clicked", self.on_button_root_password)
        
        buttons.pack_start(button_boot, False, False, 0)
        buttons.pack_start(button_machine_name, False, False, 0)
        buttons.pack_start(button_menu, False, False, 0)
        buttons.pack_start(button_dialer_theme, False, False, 0)
        buttons.pack_start(button_home_page, False, False, 0)
        buttons.pack_start(button_bootloader_theme, False, False, 0)
        buttons.pack_start(button_icons, False, False, 0)
        buttons.pack_start(button_wallpapers, False, False, 0)
        buttons.pack_start(button_screensavers, False, False, 0)
        buttons.pack_start(button_bootsplash, False, False, 0)
        buttons.pack_start(button_desktop, False, False, 0)
        buttons.pack_start(button_doc, False, False, 0)
        buttons.pack_start(button_root_password, False, False, 0)

 #       scrolled_window.add_with_viewport(buttons)     
        
        action_panel = gtk.HBox()
        confirm = gtk.Button("Confirm")
        close =  gtk.Button("Close")
        confirm.connect("clicked", self.on_confirm)
        close.connect("clicked", self.on_close)
        action_panel.pack_end(confirm, False, False, 0)
        action_panel.pack_end(close, False, False, 0)
        
        frame_content = gtk.VBox()
#         frame_content.pack_start(scrolled_window, True, True, 0)
        frame_content.pack_start(buttons, True, True, 0)
        frame_content.pack_end(action_panel, False, False, 0)

        frame.add(frame_content)
        return frame
    
    def gui_create_statusbar(self):
        """Create a status bar"""
        statusbar = gtk.Statusbar()
        return statusbar

    def on_confirm(self, widget):
        print widget.get_label()
         
        faults = []
        for key in self.optimizations:
            if not self.optimizations[key]:
                print key
                faults.append(key)
         
        if len(faults) > 0:
            message = 'Os seguintes campos não foram alterados:\n'
            for f in faults:            
                message += '\t' + f + '\n'
            message += '\nTem certeza que deseja prosseguir?'

            dialog = gtk.MessageDialog(message_format=message, buttons=gtk.BUTTONS_OK_CANCEL)
            dialog.add_events(gtk.gdk.KEY_PRESS_MASK)
            response = dialog.run()
            dialog.destroy()
            if response == gtk.RESPONSE_CANCEL:
                return

        dialog = gtk.FileChooserDialog(
            title = "Salvar em ...",
            action = gtk.FILE_CHOOSER_ACTION_SAVE,
            buttons = (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE,gtk.RESPONSE_OK)
        )
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        
        name_tar_ball = ""
        if response == gtk.RESPONSE_CANCEL:
                return
        if response == gtk.RESPONSE_OK:
            name_tar_ball  = dialog.get_filename()
        name_tar_ball = name_tar_ball.replace(" ", "\ ")
        if not name_tar_ball.endswith(".tar.gz"):
            name_tar_ball += ".tar.gz"
        dialog.destroy()

        chroot = "/tmp/chroot" #Warning.. This directory will be removed

        for key in self.optimizations:
            cmd = ""
            if key[-1] == '/':
                cmd = "mkdir -p " + chroot + key
            else:
                cmd = "mkdir -p " + chroot + key.rpartition('/')[0] + '/'
            print cmd
            subprocess.call(cmd, shell=True)
           
        for key in self.optimizations:
            cmd = ""
            if self.optimizations[key]:
                if key[-1] == '/':
                    cmd = "cp -rf " + self.optimizations[key].replace(" ", "\ ") + "/* " + chroot + key
                else:
                    cmd = "cp -rf " + self.optimizations[key].replace(" ", "\ ") + " " + chroot + key
                print cmd
                subprocess.call(cmd, shell=True)

        subprocess.call("tar -czvf " + name_tar_ball + " *", shell=True, cwd=chroot)
#        subprocess.call("mv " + name_tar_ball + " /home/" + os.getenv("USER"), shell=True, cwd=chroot) 
        subprocess.call("rm -rf " + chroot, shell=True)

        message = "Arquivo de otmização gerado com sucesso!\n"
        message += "Salvo em: " + name_tar_ball
        dialog = gtk.MessageDialog(message_format=message, buttons=gtk.BUTTONS_OK)
        dialog.add_events(gtk.gdk.KEY_PRESS_MASK)
        response = dialog.run()
        dialog.destroy()
        
    def on_close(self, widget):
        print widget.get_label()
        gtk.main_quit()

    def select_file(self, widget, key, path, filter):
        if key[-1] == '/':
            action = gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER
        else:
            action = gtk.FILE_CHOOSER_ACTION_OPEN
            
        dialog = gtk.FileChooserDialog(
            title = "Escolher arquivos",
            parent = window,
            action = action,
            buttons = (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK)
        )
        dialog.add_filter(filter)

        dialog.set_default_response(gtk.RESPONSE_OK)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            self.optimizations[key] = dialog.get_filename()
            path.set_text(dialog.get_filename())
            path.show_all()
        elif response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
        dialog.destroy()

    def create_optmizer_frame(self, title, info, pattern, key, value):
        frame = gtk.Frame(title)
        frame.set_border_width(10)
        vbox = gtk.VBox()
        hbox = gtk.HBox()
        info = gtk.Label(info)
        select = gtk.Button('Escolher arquivo')
        path = gtk.Label(self.optimizations[key][value])
        filter = gtk.FileFilter()
        filter.set_name(pattern)
        filter.add_pattern(pattern)
        select.connect('clicked', self.select_file, key, value, path, filter)
        hbox.pack_start(info, True, True, 5)
        hbox.pack_end(select, True, True, 5)
        vbox.pack_start(hbox, False, False, 0)
        vbox.pack_start(path, False, False, 10)
        frame.add(vbox)
        return frame

    def maroto_method_ftw(self, title, list_of_espec = None):

        def destroy(widget):
            window.destroy()

        window = gtk.Window()
        window.set_title(title)
        window.set_default_size(200, 200)
        window.set_modal(True)
        window.connect('destroy', destroy)

        frame = gtk.Frame(title)
        frame.set_border_width(10)
       
        action_panel = gtk.HBox()
        close = gtk.Button("close")
        close.connect("clicked", destroy)
        action_panel.pack_end(close, False, False, 0)
        
        frame_content = gtk.VBox()
        
        for field in list_of_espec:
            field_frame = gtk.Frame(field['key'])
            frame.set_border_width(10)
            vbox = gtk.VBox()
            hbox = gtk.HBox()
            info = gtk.Label(field['info'])
            info.set_justify(gtk.JUSTIFY_LEFT)
            select = gtk.Button('Escolher arquivo')
            select_box = gtk.VButtonBox()
            select_box.pack_start(select)
            path = gtk.Label(self.optimizations[field['key']])
            filter = gtk.FileFilter()
            filter.set_name(field['pattern'])
            if field['pattern'] == 'images':
                filter.add_pattern("*.jpg")
                filter.add_pattern("*.png")
                filter.add_pattern("*.bmp")
            else:
                filter.add_pattern(field['pattern'])

            select.connect('clicked', self.select_file, field['key'], path, filter)
            hbox.pack_start(info, True, True, 5)
            hbox.pack_end(select_box, False, False, 5)
            vbox.pack_start(hbox, False, False, 0)
            vbox.pack_start(path, False, False, 10)
            field_frame.add(vbox)
                
            frame_content.pack_start(field_frame, False, False, 5)

        frame_content.pack_end(action_panel, False, False, 0)
        frame.add(frame_content)

        statusbar = gtk.Statusbar()        

        vbox = gtk.VBox(False, 0)
        vbox.pack_start(frame, True, True, 0)
        vbox.pack_start(statusbar, False, False, 0)
        
        window.add(vbox)
        window.show_all()

    def on_button_boot(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/boot/gfxmenu',
            'info' :  'Arquivo com o splash personalizado\ndo bootloader (grub)',
            'pattern' : 'gfxmenu',
        })
        
        fields.append({
            'key' : '/boot/menu.lst',
            'info' : 'Arquivo de configuração do bootloader\n(avisar a mandriva caso seja alterado)',
            'pattern' : 'menu.lst',
        })

        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_machine_name(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/etc/sysconfig/network',
            'info' : 'Arquivo que contem o nome da maquina.\nPara mudar, altere a variavel HOSTNAME= dentro\ndeste arquivo.',
            'pattern' : 'network',
        })
        self.maroto_method_ftw(widget.get_label(), fields)
        
    def on_button_menu(self, widget):
        print widget.get_label()
        
        fields = []
        fields.append({
            'key' : '/etc/xdg/menus/positivo-applications.menu',
            'info' : 'Arquivo com o xml de descricao dos\naplicativos que aparecem ou nao no menu do kde.',
            'pattern' : 'positivo-applications.menu',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_dialer_theme(self, widget):
        print widget.get_label()
 
        fields = []
        fields.append({
            'key' : '/usr/local/Discador_Lite/data/',
            'info' : 'Diretório que contém os arquivos de personalizacao do\ndiscador da positivo (instalado a parte)\nDeve conter os arquivos:\n\tDiscadorLite.png\n\tcidades2.xml\n\tdialer.cod\n\tdialer.ini\n\tdiscador20.xml\n\tlicenca.txt\n\ttemplate.gif',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_home_page(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/usr/share/doc/HTML/index.html',
            'info' : 'Arquivo html que contem o redirecionamento\nda pagina principal do browser.',
            'pattern' : 'index.html',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_bootloader_theme(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/usr/share/gfxboot/themes/Mandriva-Positivo/',
            'info' : 'Diretório que contem a personalizacao do bootsplash do bootloader.\nDeve conter os arquivos:\n\tback.jpg\n\twallpaper.png\n\twelcome.jpg',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_icons(self, widget):
        print widget.get_label()
        
        fields = []
        fields.append({
            'key' : '/usr/share/icons/',
            'info' : 'Diretório que contém os icones a serem usados no sistema\nArquivos:\n\tATP_128pxls_positivo.png\n\tATP_64pxls_positivo.png\n\tATP_positivo.png\n\tCartao_Suporte_Linux_Sim.png\n\tManual_Positivo.png\n\tcartao_de_suporte.png\n\tdiscador_250 copy.png\n\tmanual_64pxls_positivo.png\n\tmanual_positivo.png',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)
        
    def on_button_wallpapers(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/usr/share/mdk/backgrounds/',
            'info' : 'Diretório que contem os wallpapers do sistema.',
            'pattern' : '*',
        })
        fields.append({
            'key' : '/usr/share/mdk/backgrounds/default.jpg',
            'info' : 'Escolha um wallpaper para ser utilizado\ncomo padrão do sistema.',
            'pattern' : 'images',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_screensavers(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/usr/share/mdk/screensaver/',
            'info' : 'Diretório que contem as imagens\nmostradas pelo screensaver padrao\nda mandriva que exibe fotos.',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_bootsplash(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/usr/share/plymouth/themes/Mandriva-Positivo/',
            'info' : 'Contem os arquivos de configuracao e\ntema para o bootsplash do sistema.',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_desktop(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/var/lib/oem/desktop/',
            'info' : 'Diretório com os arquivos a serem\ncolocados na área de trabalho\ndo usuario.',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_doc(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/var/lib/oem/manual/pdfs/',
            'info' : 'Diretório com a documentação e\nmanuais da positivo.',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

    def on_button_root_password(self, widget):
        print widget.get_label()

        fields = []
        fields.append({
            'key' : '/tmp/rootpwd',
            'info' : 'Arquivo contendo a senha de root do sistema',
            'pattern' : '*',
        })
        self.maroto_method_ftw(widget.get_label(), fields)

if __name__ == "__main__":
    window = Window()
    
    gtk.main()
