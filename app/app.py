import socket
import commands

MAP_COMMAND = {
    'add_user': commands.add_user,
}


async def app(command_name, data):

    command = MAP_COMMAND.get(command_name, commands.default)
    result = await command.run(data)

    output = {
        'hostname': socket.gethostname(),
        'input': (command_name, data),
        'result': result,
    }
    return output
