# MemoSynth - Chatbot with Contextual Memory

![MemoSynth Logo](https://via.placeholder.com/1200x400?text=MemoSynth)

MemoSynth is an intelligent chatbot application with memory capabilities, allowing for contextual and meaningful conversations. Built with FastAPI, React, Supabase PostgreSQL, and Groq LLM integration, this application maintains conversation history to provide personalized responses.

## Features

- **Contextual Memory**: The chatbot remembers previous conversations and uses them for context in responses
- **Multiple Conversations**: Users can manage multiple conversation threads
- **Modern UI**: Clean, responsive interface built with React
- **Powerful Backend**: FastAPI provides fast, asynchronous API endpoints
- **Supabase Integration**: Cloud PostgreSQL database with real-time capabilities
- **LLM Integration**: Leverages Groq's language models for intelligent responses

## Tech Stack

- **Frontend**: React.js with modern JavaScript
- **Backend**: FastAPI (Python)
- **Database**: Supabase PostgreSQL
- **AI Integration**: Groq API
- **Deployment**: Vercel

## Project Structure

```
memosynth/
├── backend/                  # FastAPI Backend
│   ├── app.py               # Main FastAPI application
│   ├── models.py            # Database models for Supabase
│   ├── config.py            # Configuration with Supabase settings
│   ├── database.py          # Database connection to Supabase
│   ├── services/            # Services folder
│   │   ├── __init__.py
│   │   ├── chat_service.py  # Chat processing logic
│   │   ├── supabase_service.py # Supabase API integration
│   │   └── groq_service.py  # Groq API integration
│   └── requirements.txt     # Python dependencies
├── frontend/                # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API services with Supabase integration
│   │   │   ├── api.js       # API interaction functions
│   │   │   └── supabase.js  # Supabase client setup
│   │   └── styles/          # CSS/SCSS styles
│   ├── package.json         # With Supabase dependencies
│   └── .env                 # Frontend environment variables
└── README.md                # Project documentation
```

## Getting Started

### Prerequisites

- Node.js (v16+)
- Python (v3.9+)
- Supabase account (free tier works for development)

### Setting up Supabase

1. Create a new project on [Supabase](https://supabase.com/)
2. Navigate to the SQL Editor in your Supabase dashboard
3. Run the SQL setup script provided in the `supabase-sql.sql` file
4. Note your Supabase URL and anon/public key from the API settings

### Environment Variables

#### Backend (`.env` in `backend/` directory)
```
DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres
SUPABASE_URL=https://[YOUR-PROJECT-REF].supabase.co
SUPABASE_KEY=[YOUR-SUPABASE-ANON-KEY]
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL_NAME=llama3-70b-8192
```

#### Frontend (`.env` in `frontend/` directory)
```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_SUPABASE_URL=https://[YOUR-PROJECT-REF].supabase.co
REACT_APP_SUPABASE_ANON_KEY=[YOUR-SUPABASE-ANON-KEY]
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MemoSynth.git
   cd MemoSynth
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

1. **Start the Backend Server**
   ```bash
   cd backend
   python app.py
   ```
   The API will be available at http://localhost:8000

2. **Start the Frontend Development Server**
   ```bash
   cd frontend
   npm start
   ```
   The application will be available at http://localhost:3000

## Deployment

### Deploying to Vercel

1. **Backend Deployment**
   - Connect your GitHub repository to Vercel
   - Set up the following environment variables in Vercel:
     - `DATABASE_URL`
     - `SUPABASE_URL`
     - `SUPABASE_KEY`
     - `GROQ_API_KEY`
     - `GROQ_MODEL_NAME`

2. **Frontend Deployment**
   - Connect your GitHub repository to Vercel
   - Set up the following environment variables in Vercel:
     - `REACT_APP_API_URL` (pointing to your deployed backend URL)
     - `REACT_APP_SUPABASE_URL`
     - `REACT_APP_SUPABASE_ANON_KEY`

## Supabase Features Used

- **PostgreSQL Database**: For storing chat messages and conversation history
- **Row-Level Security (RLS)**: For securing user data
- **SQL Functions**: Custom functions for conversation retrieval
- **Real-time Subscriptions**: For instant message updates (optional)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/api/chat` | POST | Send a message and get a response |
| `/api/conversations/{user_id}` | GET | Get all conversations for a user |
| `/api/conversation/{conversation_id}` | GET | Get messages in a conversation |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Supabase](https://supabase.com) for the PostgreSQL database and real-time features
- [Groq](https://groq.com) for their powerful language models
- [FastAPI](https://fastapi.tiangolo.com/) for the efficient backend framework
- [React](https://reactjs.org/) for the frontend library

---

Developed with ❤️ by [Your Name]