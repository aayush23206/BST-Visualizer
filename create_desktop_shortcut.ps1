$DesktopPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath("Desktop"), "BST Visualizer.lnk")
$TargetPath = "c:\Users\Aayush\OneDrive\Desktop\BST Visualizer2.0\run_bst.bat"
$WorkingDirectory = "c:\Users\Aayush\OneDrive\Desktop\BST Visualizer2.0"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($DesktopPath)
$Shortcut.TargetPath = $TargetPath
$Shortcut.WorkingDirectory = $WorkingDirectory
$Shortcut.Description = "Binary Search Tree Visualizer"
$Shortcut.IconLocation = "c:\Windows\System32\imageres.dll,1"
$Shortcut.Save()

Write-Host "Desktop shortcut created successfully at: $DesktopPath"
