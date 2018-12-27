:LOOP
if (%1)==() GOTO CLEANUP
"c:\Program Files\VideoLAN\VLC\vlc.exe" -vvv %1 --sout-ffmpeg-qscale 1  :sout=#transcode{vcodec=WMV2,scale=1,acodec=wma,ab=96,channels=2}:duplicate{dst=std{access=file,mux=asf,dst=%1.wmv}} vlc:quit
SHIFT
GOTO LOOP
:CLEANUP
ECHO. FINISHED!