import { useState, useRef, useEffect } from "react";
import "./ChatbotPanel.css";
import { sendMessage } from "../../services/api";

function ChatbotPanel() {
  const [open, setOpen] = useState(false);
  const INITIAL_MESSAGES = [
  {
    sender: "bot",
    text:
      "👋 Welcome!\n\nI'm your Inventory AI Assistant.\n\nYou can ask questions like:\n\n• Which products are high risk?\n• Show items that need urgent reorder.\n• Summarize today's inventory.\n• Which supplier has the longest lead time?"
  }
];
  const [messages, setMessages] = useState(INITIAL_MESSAGES);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const bottomRef = useRef(null);

  useEffect(() => {

      bottomRef.current?.scrollIntoView({

        behavior:"smooth"

      });

    }, [messages]);

    const handleClearChat = () => {

      setMessages(INITIAL_MESSAGES);

      setInput("");

      setError("");

      setLoading(false);

    };

  const handleSend = async () => {

    const question = input.trim();

    if (!question) return;

    const userMessage = {

        sender: "user",

        text: question

    };

    setMessages((prev) => [

        ...prev,

        userMessage

    ]);

    setInput("");

    try {
        setLoading(true);
        setError("");
        const response = await sendMessage(question);
        const botMessage = {

            sender: "bot",

            text: response.answer

        };

        setMessages((prev) => [

            ...prev,

            botMessage

        ]);
        setLoading(false);

    }

    catch (error) {

        console.error(error);
        const message =

          error.response?.data?.detail ||

           "Unable to contact AI assistant.";

        setError(message);

        setMessages((prev) => [

            ...prev,

            {

                sender: "bot",

                text: message

            }

        ]);
        setLoading(false);

    }

  };


  return (
    <>
      <button
        className="chat-toggle"
        onClick={() => setOpen(!open)}
      >
        🤖
      </button>

      {open && (
        <div className="chat-window">

          <div className="chat-header">

    <span>
        AI Inventory Assistant
    </span>

    <button
        className="clear-chat-btn"
        onClick={handleClearChat}
    >
        Clear
    </button>

</div>
          

          <div className="chat-body">
            {loading && (

    <div className="message-row bot">

        <div className="message-bubble bot">

            Thinking...

        </div>

    </div>

)}

        {messages.map((msg, index) => (

          <div
          key={index}
          className={`message-row ${msg.sender}`}
          >
        <div
        className={`message-bubble ${msg.sender}`}
         >
        {msg.text}
         </div>

</div>
        ))}
        <div ref={bottomRef}></div>

      </div>

      <div className="chat-input">
       <input
       disabled={loading}

    type="text"

    placeholder="Ask about your inventory..."

    value={input}

    onChange={(e) =>
        setInput(e.target.value)
    }

    onKeyDown={(e) => {

        if (e.key === "Enter") {

            handleSend();

        }

    }}

 />

     <button
      onClick={handleSend}
      disabled={loading}
      >

       {loading ? "Thinking..." : "Send"}

      </button>
      </div>
  

        </div>
      )}
    </>
  );
}

export default ChatbotPanel;