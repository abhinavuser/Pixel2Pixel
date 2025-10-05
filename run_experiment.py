import argparse
import subprocess
import sys
import torch
import os

parser = argparse.ArgumentParser()
parser.add_argument('--mode', choices=['syn', 'real'], default='syn')
parser.add_argument('--device', default='auto')
parser.add_argument('--dataset', default='kodak')
parser.add_argument('--max_epoch', type=int, default=3000)
parser.add_argument('--limit', type=int, default=None)
parser.add_argument('--checkpoint_dir', default='./checkpoints')
parser.add_argument('--extra', default='', help='Extra args to pass to underlying script')
args = parser.parse_args()

if args.device == 'auto':
    use_cuda = torch.cuda.is_available()
    device = 'cuda:0' if use_cuda else 'cpu'
else:
    device = args.device

script = 'Pixel2Pixel_syn.py' if args.mode == 'syn' else 'Pixel2Pixel_real.py'
cmd = [sys.executable, script, '--device', device, '--dataset', args.dataset, '--max_epoch', str(args.max_epoch), '--checkpoint_dir', args.checkpoint_dir]
if args.limit is not None:
    cmd += ['--limit', str(args.limit)]
if args.extra:
    cmd += args.extra.split()

print('Running:', ' '.join(cmd))
ret = subprocess.run(cmd)
sys.exit(ret.returncode)
