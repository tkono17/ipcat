#------------------------------------------------------------------------
# ipcat: gui.py
# -------------
# - menuBar: ttk.Menubar
# - mainPanel: ttk.Panedwindow
#   - listPanel: ttk.Frame
#     - imageTree: ttk.Treeview
#   - workPanel: ttk.Panedwindow
#     - imagePanel: ttk.Frame
#     - analysisPanel: AnalysisPanel
#   - outputPanel: ttk.Panedwindow
#     - galleryPanel: ttk.Frame
#     - messagePanel: ttk.Text
#------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from .guiComponents import *
from .vmodel import ViewModel
from .handlers import Handlers, openImage
from .analysis import *
import logging

logger = logging.getLogger(__name__)

def initTk():
    root = tk.Tk()
    root.title('Image Processing Square')
    root.geometry('1000x600')
    root.minsize(width=500, height=400)
    return root

#------------------------------------------------------------------------
# MainWindow
#------------------------------------------------------------------------
class MainWindow(ttk.Frame):
    def __init__(self, root):
        self.root = root
        self.setStyle()
        super().__init__(root, width=1000, height=600, style='main.TFrame')
        #
        self.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.handlers = Handlers()
        self.vmodel = ViewModel()
        #
        #
        self.menuBar = None
        # Left
        self.imageTree = None
        # Middle
        self.imagePanel = None
        self.analysisPanel = None
        # Right
        self.galleryPanel = None
        self.messagePanel = None

        self.buildGui()

    def setStyle(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='darkgreen')
        style.configure('main.TFrame', background='blue')
        style.configure('panel.TFrame', background=(32, 32, 190))
        style.configure('TButton', background=(32, 32, 190))
        pass
    
    def buildGui(self):
        self.buildMenu()
        #
        columns = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        columns.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        listPanel = ttk.Frame(columns)
        workPanel = ttk.Panedwindow(columns, orient=tk.VERTICAL)
        outputPanel = ttk.Panedwindow(columns, orient=tk.VERTICAL)
        listPanel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        workPanel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        outputPanel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        columns.add(listPanel, weight=1)
        columns.add(workPanel, weight=3)
        columns.add(outputPanel, weight=2)
        #
        self.buildListPanel(listPanel)
        self.buildWorkPanel(workPanel)
        self.buildOutputPanel(outputPanel)
        
    def buildMenu(self):
        menuBar = tk.Menu(self)
        self.root.config(menu=menuBar)
        file_menu = tk.Menu(menuBar)
        menuBar.add_cascade(label='File', menu=file_menu, underline=0)
        file_menu.add_command(label='Quit', command=self.cleanup)

    def buildListPanel(self, parent):
        tree = ttk.Treeview(parent)
        tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    def buildWorkPanel(self, parent):
        imagePanel = ttk.Frame(parent)
        imagePanel.pack(side=tk.TOP, fill=tk.X, expand=True)
        analysisPanel = AnalysisPanel(parent)
        analysisPanel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        parent.add(imagePanel, weight=3)
        parent.add(analysisPanel, weight=2)
        
    def buildOutputPanel(self, parent):
        galleryPanel = ttk.Frame(parent)
        galleryPanel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        messagePanel = tk.Text(parent)
        messagePanel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        parent.add(galleryPanel, weight=3)
        parent.add(messagePanel, weight=1)
        pass
    
    def cleanup(self):
        logger.info('Quit gui')
        