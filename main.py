import re
import asyncio
from typing import List
from collections import OrderedDict
from loguru import logger
import click

PHONE_REGEX = re.compile(r'(?:\+7|8)?\s*[\(\-]?(\d{3})[\)\-\s]?(\d{3})[\-\s]?(\d{2})[\-\s]?(\d{2})')


class PhoneExtractor:
	def __init__(self, file_path: str) -> None:
		self.file_path = file_path
		self.raw_text: str = ''
		self.numbers: OrderedDict[str, None] = OrderedDict()

	async def read_file(self) -> None:
		logger.info(f"Reading file: {self.file_path}")
		loop = asyncio.get_event_loop()
		with open(self.file_path, 'r', encoding='utf-8') as f:
			self.raw_text = await loop.run_in_executor(None, f.read)
		logger.success("File read successfully.")

	def extract_numbers(self) -> None:
		logger.info("Extracting phone numbers from text.")
		for match in PHONE_REGEX.finditer(self.raw_text):
			yyy, xxx, xx1, xx2 = match.groups()
			formatted = f"+7({yyy}){xxx}-{xx1}-{xx2}"
			if formatted not in self.numbers:
				logger.debug(f"Found number: {formatted}")
			self.numbers[formatted] = None
		logger.success(f"Extracted {len(self.numbers)} unique phone numbers.")

	def get_numbers(self) -> List[str]:
		return list(self.numbers.keys())

	async def process(self) -> List[str]:
		await self.read_file()
		self.extract_numbers()
		return self.get_numbers()


@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def main(file_path: str) -> None:
	extractor = PhoneExtractor(file_path)
	numbers = asyncio.run(extractor.process())
	click.echo("\nExtracted Phone Numbers:")
	for number in numbers:
		click.echo(number)


if __name__ == '__main__':
	main()
