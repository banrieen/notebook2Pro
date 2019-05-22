' 将一个表里的很多sheet合并到一个sheet
' 1、在包含多个sheet的工作簿中（如多个工作簿合并后含n个sheet的工作簿），新建一个sheet
' 2、在新建的sheet标签上点击右键，选择“查看代码”（wps的该按钮在开发工具下）
' 3、在打开的VBA编辑窗口中粘贴以下代码：

Sub 合并当前工作簿下的所有工作表()
    Application.ScreenUpdating = False
    For j = 1 To Sheets.Count
        If Sheets(j).Name <> ActiveSheet.Name Then
            X = Range("A65536").End(xlUp).Row + 1
            Sheets(j).UsedRange.Copy Cells(X, 1)
        End If
    Next
    
    'Range("B1").Select
    Application.ScreenUpdating = True
    MsgBox "当前工作簿下的全部工作表已经合并完毕！", vbInformation, "提示"
End Sub

