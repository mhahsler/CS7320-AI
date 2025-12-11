# Batch convert all .ppt/.pptx files encountered in folder and all its subfolders
# The produced PDF files are stored in the invocation folder
#
# If PowerShell exits with an error, check if unsigned scripts are allowed in your system.
# You can allow them by calling PowerShell as an Administrator and typing
# ```
# Set-ExecutionPolicy Unrestricted
# ```
# Get invocation path
$folderPath = Split-Path -parent $MyInvocation.MyCommand.Path

# Define the PDF save format constant
$ppSaveAsPDF = 32 # This constant value represents the PDF format in the PowerPoint interop library

# Create a PowerPoint application object
$pptApp = New-Object -ComObject PowerPoint.Application

# Make the application invisible during the process
#$pptApp.Visible = [Microsoft.Office.Core.MsoTriState]::msoFalse

# Get all PowerPoint files (.pptx) in the specified folder
Get-ChildItem -Path $folderPath -Filter "*.pptx" -File | ForEach-Object {
    $pptxFile = $_
    $pdfPath = Join-Path -Path $pptxFile.DirectoryName -ChildPath ($pptxFile.BaseName + ".pdf")

    # Check if conversion is needed:
    # 1. If the PDF does not exist (!Test-Path)
    # 2. OR if the PowerPoint file is newer ($pptxFile.LastWriteTime -gt $pdfFile.LastWriteTime)
    if (-not (Test-Path -Path $pdfPath) -or ($pptxFile.LastWriteTime -gt (Get-Item -Path $pdfPath).LastWriteTime)) {
        Write-Host "Converting $($pptxFile.Name) to PDF..."

        # Open the PowerPoint presentation
        $presentation = $pptApp.Presentations.Open($pptxFile.FullName)

        # Save the presentation as a PDF
        $presentation.SaveAs($pdfPath, $ppSaveAsPDF)

        # Close the presentation
        $presentation.Close()
        Write-Host "Successfully saved to $pdfPath"
    } else {
        Write-Host "$($pptxFile.Name) is already up to date. Skipping conversion."
    }
}

# Quit PowerPoint application and release the COM object
$pptApp.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($pptApp)
Remove-Variable pptApp
[GC]::Collect()
[GC]::WaitForPendingFinalizers()

Write-Host "Conversion process finished."

