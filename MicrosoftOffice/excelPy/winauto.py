""" Windows Application Control
#   pywinauto connect application
#   Get the specify table cell
"""

# from subprocess import Popen
from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto import Desktop
from pywinauto import timings


timings.Timings.slow()

def start_MSUI_application(system_app_name='calc.exe'):

    # Application().start('explorer.exe "C:\\Program Files"')
    Application().start(system_app_name)
    # connect to another process spawned by explorer.exe
    # Note: make sure the script is running as Administrator!
    app = Application(backend="uia").connect(path=system_app_name, title="计算器")

    app.ProgramFiles.set_focus()
    common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
    common_files.right_click_input()
    app.ContextMenu.Properties.invoke()

    # this dialog is open in another process (Desktop object doesn't rely on any process id)
    Properties = Desktop(backend='uia').Common_Files_Properties
    Properties.print_control_identifiers()
    Properties.Cancel.click()
    Properties.wait_not('visible') # make sure the dialog is closed

def start_simple_application(appName="notepad.exe"):
    app = Application().start(appName)
    dlg_spec = app.UntitledNotepad
    dlg = app['无标题 - 记事本']
    app['无标题 - 记事本'].Edit.type_keys("pywinauto Works!", with_spaces = True)
    # dlg.Edit.type_keys("pywinauto Works!", with_spaces = True)
    # window = WindowSpecification("无标题 - 记事本")
    # windows.wait("active")
    # actionable_dlg = dlg_spec.wait('active',6,2)
    return app

def assert_application(app, appInfo=""):
    # app.UntitledNotepad.menu_select("Help->About Notepad")
    app.UntitledNotepad.menu_select(appInfo)
    # Click on a button
    app['关于"记事本"']["确定"].click()
    # app['无标题 - 记事本']["关闭"].click()
    dlg = app.window(title='无标题 - 记事本')
    # dlg.minimize() 
    # dlg.close()
    dlg.menu_select("文件 -> 退出")
    # app.kill(soft=True)
    dlg_close = app['记事本']
    # app['记事本']["不保存"].click()
    # dlg_close["不保存"].click()
    dlg_close["保存"].click()
    dlg_save = app["另存为"]
    dlg_save["文件名"].Edit.type_keys("pywinautoWorks.txt", with_spaces = False)
    dlg_save["保存"]
    
def import_data_target_cell(app, datas, cell):
    # Type a text string
    app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)


if __name__ == "__main__":
    app = start_simple_application()
    assert_application(app,'帮助->关于记事本')
