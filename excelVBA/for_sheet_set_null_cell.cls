' 打卡一个Excel 工作簿（workbook），循环判断其中的每个表（book）
' 如果指定位置的cell为空，则输入 'hhhh' 并退出该表。
' 依次循环设置完工作簿中所有的表

Sub for_set_null_cell()
    'Dim xlApp As Excel.Application
    Dim xlBook As Excel.Workbook
    Dim xlSheet As Excel.Worksheet
    Set xlBook = ThisWorkbook
    'Range start from 4st sheet
    For x = 4 To xlBook.Sheets.Count
        Set xlSheet = xlBook.Sheets(x)
        Dim R As Range
        For Each R In xlSheet.Range("B2:B6")
            If R = "" Then R = "hhhh": Exit For
        Next R
    Next x
End Sub

