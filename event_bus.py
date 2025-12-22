# event_bus.py
import threading


class EventBus:
	"""
	Simple in-process event bus keyed by string. Thread-safe.
	"""

	def __init__(self):
		self._events = {}
		self._lock = threading.Lock()

	def _ensure(self, key: str) -> threading.Event:
		with self._lock:
			ev = self._events.get(key)
			if ev is None:
				ev = threading.Event()
				self._events[key] = ev
			return ev

	def wait(self, key: str, timeout=None) -> bool:
		return self._ensure(key).wait(timeout=timeout)

	def set(self, key: str):
		self._ensure(key).set()

	def clear(self, key: str):
		self._ensure(key).clear()
