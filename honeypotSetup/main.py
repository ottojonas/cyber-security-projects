import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="cmd_audits.log",
    encoding="utf-8",
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
)

user_name_capture = str(input("prompt: "))

password_capture = str(input("prompt: "))
