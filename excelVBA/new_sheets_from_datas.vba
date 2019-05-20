
Private Sub CommandButton1_Click()
Dim a As Long, b As Long, c As Long
Dim i As Integer, j As Integer, k As Integer
Dim x As Integer, y As Integer, z As Integer

Dim PoNum As String, fileP As String, NewFile As String, DateNo As String
Dim Ks As Integer, Js As Integer
Dim Kss As Integer, Jss As Integer, tp As Integer

Dim HyNum As Integer
Dim Hyf As Integer

Dim Arr

Arr = Sheets("A").UsedRange
a = Sheets("A").UsedRange.Rows.Count

Ks = 0: Js = 0: HyNum = 0
PoNum = ""

fileP = ThisWorkbook.Path
fileP = fileP & "\模板.xls"

If Len(Dir(fileP)) < 1 Then
    MsgBox "模板不存在，请确认！"
    Exit Sub
End If
For b = 2 To a
    If HyNum > 0 Then
        
        If PoNum <> Arr(b, 1) Then ' if not same
mkfile:
            If HyNum > 10 Then
            
                If HyNum Mod 10 <> 0 Then
                    Hyf = HyNum \ 10 + 1
                Else
                    Hyf = HyNum \ 10
                End If
                
                For i = 1 To Hyf
                    
                    Application.ScreenUpdating = False
                    
                    Application.Workbooks.Open (fileP)
                    Application.ScreenUpdating = False
'                    xx = Workbooks("模板.xls").Name
                    Workbooks("模板.xls").Activate
                    Workbooks("模板.xls").Sheets("模块").Select
                    
                    NewFile = PoNum & "(" & i & ")" & ".xls"
                    
                    ActiveSheet.Name = PoNum
                
                    With ActiveSheet
                    .Cells(5, 20) = "数据编号：" & PoNum
                    .Cells(7, 20) = "日期：" & DateNo
                    
                        If Ks + i * 10 < Js Then
                            Kss = Ks + (i - 1) * 10
                            Jss = Ks + i * 10 - 1

                            x = 9
                            For j = Kss To Jss

                                .Cells(x, 1) = x - 8
                                .Cells(x, 2) = Arr(j, 3)
                                .Cells(x, 5) = Arr(j, 4)
                                .Cells(x, 6) = Arr(j, 5)
                                .Cells(x, 10) = Arr(j, 6)
                                .Cells(x, 14) = Arr(j, 7)
                                .Cells(x, 16) = Arr(j, 8)
                                .Cells(x, 18) = Arr(j, 9)
                                .Cells(x, 20) = Arr(j, 10)
                                .Cells(x, 22) = Arr(j, 11)
                                .Cells(x, 24) = Arr(j, 12)
                                .Cells(x, 25) = Arr(j, 13)
                                .Cells(x, 26) = Arr(j, 14)
                                x = x + 1
                            Next j
                                                    
                        Else
                            
                            Kss = Ks + (i - 1) * 10
                            Jss = Js
                            tp = Jss - Kss + 9
                            
                            x = 9
                            For j = Kss To Jss
                                
                                .Cells(x, 1) = x - 8
                                .Cells(x, 2) = Arr(j, 3)
                                .Cells(x, 5) = Arr(j, 4)
                                .Cells(x, 6) = Arr(j, 5)
                                .Cells(x, 10) = Arr(j, 6)
                                .Cells(x, 12) = Arr(j, 7)
                                .Cells(x, 14) = Arr(j, 8)
                                .Cells(x, 16) = Arr(j, 9)
                                .Cells(x, 18) = Arr(j, 10)
                                .Cells(x, 20) = Arr(j, 11)
                                .Cells(x, 22) = Arr(j, 12)
                                .Cells(x, 23) = Arr(j, 13)
                                .Cells(x, 24) = Arr(j, 14)
                                x = x + 1
                            
                            Next j
                            
                        End If
                    
                    End With
                    Workbooks("模板.xls").SaveAs Filename:=ThisWorkbook.Path & "\New\" & NewFile
                    Workbooks(NewFile).Close
                    
                    Application.ScreenUpdating = True
                
                Next i
                
            Else
mkafile:
                Application.ScreenUpdating = False
                
                Application.Workbooks.Open (fileP)
                Application.ScreenUpdating = False
                Workbooks("模板.xls").Activate
                Workbooks("模板.xls").Sheets("模块").Select
                
                NewFile = PoNum & ".xls"
                
                ActiveSheet.Name = PoNum
                
                With ActiveSheet
                .Cells(5, 20) = "数据编号：" & PoNum
                .Cells(7, 20) = "日期：" & DateNo
                
                tp = Js - Ks + 9
                
                x = 9
                For j = Ks To Js
                    
                    .Cells(x, 1) = x - 8
                    .Cells(x, 2) = Arr(j, 3)
                    .Cells(x, 5) = Arr(j, 4)
                    .Cells(x, 6) = Arr(j, 5)
                    .Cells(x, 10) = Arr(j, 6)
                    .Cells(x, 12) = Arr(j, 7)
                    .Cells(x, 14) = Arr(j, 8)
                    .Cells(x, 16) = Arr(j, 9)
                    .Cells(x, 18) = Arr(j, 10)
                    .Cells(x, 20) = Arr(j, 11)
                    .Cells(x, 22) = Arr(j, 12)
                    .Cells(x, 23) = Arr(j, 13)
                    .Cells(x, 24) = Arr(j, 14)
                    x = x + 1
                
                Next j
                    
                End With
                
                Workbooks("模板.xls").SaveAs Filename:=ThisWorkbook.Path & "\New\" & NewFile
                Workbooks(NewFile).Close
                
                Application.ScreenUpdating = True
                
                If b > a Then GoTo byy
                
                    
            End If
                      
            
            PoNum = Arr(b, 1)
            DateNo = Arr(b, 2)
            HyNum = 1
            Ks = b
            Js = b
            
            If b + 1 > a Then GoTo mkafile
        
        Else 'same
            HyNum = HyNum + 1
            Js = b
            If b + 1 > a Then GoTo mkfile
        End If
        
    Else
    
        PoNum = Arr(b, 1)
        DateNo = Arr(b, 2)
        HyNum = 1
        Ks = b
        Js = b
        
        If b + 1 > a Then GoTo mkafile
    
    End If
    
Next b

byy:

MsgBox "OK"

End Sub
