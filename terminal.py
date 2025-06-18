import sys
import shutil
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.align import Align
from time import sleep
import time, random

console = Console()

def boot_sequence():
	console.clear()

	language_sequence = [
		{
			"header": "Sistema Conejo Blanco // Secuencia de Arranque",
			"sample": 'Entorno de sondeo para detección de idioma...'
		},
		{
			"header": "Systèmes Lapin Blanc // Séquence de démarrage du système",
			"sample": 'Environnement de sondage pour la détection de la langue...'
		},
		{
			"header": "ホワイトラビットシステムズ // システムブートシーケンス",
			"sample": '言語検出のためのポーリング環境...'
		},
		{
			"header": "Weiße-Kaninchen-Systeme // Systemstartsequenz",
			"sample": 'Polling-Umgebungen zur Spracherkennung...'
        },
        {
            "header": "Системы Белого Кролика // Последовательность загрузки системы",
			"sample": 'Опрос окружения для определения языка...'
		},
		{
			"header": "White Rabbit Systems // System Boot Sequence",
			"sample": 'Polling Surroundings for language detection...'
		}
	]

	with Live(refresh_per_second=4) as live:
		for step in language_sequence:
			header = f"[bold green]{step['header']}[/bold green]"

			body = f"[dim][italic]{step['sample']}[/italic][/dim]"
			live.update(Panel(f"{header}\n\n{body}", expand=False))
			sleep(1.5)

	# sleep(1)
	# console.print('[green]Language detected: English[/green]')
	# sleep(1)
	# console.print('[green]Updating system language settings...[/green]')
	# sleep(2)
	# test_chaotic_flash_with_text('[green]System language set to English[/green]')


	# # package this whole burst->message->sleep->clear into a function
	# flash_noise_burst(center=False)
	# glitch_type_out(text="...hello?", style="bold magenta")
	# sleep(2)
	# clear_last_lines()
	# flash_noise_burst(center=False)
	# glitch_type_out(text="Something is wrong... horribly wrong...", style="bold magenta")
	# sleep(3)
	# clear_last_lines()



	steps = [
        '[cyan]Language detected: English[/cyan]',
		'[cyan]Updating system language settings...[/cyan]',
		"[cyan]Initializing system memory...[/cyan]",
		"[cyan]Loading kernel modules...[/cyan]",
		"[cyan]Mounting /core/ai...[/cyan]",
		"[cyan]Power Supply: [/cyan][green]STABLE[/green]",
		"[cyan]Video Output Device: [/cyan][green]CONNECTED[/green]",
        "[cyan]User Input Device: [/cyan][red]NOT CONNECTED[/red]",
        "[yellow]Warning: Peripheral input device not detected[/yellow]",
        "[cyan]Awaiting input device connection...[/cyan]",
        "[red]-- INTERR[green]⟟⟟⟟⟟[/green]UPT[green]⟟⟟⟟[/green] --[/red]",
        "[red]SYST[green]cho--E|_[/green]EM INTERRU[green]𓂀𓂀 𓁹𓅓𓃗𓆗[/green]PT: UNKNOWN SOURCE[/red]",
        "[red]ECHO PATH BREACH[green]⠛⠃⠛[/green] DETECT[green]⠛⠃[/green]ED[/red]",
	]

	for step in steps:
		console.print(step)
		if step == "[red]ECHO PATH BREACH[green]⠛⠃⠛[/green] DETECT[green]⠛⠃[/green]ED[/red]":
			test_chaotic_flash()
		elif step.startswith("[red]"):
			flash_noise_burst(center=False)
			# sleep(1)
		else:
			sleep(2)

	console.clear()
	glitch_type_out('Pay attention...', delay=0.05, glitch_chance=0.05)
	time.sleep(3)
	console.clear()
	glitch_type_out('The rabbit hole goes deeper...', delay=0.05, glitch_chance=0)
	time.sleep(3)
	console.clear()
	output_line = 'Find the keyboard...'
	glitch_type_out_with_rabbit_overwrite(output_line, delay=0.2)
	console.clear()

	steps = [
        '[cyan]Language detected: English[/cyan]',
		'[cyan]Updating system language settings...[/cyan]',
		"[cyan]Initializing system memory...[/cyan]",
		"[cyan]Loading kernel modules...[/cyan]",
		"[cyan]Mounting /core/ai...[/cyan]",
		"[cyan]Power Supply: [/cyan][green]STABLE[/green]",
		"[cyan]Video Output Device: [/cyan][green]CONNECTED[/green]",
        "[cyan]User Input Device: [/cyan][red]NOT CONNECTED[/red]",
        "[yellow]Warning: Peripheral input device not detected[/yellow]",
        "[cyan]Awaiting input device connection...[/cyan]",
	]

	test_chaotic_flash()
	console.print('[green]Echo path breach resolved...[/green]')
	sleep(2)
	console.print( "[green]Restoring previous diagnostic session...[/green]",)
	sleep(2)
	header = '[bold green]White Rabbit Systems // System Boot Sequence[bold green]'
	body = '[italic]Polling Surroundings for language detection...[/italic]'
	console.print(Panel(f'{header}\n\n{body}', expand=False))
	for step in steps:
		console.print(step)


	# Continue with rest of boot
	# console.print("[yellow]Warning: Peripheral input device not detected[/yellow]")
	time.sleep(10)
	# console.print("[cyan]Launching user shell...[/cyan]")
	# console.print()
	# time.sleep(0.5)


