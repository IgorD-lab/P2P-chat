# P2P-chat

This project implements a basic decentralized chat application that allows users to communicate directly with each other on the same local network (localhost).

**Requirements:**

- Python 3
- `pip` (Python package manager)

**Installation:**

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/simple-p2p-chat.git
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate.bat
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

**Running the Application:**

1. **Start the Server:**

   ```bash
   python server.py
   ```

2. **Start Clients:**

   Open separate terminal windows and run `python client.py` in each. You will be prompted to:

   - Enter the server's host ('127.0.0.1' by default).
   - Choose a port of the client you wish to connect to (manually specify port visible in other clients window).  
    ![image](https://github.com/IgorD-lab/P2P-chat/assets/74680803/84b0ef2b-cc4d-43b7-8366-229cbdd886d0)  

   **Note:**

   - The "Choose a client from these" message displays only pre existing clients. You can still connect to newer clients by entering their port.
  
3. **Stop the server:**

   - Once all of the clients are connected you can stop the server (clients dont need server to communicate only to connect)

4. **Chat:**

   - Type messages in any client window, and they will be broadcast to all connected clients even without a running server.


**Alternative Implementation (Optional):**

This project uses Twisted for network communication. If you prefer, you can explore using `asyncio` protocols for a similar approach.

**Future Enhancements (Open an issue if you wish for these functionalities to be implemented):**

- Explore implementing file transfer functionalities.
- Consider expanding to a distributed network architecture for broader usability beyond localhost.
- Voice chat

**Contributions:**

I welcome your contributions to this project! Feel free to fork the repository, make improvements, and create pull requests.
