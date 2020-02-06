' 对于选定激活的窗口，使用插入的椭圆或矩形框起来
' 颜色默认为黑色

' 椭圆边框
Sub DrawCircle()
    Dim Arng As Range
    Dim WorkRng As Range
    Set WorkRng = Application.Selection
    For Each Arng In WorkRng.Areas
        With Arng
            x = Arng.Height * 0.1
            y = Arng.Width * 0.1
            Application.ActiveSheet.Ovals.Add Top: = .Top - x, Left: = .Left - y, _
            Height: = .Height - 2 * x, Width: = .Width - 1.5 * y
            With Application.ActiveSheet.Ovals(ActiveSheet.Ovals.Count)
                .Interior.ColorIndex = xlNone
                .ShapeRange.Line.Weight = 1.5
                .ShapeRange.Line.ForeColor.RGB = RGB(0 0 255)
            End With
        End With
    Next
    WorkRng.Select
End Sub

' 参考链接： https://www.extendoffice.com/documents/excel/2231-excel-circle-around-cell.html
'           https://exceloffthegrid.com/add-rectangles-around-cells/

' 矩形边框
Sub add_shape()
    Dim redBox As Shape
    Dim selectedAreas As Range
    Dim i As Integer
    Dim tempShape As Shape
    'Loop through each selected area in active sheet
    For Each selectedAreas In Selection.Areas
        'Create a rectangle
        Set redBox = ActiveSheet.Shapes.AddShape(msoShapeRectangle, _
            selectedAreas.Left, selectedAreas.Top, _
            selectedAreas.Width, selectedAreas.Height)
        'Change attributes of shape created
        redBox.Line.ForeColor.RGB = RGB(0, 0, 255)
        redBox.Line.Weight = 1.5
        redBox.Fill.Visible = msoFalse
        'Loop to find a unique shape name
    Next

End Sub
