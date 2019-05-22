Sub cell_format()
    Dim sht As Worksheet
    Dim rng As Range
    
    Set sht = Worksheets("Sheet1")
    Set rng = sht.Range("A1:H1")
    
    ' 设置边框格式
    ' 这是常规的实线、细线，默认颜色为黑色
    rng.Borders.LineStyle = xlContinuous
    '取消边框线
    'Range("A1:B11").Borders.LineStyle=0
    'rng.Borders.LineStyle = 0
    'sht.Range("A2:A2").Borders.LineStyle = 0

    End Sub