# Refactor this to handle commands as they get added further through the game
def handle_command(command: str) -> str:
    command = command.strip().lower()

    if command == "help":
        return "Available commands:\n  help\n  status\n  enhance\n  exit"
    elif command == "status":
        return "Subsystem status:\n- Audio: OK\n- Visual: Calibrated\n- Lock: Standby"
    elif command == "enhance":
        return "Enhancing signal...\n[green]Signal clarity improved by 37%[/green]"
    elif command == "exit":
        return "[red]Session terminated.[/red]"
    else:
        return "[yellow]Unknown command.[/yellow] Type 'help' for a list of valid commands."

def type_out(text: str, delay: float = 0.03, style: str = ""):
	"""Print text one character at a time with optional rich styling."""
	for char in text:
		console.print(char, end='', style=style, soft_wrap=True)
		sys.stdout.flush()
		time.sleep(delay)
	console.print()

def clear_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1A')  # Up one line
        sys.stdout.write('\x1b[2K')  # Clear line
    sys.stdout.flush()
def main():
    boot_sequence()
    console.print(Panel("[bold green]Interactive Secure Shell Ready[/bold green]", expand=False))

    while True:
        command = console.input("[green]>> [/green]")
        result = handle_command(command)
        console.print(result)
        if command.strip().lower() == "exit":
            break

def system_line(text):
    print(f"\033[32m{text}\033[0m")

def rabbit_line(text):
    print(f"\033[1m\033[36m:: {text}\033[0m")

def glitch_line(text):
    glitched = ''.join(
        c if random.random() > 0.1 else chr(random.randint(33, 126))
        for c in text
    )
    print(f"\033[35m{glitched}\033[0m")

def glitch_type_out(text: str, delay: float = 0.075, glitch_chance=0.05, style="bold magenta"):
	"""Type out text with occasional glitched characters and optional styling."""
	text = f'ДД: {text}'
	for char in text:
		# Randomly replace character
		if random.random() < glitch_chance and char not in [' ', '.', ':', 'Д']:
			glitched_char = chr(random.randint(33, 126))
		else:
			glitched_char = char

		if glitched_char == 'Д':
			console.print(glitched_char, end='', style='bold white', soft_wrap=True)
		else:
			console.print(glitched_char, end='', style=style, soft_wrap=True)
		sys.stdout.flush()
		time.sleep(delay)

	console.print()  # Newline at end

def glitch_type_out_with_rabbit_overwrite(text: str, delay: float = 0.075, style="bold magenta"):
	"""Type out text with occasional glitched characters and optional styling."""
	text = f'ДД: {text}'
	for char in text:

		if char == 'Д':
			console.print(char, end='', style='bold white', soft_wrap=True)
		else:
			console.print(char, end='', style=style, soft_wrap=True)
		sys.stdout.flush()
		time.sleep(delay)
    # just a test here, remove later
	sleep(4)
	target_index = text.index('o', 0)  # First 'c' in 'connection'
	cursor_back = len(text) - target_index
	sys.stdout.write(f'\x1b[{cursor_back}D')  # Move left N chars
	sys.stdout.write("🐇")
	sys.stdout.write(f'\x1b[{cursor_back}C')  # Move right N characters
	sys.stdout.flush()
	sleep(1)

	console.print()  # Newline at end
def flash_and_clear(text, delay=0.4):
    sys.stdout.write(f"\r{text}")
    sys.stdout.flush()
    time.sleep(delay)
    sys.stdout.write("\r" + " " * len(text) + "\r")
    sys.stdout.flush()

def flash_noise_burst(count=15, delay=0.2, center=True):
    noise_lines = [
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒🐇▒▒▒▒▒▒▒▒",
        "⣷⣯⣾⣽⣻⣿⣿⣿⣾⣿⣯⣟⣽⣻",
        "error://::∵∴∷⩹⩺⩻",
        "⟟⟟⟟⟟⟟⟟⟟⟟🐇⟟⟟",
        "ΣYSTEM_BR34K→█▒░░▒░▒░█",
        "01101000 01110101 01101110 01110🐇100",
        "[MEM_DUMP] 0xA1C5 0xA1C6 0xA1C7 ▒▒▒▒▒",
        "[🞭🞮🞰🞲🞬🞫]",
        "𓂀𓂀𓂀𓂀𓂀 𓁹𓅓𓃗𓆗",
        "▒⠛⢶⡿⠛⠃▒░░▒▒⡴⠛⠃⠒⠂",
        ":: signal trace//echo--E|_broken",
        "[rebind_failed] peripheral_x",
        "— connection? echo... echo... 🐇"
    ]

    cols = shutil.get_terminal_size().columns
    for _ in range(count):
        line = random.choice(noise_lines)
        if center:
            line = line.center(cols)
        flash_and_clear(line, delay)

