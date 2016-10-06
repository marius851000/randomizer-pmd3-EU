rmdir /Q /S "./romus"
rmdir /Q /S "./rom"
rmdir /Q /S "./m_go"
rmdir /Q /S "./portraits"
rmdir /Q /S "./porrandom"

del "rom"
mkdir "rom"
echo "extraction de la rom EU"
ndstool.exe -x "rom-EU.nds" -9 "rom/arm9.bin" -7 "rom/arm7.bin" -y9 "rom/y9.bin" -y7 "rom/y7.bin" -d "rom/data" -y "rom/overlay" -t "rom/banner.bin" -h "rom/header.bin" -v


ppmd_kaoutil.exe "./rom/data/FONT/kaomado.kao" "./portraits"
ppmd_packfileutil.exe "rom/data/MONSTER/m_ground.bin"