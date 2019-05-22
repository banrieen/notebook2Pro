VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisWorkbook"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub DrawCircle()
    'Updateby20141105
    Dim Arng As Range
    Dim WorkRng As Range
    Set WorkRng = Application.Selection
    For Each Arng In WorkRng.Areas
        With Arng
            x = Arng.Height * 0.1
            y = Arng.Width * 0.1
            Application.ActiveSheet.Ovals.Add Top:=.Top - x, Left:=.Left - y, _
            Height:=.Height + 2 * x, Width:=.Width + 1.5 * y
            With Application.ActiveSheet.Ovals(ActiveSheet.Ovals.Count)
                .Interior.ColorIndex = xlNone
                .ShapeRange.Line.Weight = 1.25
                .ShapeRange.Line.ForeColor.RGB = RGB(0, 0, 0)
            End With
        End With
    Next
    WorkRng.Select
End Sub

