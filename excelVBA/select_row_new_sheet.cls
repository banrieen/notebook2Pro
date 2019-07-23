' 填制凭证
' 单元格数据格式设置
'Sub s()
'    [a1].NumberFormatLocal = "@" '设置A1单元格为文本格式
'    [b1].NumberFormatLocal = "yyyy/m/d" '设置B1单元格为日期格式
'    [c1].NumberFormatLocal = "[$-F400]h:mm:ss AM/PM" '设置C1单元格为时间格式
'    [d1].NumberFormatLocal = "0.00%" '设置D1单元格为百分比格式
'    [e1].NumberFormatLocal = "0.00E+00" '设置E1单元格为科学记数法格式
'    [f1].NumberFormatLocal = "G/通用格式" '设置F1单元格为常规格式
'End Sub
'EXCEL用VBA提取字符串:
'mid(源字串，起始位号x，提取长度m)；返回第x位起m个字符。要求：起始位号+提取长度<=源字串长度+1
'left(源字串，左侧截取长度x)；返回左侧x个字符
'right(源字串，右侧截取长度y)；返回右侧y个字符
'instr(源字串，待查找子字串u)；返回子字串首字符在源字串中的起始位号
'chr(65)；返回字母A




Sub 资产1_Click()
    Application.ScreenUpdating = False
    'ThisWorkbook.Sheets("Sheet1").Activate
    Dim flag As Integer
    Dim length As Integer
    For j = 4 To Cells(Rows.Count, 1).End(3).Row
    On Error GoTo Errorcatch
        If Sheets(1).Cells(j, 23) <> Sheets(1).Cells(j - 1, 23) Then
            b = 1

            Sheets(2).Copy after:=Sheets(2)
            Set sh = Sheets(3)
            flag = InStr(Sheets(1).Cells(j, 3), "/")
            length = len(Sheets(1).Cells(j, 3))
            If flag = 0 Then
                sh.Name = Left(Sheets(1).Cells(j, 3)
            else
                sh.Name = Left(Sheets(1).Cells(j, 3), flag - 1) & "-" &right(Sheets(1).Cells(j, 3),length-flag)
            End If
            'MsgBox Left(Sheets(1).Cells(j, 3), flag - 1) & "-" & Str(Int((1000 * Rnd) + 1))
            'sh.Name = Left(Sheets(1).Cells(j, 3), flag - 1) & "-" & Str(Int((1000 * Rnd) + 1))
            
            sh.[G11] = Sheets(1).Cells(j, 2)
            sh.[I11] = Sheets(1).Cells(j, 3)
            sh.[G12] = Sheets(1).Cells(j, 4)
            sh.[G13] = Sheets(1).Cells(j, 5)
            sh.[G14] = Sheets(1).Cells(j, 10)
            sh.[G16] = Sheets(1).Cells(j, 6)
             
            
        End If
        Application.Wait (Now + TimeValue("00:00:01"))
    Next j
    MsgBox "Sheet 总计："+str(ThisWorkbook.Worksheets.Count) + " 新生成的sheet踪迹：" + str(j-4)
    Errorcatch:
    MsgBox Err.Description
    Application.ScreenUpdating = True
   
End Sub
   

Sub 生成10合一表_Click()
    Application.ScreenUpdating = False
    Dim flag As Integer
    Dim length As Integer
    Dim dir As Integer
    Dim i As Integer
    Dim tmpSheet As Worksheet
    For j = 4 To Cells(Rows.Count, 1).End(3).Row
        'On Error GoTo Errorcatch
        i = j - 4
        If i Mod 10 = 0 Then
            Sheets(3).Copy after:=Sheets(3)
            Set tmpSheet = Sheets(4)
            'tmpSheet.Select
            
            flag = InStr(Sheets(1).Cells(j, 3), "/")
            length = Len(Sheets(1).Cells(j, 3))
            
            If flag = 0 Then
                tmpSheet.Name = Sheets(1).Cells(j, 3)
            Else
                tmpSheet.Name = Left(Sheets(1).Cells(j, 3), flag - 1) & "-" & Right(Sheets(1).Cells(j, 3), length - flag)
            End If
            
            tmpSheet.[G11] = Sheets(1).Cells(j, 2)
            tmpSheet.[I11] = Sheets(1).Cells(j, 3)
            tmpSheet.[G12] = Sheets(1).Cells(j, 4)
            tmpSheet.[G13] = Sheets(1).Cells(j, 5)
            tmpSheet.[G14] = Sheets(1).Cells(j, 10)
            tmpSheet.[G16] = Sheets(1).Cells(j, 6)
            
        ElseIf i Mod 10 = 1 Then
            tmpSheet.[G20] = Sheets(1).Cells(j, 2)
            tmpSheet.[I20] = Sheets(1).Cells(j, 3)
            tmpSheet.[G21] = Sheets(1).Cells(j, 4)
            tmpSheet.[G22] = Sheets(1).Cells(j, 5)
            tmpSheet.[G23] = Sheets(1).Cells(j, 10)
            tmpSheet.[G25] = Sheets(1).Cells(j, 6)
       ElseIf i Mod 10 = 2 Then
            tmpSheet.[G29] = Sheets(1).Cells(j, 2)
            tmpSheet.[I29] = Sheets(1).Cells(j, 3)
            tmpSheet.[G30] = Sheets(1).Cells(j, 4)
            tmpSheet.[G31] = Sheets(1).Cells(j, 5)
            tmpSheet.[G32] = Sheets(1).Cells(j, 10)
            tmpSheet.[G34] = Sheets(1).Cells(j, 6)
       ElseIf i Mod 10 = 3 Then
            tmpSheet.[G38] = Sheets(1).Cells(j, 2)
            tmpSheet.[I38] = Sheets(1).Cells(j, 3)
            tmpSheet.[G39] = Sheets(1).Cells(j, 4)
            tmpSheet.[G40] = Sheets(1).Cells(j, 5)
            tmpSheet.[G41] = Sheets(1).Cells(j, 10)
            tmpSheet.[G43] = Sheets(1).Cells(j, 6)
       ElseIf i Mod 10 = 4 Then
            tmpSheet.[G47] = Sheets(1).Cells(j, 2)
            tmpSheet.[I47] = Sheets(1).Cells(j, 3)
            tmpSheet.[G48] = Sheets(1).Cells(j, 4)
            tmpSheet.[G49] = Sheets(1).Cells(j, 5)
            tmpSheet.[G50] = Sheets(1).Cells(j, 10)
            tmpSheet.[G52] = Sheets(1).Cells(j, 6)
       ElseIf i Mod 10 = 5 Then
            tmpSheet.[L11] = Sheets(1).Cells(j, 2)
            tmpSheet.[N11] = Sheets(1).Cells(j, 3)
            tmpSheet.[L12] = Sheets(1).Cells(j, 4)
            tmpSheet.[L13] = Sheets(1).Cells(j, 5)
            tmpSheet.[L14] = Sheets(1).Cells(j, 10)
            tmpSheet.[L16] = Sheets(1).Cells(j, 6)
       ElseIf i Mod 10 = 6 Then
            tmpSheet.[L20] = Sheets(1).Cells(j, 2)
            tmpSheet.[N20] = Sheets(1).Cells(j, 3)
            tmpSheet.[L21] = Sheets(1).Cells(j, 4)
            tmpSheet.[L22] = Sheets(1).Cells(j, 5)
            tmpSheet.[L23] = Sheets(1).Cells(j, 10)
            tmpSheet.[L25] = Sheets(1).Cells(j, 6)
      ElseIf i Mod 10 = 7 Then
            tmpSheet.[L29] = Sheets(1).Cells(j, 2)
            tmpSheet.[N29] = Sheets(1).Cells(j, 3)
            tmpSheet.[L30] = Sheets(1).Cells(j, 4)
            tmpSheet.[L31] = Sheets(1).Cells(j, 5)
            tmpSheet.[L32] = Sheets(1).Cells(j, 10)
            tmpSheet.[L34] = Sheets(1).Cells(j, 6)
      ElseIf i Mod 10 = 8 Then
            tmpSheet.[L38] = Sheets(1).Cells(j, 2)
            tmpSheet.[N38] = Sheets(1).Cells(j, 3)
            tmpSheet.[L39] = Sheets(1).Cells(j, 4)
            tmpSheet.[L40] = Sheets(1).Cells(j, 5)
            tmpSheet.[L41] = Sheets(1).Cells(j, 10)
            tmpSheet.[L43] = Sheets(1).Cells(j, 6)
      ElseIf i Mod 10 = 9 Then
            'dir = (9 - 5) * 9
            tmpSheet.[L47] = Sheets(1).Cells(j, 2)
            tmpSheet.[N47] = Sheets(1).Cells(j, 3)
            tmpSheet.[L48] = Sheets(1).Cells(j, 4)
            tmpSheet.[L49] = Sheets(1).Cells(j, 5)
            tmpSheet.[L50] = Sheets(1).Cells(j, 10)
            tmpSheet.[L52] = Sheets(1).Cells(j, 6)
      Else
          MsgBox "Sheet1 Datas Error !" + Str(j - 4 Mod 10)
      End If
    
    Next j
MsgBox "Sheets ×Ü¼Æ£º" + Str(ThisWorkbook.Worksheets.Count)
'Errorcatch:
'    MsgBox Err.Description
Application.ScreenUpdating = True
End Sub