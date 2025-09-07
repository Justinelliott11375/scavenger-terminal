import argparse

from terminal_session import TerminalSession


def parse_args():
	parser = argparse.ArgumentParser(description='Terminal session')
	parser.add_argument(
		'--start-at',
		type=str,
		default='boot',
		help='Start the session at a specific point (e.g., boot, keyboard_ready)',
	)
	return parser.parse_args()


def main():
	args = parse_args()
	session = TerminalSession()

	# TODO: keyboard ready may not be the best name, interactive session? come up with a convention
	if args.start_at == 'keyboard_ready':
		session.start_interactive_session()
	elif args.start_at == 'boot':
		session.run()


if __name__ == '__main__':
	main()
