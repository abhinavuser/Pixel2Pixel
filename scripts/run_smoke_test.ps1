python "${PSScriptRoot}\\make_small_dataset.py"
python "${PSScriptRoot}\\..\\Pixel2Pixel_syn.py" --device cpu --limit 1 --max_epoch 1 --ws 16 --ps 3 --nn 4 --mm 2
