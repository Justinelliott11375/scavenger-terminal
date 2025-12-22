# sequence_types.py
from dataclasses import dataclass
from typing import Any, Callable, List, Optional


@dataclass
class Step: ...


@dataclass
class PrintLine(Step):
	text: str
	style: Optional[str] = None


@dataclass
class PrintLines(Step):
	lines: List[str]
	style: Optional[str] = None


@dataclass
class Render(Step):
	renderable: Any


@dataclass
class Sleep(Step):
	seconds: float


@dataclass
class OverwriteLastLine(Step):
	text: str
	style: Optional[str] = None


@dataclass
class Effect(Step):
	name: str
	params: dict


@dataclass
class WaitForSignal(Step):
	key: str
	timeout: Optional[float] = None


@dataclass
class Call(Step):
	func: Callable[[], None]


@dataclass
class TerminalSequence:
	steps: List[Step]
	name: str = 'anonymous'
