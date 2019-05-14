
import asyncio
import tornado.escape
import tornado.ioloop
import tornado.locks
import tornado.web
import os.path
import uuid


from tornado.options import define, options, parse_command_line

define("port", default=8889,help="Run on the given port. ", type=int)
define("debug", default=True, help="Run in debug mode. ")

class MessageBuffer(object):
    def __init__(self):
        self.cond = tornado.locks.Condition()
        self.cache = []
        self.cache_size = 200
    
    def get_messages_since(self, cursor):
        """ Return a list of messages newer than the given cursor.
            ``cursor`` should be the ``id`` of the last message received.
        """
        results = []
        for msg in reversed(self.cache):
            if msg["id"] == cursor:
                break
            result.append(msg)
        results.reverse()
        return results

    def add_message(self, message):
        self.cache.append(message)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size :]
        self.cond.notify_all()

# Making this a non-singleton is left as an exercise for the reader
global_message_buffer = MessageBuffer()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=global_message_buffer.cache)

class MessageNewhandler(tornado.web.RequestHandler):
    """ Post a new massage to the chat room. """
    def post(self):
        message = {"id": str(uuid.uuid4()), "body":self.get_argument("body")}
        message["html"] = tornado.escape.to_unicode(
            self.render_string("message.html", message=message)
        )
        if self.get_argument("next", None):
            self.redirect(self.get_argument("next"))
        else:
            self.write(message)
        global_message_buffer.add_message(message)


class MessageUpdatesHandler(tornado.web.RequestHandler):
    """ Loog-polling request for new messages.
        Waits until new messages are available before returning anything.
    """
    async def post(self):
        cursor = self.get_argument("cursor", None)
        message = global_message_buffer.get_messages_since(cursor)
        while not messages:
            self.wait_future = global_message_buffer.cond.wait()
            try:
                await self.wait_future
            except asyncio.CancelledError:
                return
            message = global_message_buffer.get_messages_since(cursor)
        if self.request.connection.stream.closed():
            return
        self.write(dict(messages=messages))
    
    def on_connection_close(self):
        self.wait_future.cancel()


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/",MainHandler),
            (r"/a/message/new",MessageNewhandler),
            (r"/a/message/updates",MessageUpdatesHandler)
        ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__),"templates"),
        static_path=os.path.join(os.path.dirname(__file__),"static") ,
        xsrf_cookies=True,
        debug=options.debug
    ) 
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()