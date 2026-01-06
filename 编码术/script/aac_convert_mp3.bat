@echo off
for %%a in (*.aac) do (
    ffmpeg -i "%%a" "%%~na.mp3"
)
pause
