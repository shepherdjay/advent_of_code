"""
Can we simplify the structure of the code so that the "processor" of the com device just waits for an
instruction from a queue and processes it?
--> noop would add int 0 to queue
--> addx would add int 0 followed by the value to add to queue (since it takes two ticks)
"""

from asyncio.queues import Queue
import asyncio
import time


class Display:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.display_queue = Queue()
        self.cursor = 0

        asyncio.create_task(self.draw())

    def _draw_pixel(self, sprite_loc):
        if self.cursor % self.width in range(sprite_loc - 1, sprite_loc + 2):
            return '#'
        return ' '

    async def draw(self):
        while True:
            time.sleep(0.025)
            sprite_loc = await self.display_queue.get()
            if self.cursor % self.width == 0:
                print()
            print(self._draw_pixel(sprite_loc=sprite_loc), end='')
            self.cursor += 1


class CommunicationsDevice:
    def __init__(self):
        self.x_register = 1
        self._reg_history = [self.x_register]
        self.cycles = 0
        self.queue = Queue()
        self.display = Display(height=6, width=40)

        asyncio.create_task(self.processor())

    async def processor(self):
        while True:
            register_add = await self.queue.get()
            await self.display.display_queue.put(self.x_register)
            self.cycles += 1
            self._reg_history.append(self.x_register)
            self.x_register += register_add

    async def process_instruction(self, instruction):
        match instruction.split():
            case ['noop']:
                await self.queue.put(0)

            case ['addx', value]:
                await self.queue.put(0)
                await self.queue.put(int(value))

    def signal_strength(self, reg_hist_indx=-1):
        return reg_hist_indx * self._reg_history[reg_hist_indx]


async def main():
    with open('day10_input.txt', 'r') as elf_file:
        instructions = [line.strip() for line in elf_file]

    walkie_talkie = CommunicationsDevice()

    futures = [
        asyncio.create_task(walkie_talkie.process_instruction(instruction))
        for instruction in instructions
    ]

    await asyncio.gather(*futures)

    print(sum([walkie_talkie.signal_strength(x) for x in [20, 60, 100, 140, 180, 220]]))


if __name__ == '__main__':
    asyncio.run(main())
