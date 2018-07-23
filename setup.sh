#!/usr/bin/env bash
echo -e "           
         -/osssssooooosssssssssssssso/-         
        /sssssso+///////////////++osssyys        
      looooss*************************yooos:     
      oyyys- ./ossssssssooooossssso/. .ossy:      
      yyyy- -sssssssssssssooooss/-:ss/  sss+      
      yyys  syyysssssoo+///+oooo:.:sss. /sso      
      yyyo  yyyyyys+-....... ./oooosss. :ss+      
      ssyo  yyyyys: ./osssso+- .+oooos. :ss+      
      oss+  yyyyy/ .syssssssss:  osooo. :ss+      
      ooo+  yyyyy. /yyyysssssss  +ssso. :ss+      
      ++o/  ssyyy/ .syyyyyssss/  sssss. :oo+      
      /++/  osssyy: .+syyyyso:  +sssss. :oo+      
      ////  ooossss+-  .--../  sssssss. :ss+      
      :://  -+ooossssso++/+ossyysssss+  oss+      
      -:::: ./+ooosssyyyyyyyyyyyyso:+  sss:      
       -::::                          osss/       
        .-:::::--------::::::::://+ssyyso-        
          .-:::///+++ooosssyyyyyyyyssso/.          
           -/osssssooooossssssssssssss/             
"                                                 
                                                  

spinner() {
    local i sp n
    sp='/-\|'
    n=${#sp}
    printf ' '
    while sleep 0.1; do
        printf "%s\b" "${sp:i++%n:1}"
    done
}

echo ================================================================================
echo 'InstaPy Telegram Bot v1.0'
echo ================================================================================
echo by haloivan
echo https://github.com/haloivan/instapy-telegram
echo ================================================================================
spinner &
sleep 5
echo 'InstaPy Telegram Bot Setup Started'
echo ================================================================================
cd ../
dirMain=$(pwd)
sleep 5
echo 'Copying main file...'
sleep 3
cp $dirMain/instapy-telegram/instapytelegram.py $dirMain/instapytelegram.py
echo 'Main file copied to' $dirMain/instapytelegram.py
cd instapy-telegram
sleep 3
echo 'installing module and package'
sleep 3
spinner_pid=$!
kill $spinner_pid >/dev/null 2>&1 || true
pip3 install . | fold
echo ================================================================================
echo "Setup Data"
echo ================================================================================
chmod +x $dirMain/instapy-telegram/teledata/config.ini
chmod 774 $dirMain/instapy-telegram/teledata/config.ini
echo "Insert your telegram bot token:"
read token
echo "Insert your Instgram username: "
read username
read -sp "Insert your Instgram password: " password 
printf "[telegram]\ntoken = ${token}\n[instapy]\nusername = ${username}\npassword = ${password}" > $dirMain/instapy-telegram/teledata/config.ini
echo ""
echo ================================================================================
echo "Setup is completed. Have Fun!!! :D"
echo ================================================================================