from typing import Optional, Union, List
from rich.console import RenderableType
class TerminalOutput:
	def __init__(
			self,
			lines: Optional[List[str]] = None,
			renderable: Optional[RenderableType] = None,
			scrollable: bool = True,
			wrap: bool = True,
	):
		self.lines = lines
		self.renderable = renderable
		self.scrollable = scrollable
		self.wrap = wrap
