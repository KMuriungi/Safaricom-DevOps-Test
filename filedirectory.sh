# Kithinji Muriungi 

image=0
muzik=0
video=0
log=0
other=0
for k in * 
do
    if [[ $k == *.mp3 || $k == *.flac ]]
    then
        if [ $muzik == 0 ] 
        then
            mkdir music;
            muzik=`expr $muzik+1`
        fi
        mv $k $pwd music; 
    fi
    if [[ $k == *.jpg || $k == *.png ]]
    then
        if [ $image == 0 ]
        then
            mkdir images;
            image=`expr $image+1`
        fi
        mv $k $pwd images;
    fi
    if [[ $k == *.avi || $k == *.mov ]]
    then
        if [ $video == 0 ]
        then
            mkdir videos;
            video=`expr $video+1`
        fi
        mv $k $pwd videos;
    fi
    if [[ $k == *.log ]]
    then
        rm $k 
    fi
done
