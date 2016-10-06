rmdir /Q /S "./romus"
rmdir /Q /S "./rom"
rmdir /Q /S "./m_go"
rmdir /Q /S "./portraits"
rmdir /Q /S "./porrandom"


del "romus"
mkdir "romus"
echo "extraction de la rom US"
ndstool.exe -x "rom-US.nds" -9 "romus/arm9.bin" -7 "romus/arm7.bin" -y9 "romus/y9.bin" -y7 "romus/y7.bin" -d "romus/data" -y "romus/overlay" -t "romus/banner.bin" -h "romus/header.bin" -v

del "rom"
mkdir "rom"
echo "extraction de la rom EU"
ndstool.exe -x "rom-EU.nds" -9 "rom/arm9.bin" -7 "rom/arm7.bin" -y9 "rom/y9.bin" -y7 "rom/y7.bin" -d "rom/data" -y "rom/overlay" -t "rom/banner.bin" -h "rom/header.bin" -v

echo "copy des fichier"
del "rom\data\BALANCE\mappa_gs.bin"
del "rom\data\BALANCE\mappa_gt.bin"
del "rom\data\BALANCE\mappa_gy.bin"
del "rom\data\BALANCE\mappa_s.bin"
del "rom\data\BALANCE\mappa_t.bin"
del "rom\data\BALANCE\mappa_y.bin"

copy "romus\data\BALANCE\mappa_gs.bin" "rom\data\BALANCE\mappa_gs.bin"
copy "romus\data\BALANCE\mappa_gt.bin" "rom\data\BALANCE\mappa_gt.bin"
copy "romus\data\BALANCE\mappa_gy.bin" "rom\data\BALANCE\mappa_gy.bin"
copy "romus\data\BALANCE\mappa_s.bin" "rom\data\BALANCE\mappa_s.bin"
copy "romus\data\BALANCE\mappa_t.bin" "rom\data\BALANCE\mappa_t.bin"
copy "romus\data\BALANCE\mappa_y.bin" "rom\data\BALANCE\mappa_y.bin"

del "pmd-random.nds"
ndstool.exe -c "pmd-random.nds" -9 "rom/arm9.bin" -7 "rom/arm7.bin" -y9 "rom/y9.bin" -y7 "rom/y7.bin" -d "rom/data" -y "rom/overlay" -t "rom/banner.bin" -h "rom/header.bin"