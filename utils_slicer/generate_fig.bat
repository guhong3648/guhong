@echo off
start "" "C:\Program Files\AutoHotkey\AutoHotkey.exe" "C:\Users\amilab\AppData\Local\slicer.org\Slicer 5.5.0-2023-10-09\utils\close_warning.ahk"
set slicer=C:\Users\amilab\AppData\Local\slicer.org\Slicer 5.5.0-2023-10-09\Slicer.exe
set script=C:\Users\amilab\AppData\Local\slicer.org\Slicer 5.5.0-2023-10-09\utils\generate_fig_bat.py

@REM set models=H_Others_UNet H_Others_ResUNet H_Others_nnUNet H_Others_TSC_Net H_Others_UDADS_Net H_Others_FANN H_Others_WingsNet H_P_EGA_Net_KDI P_EGA_Net_KDI Z_Label
set models=Others_UNet Others_ResUNet Others_nnUNet Others_TSC_Net Others_UDADS_Net Others_FANN Others_WingsNet 
set patients=LIDC_005 LIDC_031 LIDC_033 LIDC_034 LIDC_049 Shanghai_008 Shanghai_013 Shanghai_038 Shanghai_056 Shanghai_065 Shanghai_077 Shanghai_098 Shanghai_105 Shanghai_107 Shanghai_108 Shanghai_145 Shanghai_147 Shanghai_184 Shanghai_186 Shanghai_210
@REM set patients=Shanghai_077 Shanghai_107 Shanghai_108 Shanghai_184

set VTK_DEBUG_LEAKS=0
for %%m in (%models%) do (
    for %%p in (%patients%) do (
        echo Processing %%m / %%p
        "%slicer%" --no-splash --disable-cli-modules --python-script "%script%" -- %%m %%p
    )
)

echo Done
pause