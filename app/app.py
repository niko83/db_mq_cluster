import commands
import settings

MAP_COMMAND = {
    'add_user': commands.add_user,
}


async def app(command_name, data):

    command = MAP_COMMAND.get(command_name, commands.default)
    result = await command.run(data)

    output = {
        'hostname': settings.HOSTNAME,
        'input': (command_name, data),
        'result': result,
    }
    return output
