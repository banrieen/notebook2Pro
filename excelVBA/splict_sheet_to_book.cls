' excel将一个工作表根据条件拆分成多个工作簿、工作表
' 出现运行错误'3706'，可将连接方式，改用DSN连接：conn.Open "Dsn=Excel Files;DBQ=" & ThisWorkbook.FullName

Sub CFGZB()
 
    Dim myRange As Variant
 
    Dim myArray
 
    Dim titleRange As Range
 
    Dim title As String
 
    Dim columnNum As Integer
 
 
 
    myRange = Application.InputBox(prompt:="请选择标题行：", Type:=8)
 
    myArray = WorksheetFunction.Transpose(myRange)
 
 
 
    Set titleRange = Application.InputBox(prompt:="请选择拆分的表头，必须是第一行，且为一个单元格，如：“姓名”", Type:=8)
 
    title = titleRange.Value
 
    columnNum = titleRange.Column
 
    Application.ScreenUpdating = False
 
    Application.DisplayAlerts = False
 
    Dim i&, Myr&, Arr, num&
 
    Dim d, k
 
    For i = Sheets.Count To 1 Step -1
 
        If Sheets(i).Name <> "数据源" Then
 
            Sheets(i).Delete
 
        End If
 
    Next i
 
    Set d = CreateObject("Scripting.Dictionary")
 
    Myr = Worksheets("数据源").UsedRange.Rows.Count
 
    Arr = Worksheets("数据源").Range(Cells(2, columnNum), Cells(Myr, columnNum))
 
    For i = 1 To UBound(Arr)
 
        d(Arr(i, 1)) = ""
 
    Next
 
    k = d.keys
 
    For i = 0 To UBound(k) 
 
        Set conn = CreateObject("adodb.connection")
 
        ' conn.Open "provider=microsoft.jet.oledb.4.0;extended properties=excel 8.0;data source=" & ThisWorkbook.FullName
        conn.Open "Dsn=Excel Files;DBQ=" & ThisWorkbook.FullName
        Sql = "select * from [数据源$] where " & title & " = '" & k(i) & "'"
 
        Dim Nowbook As Workbook
 
        Set Nowbook = Workbooks.Add
 
        With Nowbook
 
            With .Sheets(1)
 
                .Name = k(i)
 
                For num = 1 To UBound(myArray)
 
                    .Cells(1, num) = myArray(num, 1)
 
                Next num
 
                .Range("A2").CopyFromRecordset conn.Execute(Sql)
 
            End With
 
        End With
 
 
 
        ThisWorkbook.Activate
 
        Sheets(1).Cells.Select
 
        Selection.Copy
 
        Workbooks(Nowbook.Name).Activate
 
        ActiveSheet.Cells.Select
 
        Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
 
        Application.CutCopyMode = False
 
        Nowbook.SaveAs ThisWorkbook.Path & "\" & k(i)
 
        Nowbook.Close True
 
        Set Nowbook = Nothing
 
    Next i
 
    conn.Close
 
    Set conn = Nothing
 
    Application.DisplayAlerts = True
 
    Application.ScreenUpdating = True
 
End Sub