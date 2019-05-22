' 使用正则表达式提取单元格中的数字
'

Sub Test()
    Application.ScreenUpdating = False
    Application.Cursor = xlWait
   
    Dim lngRows As Long, lngR As Long
    Dim strTemp As String
    Dim strR As Variant
   
    lngRows = Sheet1.Range("A" & Rows.Count).End(xlUp).Row
   
    For lngR = 2 To lngRows
        strTemp = Sheet1.Range("A" & lngR).Value2
        strR = GetDigit(strTemp)
        If IsEmpty(strR) = False Then Sheet1.Range("B" & lngR).Resize(1, UBound(strR)) = strR
    Next
   
    Application.ScreenUpdating = True
    Application.Cursor = xlDefault
End Sub

Function GetDigit(strValue As String) As Variant
    Dim objReg As Object
    Dim objMatchs As Object, objMatch As Object
    Dim strPat As String
    Dim strResult() As String  '字符型String可以得到[00001],如果想直接得到数字，可以定义为长整型Long
    Dim intIndex As Integer
   
    strPat = "\d+\.*\d*"
   
    Set objReg = CreateObject("VBScript.RegExp")
    With objReg
        .Global = True
        .Pattern = strPat
        Set objMatchs = .Execute(strValue)
        intIndex = objMatchs.Count
        If intIndex > 0 Then
            ReDim strResult(1 To objMatchs.Count)
            intIndex = 0
            For Each objMatch In objMatchs
                   intIndex = intIndex + 1
                   strResult(intIndex) = objMatch
            Next
            GetDigit = strResult
        End If
    End With
   
End Function