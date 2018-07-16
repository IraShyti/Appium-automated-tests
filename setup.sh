#wget https://bitbucket.org/appium/appium.app/downloads/appium-1.4.13.dmg

#tmp_file='appium-1.4.13.dmg'
#apps_folder='/Applications'

#echo "Mounting image..."
#volume=`hdiutil mount $tmp_file | tail -n1 | perl -nle '/(\/Volumes\/[^ ]+)/; print $1'`

# Locate .app folder and move to /Applications
#app=`find $volume/. -name *.app -maxdepth 1 -type d -print0`
#echo "Copying `echo $app | awk -F/ '{print $NF}'` into $apps_folder..."
#cp -ir $app $apps_folder

# Unmount volume, delete temporal file
#echo "Cleaning up..."
#hdiutil unmount $volume -quiet
#rm $tmp_fil


brew install mongodb
mkdir -p /data/db
chmod 766 /data/db
mongod


git clone https://irashyti@bitbucket.org/seecis/appium-tests.git
cd appium-tests
pip install -r requirements.txt
#python appium_tests.py

cd ..
#git clone https://irashyti@bitbucket.org/seecis/appium-web.git
#cd appium-web
#npm install
#node app_server.js


cd ..
cp appium-tests/supervisord.conf supervisord.conf
#sudo supervisord -c supervisord.conf

brew install nginx
cp appium-test/appium.conf /usr/local/etc/enginx/servers/appium.conf
sudo nginx -s reload
