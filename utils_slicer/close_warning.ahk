#Persistent
SetTimer, CloseVTK, 1000
return

CloseVTK:
IfWinExist, Error
{
    WinClose, Error
}
return
