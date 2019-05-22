' 不同表合并到一个有很多sheet的表里
' 
' 1、新建一个工作薄，将其命名为你合并后的名字。
' 2、打开此工作薄。
' 3、在其下任一个工作表标签上点击右键，选择“查看代码”。（wps的该按钮在开发工具下）
' 4、在打开的VBA编辑窗口中粘贴以下代码：

Sub 工作薄间工作表合并()
    Dim FileOpen
    Dim X As Integer
    Application.ScreenUpdating = False
    FileOpen = Application.GetOpenFilename(FileFilter:="所有 Excel文件(*.xlsx;*.xls;*.xlsm),*.xls", MultiSelect:=True, Title:="合并工作薄")
    X = 1
    While X <= UBound(FileOpen)
        Workbooks.Open Filename:=FileOpen(X)
        Sheets().Move After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count)
        X = X + 1
    Wend

    ExitHandler:
        Application.ScreenUpdating = True
    Exit Sub

errhadler:
    MsgBox Err.Description
End Sub

Sub 工作薄间工作表合并()
    Dim FileOpen
    Dim X As Integer
    Application.ScreenUpdating = False
    ' 事先不过滤文件类型
    FileOpen = Application.GetOpenFilename(FileFilter:="", MultiSelect:=True, Title:="合并工作薄")
    X = 1
    While X <= UBound(FileOpen)
        Workbooks.Open Filename:=FileOpen(X)
        Sheets().Move After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count)
        X = X + 1
    Wend

    ExitHandler:
        Application.ScreenUpdating = True
    Exit Sub

errhadler:
    MsgBox Err.Description
End Sub

