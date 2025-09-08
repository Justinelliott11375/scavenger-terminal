# usb_gate_generic.py
import sys
import time
from typing import Optional

import pyudev

VENDOR_ID = 'abcd'
MODEL_ID = '1234'
TARGET_SIZE_MB = 960
SIZE_TOL_MB = 128  # +/- window to allow slight formatting differences


def on_correct_usb_inserted():
	# TODO: implement reaction to correct USB insertion here
	print('[USB] Correct generic stick detected. Advancing game step.', flush=True)


def _device_size_mb(device) -> Optional[int]:
	try:
		dev = device
		while dev and dev.device_type not in ('disk', 'partition'):
			dev = dev.parent
		if not dev:
			return None

		# For partitions, go up to the parent "disk" for size
		if dev.device_type == 'partition' and dev.parent:
			dev = dev.parent

		# sysfs provides "size" as sector count * 512 bytes
		path = f'/sys/class/block/{dev.sys_name}/size'
		with open(path, 'r') as f:
			sectors = int(f.read().strip())
		bytes_ = sectors * 512
		mb = int(bytes_ // (1024 * 1024))
		return mb
	except Exception:
		return None


def _matches_fingerprint(device) -> bool:
	# Only consider block devices created ("add" events will give us both disk and partition on many sticks)
	if device.subsystem != 'block':
		return False
	if device.device_type not in ('disk', 'partition'):
		return False

	# Vendor/Model check (most important for this generic device)
	if device.get('ID_VENDOR_ID') != VENDOR_ID:
		return False
	if device.get('ID_MODEL_ID') != MODEL_ID:
		return False

	# Size check for collision avoidance
	size_mb = _device_size_mb(device)
	if size_mb is None:
		# If we can't read size for some reason, fail closed
		return False
	if not (TARGET_SIZE_MB - SIZE_TOL_MB <= size_mb <= TARGET_SIZE_MB + SIZE_TOL_MB):
		return False

	return True


def _sweep_existing(ctx: pyudev.Context) -> bool:
	"""Covers the 'already plugged in when we start waiting' case."""
	for dev in ctx.list_devices(subsystem='block'):
		if _matches_fingerprint(dev):
			return True
	return False


def wait_for_generic_usb(timeout: float | None = None) -> bool:
	"""
	Blocks until the specific generic USB appears (per our composite fingerprint).
	Returns True on match, False on timeout.
	"""
	ctx = pyudev.Context()

	# Quick sweep in case it's already present
	if _sweep_existing(ctx):
		return True

	monitor = pyudev.Monitor.from_netlink(ctx)
	monitor.filter_by('block')
	start = time.time()

	for action, dev in monitor:
		if action != 'add':
			# we only care about insertions
			continue
		if _matches_fingerprint(dev):
			return True
		if timeout is not None and (time.time() - start) >= timeout:
			return False


def gate_run(timeout: float | None = None) -> bool:
	print('[USB] Waiting for the specific generic USB…', flush=True)

	if not sys.platform.startswith('linux'):
		print('[USB] Unsupported platform, skipping USB wait.', flush=True)
		return False

	ok = wait_for_generic_usb(timeout=timeout)
	if ok:
		on_correct_usb_inserted()
		return True
	print('[USB] Timeout waiting for the stick.', flush=True)
	return False


if __name__ == '__main__':
	gate_run(timeout=None)
