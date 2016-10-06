rmdir "temp"
mkdir "temp"

mkdir "temp/romus"
echo "extraction de la rom US"
ndstool.exe -x "rom-US.nds" -9 "temp/romus/arm9.bin" -7 "temp/romus/arm7.bin" -y9 "temp/romus/y9.bin" -y7 "temp/romus/y7.bin" -d "temp/romus/data" -y "temp/romus/overlay" -t "temp/romus/banner.bin" -h "temp/romus/header.bin" -v

del "temp/rom"
mkdir "temp/rom"
echo "extraction de la rom EU"
ndstool.exe -x "rom-EU.nds" -9 "temp/rom/arm9.bin" -7 "temp/rom/arm7.bin" -y9 "temp/rom/y9.bin" -y7 "temp/rom/y7.bin" -d "temp/rom/data" -y "temp/rom/overlay" -t "temp/rom/banner.bin" -h "temp/rom/header.bin" -v

echo "copy des fichier"
del "temp/rom\data\BALANCE\mappa_gs.bin"
del "temp/rom\data\BALANCE\mappa_gt.bin"
del "temp/rom\data\BALANCE\mappa_gy.bin"
del "temp/rom\data\BALANCE\mappa_s.bin"
del "temp/rom\data\BALANCE\mappa_t.bin"
del "temp/rom\data\BALANCE\mappa_y.bin"

copy "temp/romus\data\BALANCE\mappa_gs.bin" "rom\data\BALANCE\mappa_gs.bin"
copy "temp/romus\data\BALANCE\mappa_gt.bin" "rom\data\BALANCE\mappa_gt.bin"
copy "temp/romus\data\BALANCE\mappa_gy.bin" "rom\data\BALANCE\mappa_gy.bin"
copy "temp/romus\data\BALANCE\mappa_s.bin" "rom\data\BALANCE\mappa_s.bin"
copy "temp/romus\data\BALANCE\mappa_t.bin" "rom\data\BALANCE\mappa_t.bin"
copy "temp/romus\data\BALANCE\mappa_y.bin" "rom\data\BALANCE\mappa_y.bin"

echo "fichier de random copier, debut de la décompilation de la rom EU"
mkdir "temp/portraits"
ppmd_kaoutil.exe ".temp/rom/data/FONT/kaomado.kao" "./temp/portraits"
ppmd_packfileutil.exe "temp/rom/data/MONSTER/m_ground.bin"

echo "fichier extrait"

randomizer.py

call ppmd_kaoutil.exe "temp/portraits" "temp/rom/data/FONT/kaomado.kao"

ppmd_packfileutil.exe "temp/rom/data/MONSTER/m_ground"

del "temp/rom.nds"
ndstool.exe -c "pmd-random.nds" -9 "temp/rom/arm9.bin" -7 "temp/rom/arm7.bin" -y9 "temp/rom/y9.bin" -y7 "temp/rom/y7.bin" -d "temp/rom/data" -y "temp/rom/overlay" -t "temp/rom/banner.bin" -h "temp/rom/header.bin"

del "temp/pmd-random.nds"
ndstool.exe -c "pmd-random.nds" -9 "temp/rom/arm9.bin" -7 "temp/rom/arm7.bin" -y9 "temp/rom/y9.bin" -y7 "temp/rom/y7.bin" -d "temp/rom/data" -y "temp/rom/overlay" -t "temp/rom/banner.bin" -h "temp/rom/header.bin"