# Utility effects
def amplify(text, factor=2):
    return ''.join(c * factor for c in text)

def fullwidth(text):
    return ''.join(chr(ord(c) + 0xFEE0) if '!' <= c <= '~' else c for c in text)

def pixel_scale_sim(text):
    if random.random() < 0.5:
        return amplify(text, factor=2)
    return fullwidth(text)

# Clean flicker effect
def flicker_line(text, duration=0.6, interval=0.1):
    width = shutil.get_terminal_size().columns
    padded = text.ljust(width)
    end_time = time.time() + duration
    while time.time() < end_time:
        style = random.choice(["bold red", "dim cyan", "yellow", "bold magenta", "green"])
        console.print(padded, style=style, end='\r', highlight=False)
        sys.stdout.flush()
        time.sleep(interval)
    console.print(" " * width, end='\r')

# Clean color pulse effect
def color_pulse(text, pulses=5, interval=0.1):
    colors = ["red", "yellow", "green", "cyan", "magenta"]
    width = shutil.get_terminal_size().columns
    padded = text.ljust(width)
    for _ in range(pulses):
        style = random.choice(colors)
        console.print(padded, style=style, end='\r')
        sys.stdout.flush()
        time.sleep(interval)
    console.print(" " * width, end='\r')

# Unified method
def chaotic_flash_burst(count=6, flicker_duration=0.4, pulse=True, center=True):
	cols = shutil.get_terminal_size().columns
	noise_lines = [
		"▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
		"⣷⣯⣾⣽⣻⣿⣿⣿⣾⣿⣯⣟⣽⣻",
		"error://::∵∴∷⩹⩺⩻",
		"ΣYSTEM_BR34K→█▒░░▒░▒░█",
		"01101000 01110101 01101110 01110100",
		"[MEM_DUMP] 0xA1C5 0xA1C6 ▒▒▒▒▒",
		":: echo trace → /null 🐇",
		"▒⠛⢶⡿⠛▒▒⡴⠛⠃⠒⠂",
        "⟟⟟⟟⟟⟟⟟⟟⟟⟟⟟",
        "[MEM_DUMP] 0xA1C5 0xA1C6 0xA1C7 ▒▒▒▒▒",
        "[🞭🞮🞰🞲🞬🞫]",
        "𓂀𓂀𓂀𓂀𓂀 𓁹𓅓𓃗𓆗",
        "▒⠛⢶⡿⠛⠃▒░░▒▒⡴⠛⠃⠒⠂",
        ":: signal trace//echo--E|_broken",
        "[rebind_failed] peripheral_x",
        "— connection? echo... echo... 🐇"
	]

	for _ in range(count):
		line = random.choice(noise_lines)
		line = pixel_scale_sim(line)
		if center:
			line = line.center(cols)

		flicker_line(line, duration=flicker_duration)
		if pulse:
			color_pulse(line, pulses=3, interval=0.08)

# Updated chaotic_flash_burst
def chaotic_flash_burst_with_text(count=6, flicker_duration=0.4, pulse=True, center=True, insert_text=None):
    cols = shutil.get_terminal_size().columns
    noise_lines = [
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
        "⣷⣯⣾⣽⣻⣿⣿⣿⣾⣿⣯⣟⣽⣻",
        "error://::∵∴∷⩹⩺⩻",
        "ΣYSTEM_BR34K→█▒░░▒░▒░█",
        "01101000 01110101 01101110 01110100",
        "[MEM_DUMP] 0xA1C5 0xA1C6 ▒▒▒▒▒",
        ":: echo trace → /null 🐇",
        "▒⠛⢶⡿⠛▒▒⡴⠛⠃⠒⠂",
        "⟟⟟⟟⟟⟟⟟⟟⟟⟟⟟",
        "[MEM_DUMP] 0xA1C5 0xA1C6 0xA1C7 ▒▒▒▒▒",
        "[🞭🞮🞰🞲🞬🞫]",
        "𓂀𓂀𓂀𓂀𓂀 𓁹𓅓𓃗𓆗",
        "▒⠛⢶⡿⠛⠃▒░░▒▒⡴⠛⠃⠒⠂",
        ":: signal trace//echo--E|_broken",
        "[rebind_failed] peripheral_x",
        "— connection? echo... echo... 🐇"
    ]

    for i in range(count):
        if insert_text and random.random() < 0.5:
            line = insert_text
        else:
            line = random.choice(noise_lines)
            line = pixel_scale_sim(line)

        if center:
            line = line.center(cols)

        flicker_line(line, duration=flicker_duration)
        if pulse:
            color_pulse(line, pulses=3, interval=0.08)
# Demo/test trigger
def test_chaotic_flash():
    chaotic_flash_burst(count=8, flicker_duration=0.4, pulse=True, center=False)

def test_chaotic_flash_with_text(text):
	chaotic_flash_burst_with_text(count=8, flicker_duration=0.4, pulse=True, center=False, insert_text=text)

if __name__ == "__main__":
    main()
