' 在指定范围内的单元格如果时空的，则删除该行；
' 非空行则上移

' Sub delete_null()
' 
' For i = 23 To 9 Step -1
'     If Cells(i, 5) = "" Then
'         Rows(i).Select
'         Selection.Delete Shift:=xlUp
'     End If
' Next i
' End Sub

Sub delete_null()
    Dim xlBook As Excel.Workbook
    Dim xlSheet As Excel.Worksheet
    Set xlBook = ThisWorkbook
    'Range start from 4st sheet
    For x = 1 To xlBook.Sheets.Count
        Set xlSheet = xlBook.Sheets(x)
        xlSheet.Select
        For I = 23 To 9 Step -1
            If Cells(I, 5) = "" Then
                Rows(I).Select
                Selection.Delete Shift:=xlUp
            End If
        Next I
    Next x
End Sub

