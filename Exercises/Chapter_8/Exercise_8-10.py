def show_messages(list_of_messages: list, printed_messages: list):
    while list_of_messages:
        message = list_of_messages.pop()
        print(f'Message: {message}')
        send_message(list_of_messages, printed_messages, message)

def send_message(
        list_of_messages: list,
        printed_messages: list,
        message_to_move):
    printed_messages.append(message_to_move)


messages = ['Hi', 'Hello', 'Howdy', 'Oi']
sent_messages = []

show_messages(messages, sent_messages)

print(messages)
print(sent_messages)