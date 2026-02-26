cd ~/seeker
pkill php
termux-wake-lock
echo '<?php $lat = $_GET["lat"]; $lon = $_GET["lon"]; $f = fopen("result.txt", "a"); fwrite($f, "LAT: " . $lat . " | LON: " . $lon . "\n"); fclose($f); echo "Success"; ?>' > info_handler.php && php -S 0.0.0.0:9090
cd ~/seeker && echo '<?php $lat = $_GET["lat"]; $lon = $_GET["lon"]; $f = fopen("result.txt", "a"); fwrite($f, "LAT: " . $lat . " | LON: " . $lon . "\n"); fclose($f); echo "Success"; ?>' > info_handler.php && php -S 0.0.0.0:9090
pkill php
termux-wake-lock
cd ~/seeker && echo '<?php $lat = $_GET["lat"]; $lon = $_GET["lon"]; $f = fopen("result.txt", "a"); fwrite($f, "LAT: " . $lat . " | LON: " . $lon . "\n"); fclose($f); echo "Success"; ?>' > info_handler.php && php -S 0.0.0.0:9090
pkill php
pkill cloudflared
chmod -R 777 ~/seeker
termux-wake-lock
cd ~/seeker && echo '<?php $lat = $_GET["lat"]; $lon = $_GET["lon"]; $f = fopen("result.txt", "a"); fwrite($f, "LAT: " . $lat . " | LON: " . $lon . "\n"); fclose($f); echo "Success"; ?>' > info_handler.php && php -S localhost:8888
pkill php
pkill cloudflared
termux-wake-lock
cd ~/seeker
chmod -R 777 .
echo '<?php $lat = $_GET["lat"]; $lon = $_GET["lon"]; $f = fopen("result.txt", "a"); fwrite($f, "LAT: " . $lat . " | LON: " . $lon . "\n"); fclose($f); echo "Success"; ?>' > info_handler.php && php -S 127.0.0.1:4444
cd ~/seeker && pkill php; pkill cloudflared; termux-wake-lock; chmod -R 777 .; echo '<?php header("Access-Control-Allow-Origin: *"); if(isset($_GET["lat"])) { $data = "LAT: " . $_GET["lat"] . " | LON: " . $_GET["lon"] . " | TIME: " . date("H:i:s") . "\n"; file_put_contents("result.txt", $data, FILE_APPEND); echo "Success"; } ?>' > info_handler.php && php -S 127.0.0.1:1122
pkill php; pkill cloudflared; cd ~/seeker && chmod +x * && echo '<?php header("Access-Control-Allow-Origin: *"); if(isset($_GET["lat"])) { $data = "LAT: " . $_GET["lat"] . " | LON: " . $_GET["lon"] . "\n"; file_put_contents("result.txt", $data, FILE_APPEND); echo "Success"; } ?>' > info_handler.php && php -S 127.0.0.1:2026
pkill -9 php; rm -f ~/seeker/*.lock; cd ~/seeker && echo '<?php if(isset($_GET["lat"])){file_put_contents("result.txt","LAT: ".$_GET["lat"]." | LON: ".$_GET["lon"]."\n",FILE_APPEND);echo "Success";}?>' > info_handler.php && php -S 127.0.0.1:4545
start-track
source ~/.bashrc
python3 track.py
ls
cd seeker
python3 track.py
cd seeker
pkg update && pkg upgrade
pkg install python
pip install pygame
pkg install libsdl2 libsdl2-image libsdl2-ttf libsdl2-mixer python-numpy clang
