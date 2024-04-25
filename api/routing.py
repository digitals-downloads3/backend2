from channels.routing import ChannelNameRouter, URLRouter
from chat.consumers import ChatConsumer

channel_routing = ChannelNameRouter({
    "chat": ChatConsumer,
})

application = URLRouter(channel_routing)
