from mastodon import Mastodon, StreamListener
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

domain = "itabashi.0j0.jp"
url = "https://{0}".format(domain)
token = open("./data/access_token", "r")
mail = open("./data/mail_address.txt", "r")
passwd = open("./data/password.txt", "r")

logger.debug(mail.read())
logger.debug(passwd.read())
logger.debug(token.read())
logger.debug(url)

mastodon = Mastodon(
    access_token = token,
    api_base_url = url
    )

mastodon.log_in(
username = mail,
password = passwd,
scopes=['read', 'write'],
)

#class MaStreamListener(StreamListener):
#  def on_update(self, status):
#    logger.debug(status.content)
#  def on_notification(self, notification):
#    logger.debug(notification)
#  def on_delete(self, status_id):
#    logger.debug(status_id)

#mastodon.stream_user(MaStreamListener())

mastodon.toot("""にゃーん""")