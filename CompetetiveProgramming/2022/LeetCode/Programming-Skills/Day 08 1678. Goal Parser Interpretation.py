class Solution:
    def interpret(self, command: str) -> str:
        # while '()' in command:
        command = command.replace('()', 'o')
        # while '(al)' in command:
        command = command.replace('(al)', 'al')
        return command
