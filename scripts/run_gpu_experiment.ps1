# Run experiment wrapper and prefer GPU if available
python ..\run_experiment.py --mode syn --device auto --dataset kodak --max_epoch 50 --limit 2 --checkpoint_dir ..\results_checkpoints
