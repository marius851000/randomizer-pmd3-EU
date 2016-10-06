clean.bat

call ppmd_kaoutil.exe "portraits" "rom/data/FONT/kaomado.kao"

ppmd_packfileutil.exe "rom/data/MONSTER/m_ground"

del "rom.nds"
ndstool.exe -c "pmd-random.nds" -9 "rom/arm9.bin" -7 "rom/arm7.bin" -y9 "rom/y9.bin" -y7 "rom/y7.bin" -d "rom/data" -y "rom/overlay" -t "rom/banner.bin" -h "rom/header.bin"