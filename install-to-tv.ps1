<#
.SYNOPSIS
    סקריפט אוטומטי להתקנת משחקי webOS TV על גבי טלוויזיית LG דרך הרשת.
.DESCRIPTION
    מתקין את חבילות ה-IPK ישירות על גבי הטלוויזיה בעזרת ares-cli או webOS Dev Manager.
.PARAMETER TvIp
    כתובת ה-IP של הטלוויזיה (לדוגמה 192.168.1.XX או הגדרת משתנה סביבה TV_IP)
.PARAMETER Port
    פורט החיבור (9922 למצב מפתח רגיל, 22 לטלוויזיה עם Root)
#>
[CmdletBinding()]
param(
    [string]$TvIp = $env:TV_IP,
    [int]$Port = 9922
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$pkgDir = Join-Path $scriptDir "packages"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  🎮 LG webOS TV - מתקין משחקים אוטומטי" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

if ([string]::IsNullOrWhiteSpace($TvIp)) {
    Write-Host "נא להזין את כתובת ה-IP של הטלוויזיה (לדוגמה: 192.168.X.X):" -ForegroundColor Yellow
    $TvIp = Read-Host "TV IP Address"
    if ([string]::IsNullOrWhiteSpace($TvIp)) {
        Write-Error "לא הוזנה כתובת IP עבור הטלוויזיה. הפעולה בוטלה."
        exit 1
    }
}

Write-Host "כתובת הטלוויזיה: $TvIp`:$Port" -ForegroundColor Gray

$ipks = Get-ChildItem -Path $pkgDir -Filter "*.ipk"
if ($ipks.Count -eq 0) {
    Write-Error "לא נמצאו קבצי IPK בתיקייה $pkgDir"
    exit 1
}

Write-Host "`nנמצאו $($ipks.Count) חבילות משחק להתקנה:" -ForegroundColor Green
$ipks | ForEach-Object { Write-Host " - $($_.Name) ($([math]::Round($_.Length / 1MB, 2)) MB)" -ForegroundColor White }

# בדיקת זמינות חיבור לטלוויזיה
Write-Host "`nבודק חיבור לטלוויזיה בכתובת $TvIp..." -ForegroundColor Cyan
$ping = Test-NetConnection -ComputerName $TvIp -Port $Port -WarningAction SilentlyContinue
if (-not $ping.TcpTestSucceeded) {
    Write-Warning "לא ניתן להתחבר לפורט $Port בכתובת $TvIp."
    Write-Host "אנא ודא ש:" -ForegroundColor Yellow
    Write-Host " 1. הטלוויזיה דולקת ומחוברת לאותה רשת Wi-Fi/כבל."
    Write-Host " 2. אפליקציית Developer Mode פתוחה ו-Dev Mode Status מופעל (ON)."
    Write-Host " 3. Key Server מופעל (ON)."
    Write-Host "`nניתן להתקין בקלות גם דרך ממשק webOS Dev Manager!" -ForegroundColor Cyan
    exit 1
}

Write-Host "חיבור תקין! ✓" -ForegroundColor Green

# בדיקה אם קיים ares-cli במערכת
$hasAres = Get-Command ares-install -ErrorAction SilentlyContinue
if ($hasAres) {
    Write-Host "`nמתקין באמצעות ares-cli..." -ForegroundColor Cyan
    foreach ($ipk in $ipks) {
        Write-Host "מתקין: $($ipk.Name)..." -ForegroundColor Yellow
        & ares-install $ipk.FullName
    }
    Write-Host "`nכל המשחקים הותקנו בהצלחה! תיהנו! 🎮" -ForegroundColor Green
    exit 0
}

Write-Host "`n[מידע] ares-cli אינו מותקן גלובלית." -ForegroundColor Yellow
Write-Host "באפשרותך לפתוח את webOS Dev Manager ולגרור את הקבצים הבאים:" -ForegroundColor Cyan
$ipks | ForEach-Object { Write-Host "  📂 $($_.FullName)" -ForegroundColor White }

Write-Host "`nפתיחת webOS Dev Manager..." -ForegroundColor Gray
$devManagerExe = "C:\Program Files\webOS Dev Manager\webos-dev-manager.exe"
if (Test-Path $devManagerExe) {
    Start-Process $devManagerExe
    Write-Host "webOS Dev Manager הופעל! פשוט גרור את הקבצים לחלון התוכנה." -ForegroundColor Green
}
