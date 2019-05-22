'用vba将多个工作表另存为独立的工作簿文件
'当用鼠标右键单击工作表名称标签，在弹出的快捷菜单中选择“移动或者复制”命令，在弹出的“移动或者复制工作表”对话框中可以选择将工作表移动到当前工作簿中的任意一个工作表的位置之前或之后，也可以将工作表移动到一个新的空白工作簿。
'在vba中，Worksheet对象的Copy方法可以实现以上的功能。它的语法如下：
'expression . Copy( Before , After )
'其中 Before 和After参数表示要插在哪个工作表之前或者之后，如果都不提供的话，则表示移动到一个空白的新的工作簿。
'以下是一个通用的将当前工作簿除了活动工作表以外的所有工作表另存为独立的工作簿文件的代码：

Sub save_sheets_as_single_book()
    Dim oWK As Worksheet
    Dim oWB As Workbook
    Dim sPath As String
    If MsgBox("现在开始将把各sheet独立另存为book文件，请再次检查格式数据是否正确？", vbYesNo, "重要提示") = vbYes Then
        sPath = Excel.ThisWorkbook.Path
        sName = Excel.Application.ActiveSheet.Name
        Excel.Application.DisplayAlerts = False
        For Each oWK In Excel.ThisWorkbook.Worksheets
            With oWK
                If .Name <> sName Then
                    .Copy
                    Set oWB = Excel.Application.ActiveWorkbook
                    oWB.SaveAs sPath & "\" & .Name, xlOpenXMLWorkbook
                    oWB.Close
                End If
            End With
        Next
        Excel.Application.DisplayAlerts = True
    End If
End Sub
