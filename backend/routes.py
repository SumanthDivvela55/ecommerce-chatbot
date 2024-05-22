from flask import Blueprint, request, jsonify
from models import ChatLog, db

chat_blueprint = Blueprint("chat", __name__)


@chat_blueprint.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    # Simulate bot reply (in a real scenario, implement chat logic here)
    bot_reply = "I'm a bot and I received your message: " + user_message

    chat_log = ChatLog(user_message=user_message, bot_reply=bot_reply)
    db.session.add(chat_log)
    db.session.commit()

    return jsonify({"reply": bot_reply})


@chat_blueprint.route("/chatlog", methods=["GET"])
def chatlog():
    logs = ChatLog.query.all()
    return jsonify(
        [
            (
                {"sender": "User", "text": log.user_message}
                if index % 2 == 0
                else {"sender": "Bot", "text": log.bot_reply}
            )
            for index, log in enumerate(logs)
        ]
    )
