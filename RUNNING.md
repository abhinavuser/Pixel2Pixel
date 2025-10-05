Reproducing the Pixel2Pixel repo locally (Windows / PowerShell)

This file documents the exact commands used to create a reproducible local environment, run a quick smoke test, and run on GPU (if available). All commands are for PowerShell (Windows).

1) Create a Python virtual environment and activate it

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

3) Quick smoke test (small image, CPU, 1 image, 1 epoch)

This helper will create a small 128x128 test image from the first image in `data/kodak`, then run the synthetic script with small window/patch sizes to keep memory low.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_smoke_test.ps1
# Or run manually:
python .\scripts\make_small_dataset.py
python .\Pixel2Pixel_syn.py --device cpu --limit 1 --max_epoch 1 --ws 16 --ps 3 --nn 4 --mm 2
```

4) Running on GPU (recommended for real experiments)

If your machine has a CUDA-capable GPU and you installed a CUDA-enabled PyTorch wheel, run with `--device cuda:0` (or omit --device if you want auto-detect):

```powershell
# Example: full run on folder 'kodak' with GPU
python .\Pixel2Pixel_syn.py --device cuda:0 --dataset kodak --ws 40 --ps 7 --nn 16 --mm 8 --max_epoch 3000

# For real data (assumes data/SIDD/GT and data/SIDD/Noisy exist):
python .\Pixel2Pixel_real.py --device cuda:0 --dataset SIDD --GT GT --Noisy Noisy --ws 40 --ps 7 --nn 100 --mm 20 --max_epoch 3000
```

5) Git: pushing these commits to your remote repository

This project already has a remote `origin` set (e.g., https://github.com/abhinavuser/Pixel2Pixel.git). To push local commits to GitHub:

```powershell
git status
git add <files>
git commit -m "Describe changes"
git push origin main
```

Notes about authentication:
- If HTTPS push prompts for username/password, create a GitHub Personal Access Token (PAT) and use it as the password. See GitHub docs.
- Alternatively configure SSH keys and use an SSH remote (git@github.com:...) instead of HTTPS.

6) Troubleshooting tips
- If you hit OOM on CPU: reduce `--ws`, `--ps`, `--nn`, `--limit` and/or resize images.
- If PyTorch shows `torch.*+cpu` and `torch.cuda.is_available()` is False, you need a CUDA-compatible PyTorch install (follow https://pytorch.org/get-started/locally/).
