# Get-Easyaid Server

Flask API server for generating personalized financial aid requests for Coursera courses.

## Key Features

- **Smart Caching System**: Scraped course pages are cached in `static/scraps/` directory to avoid redundant web scraping and improve response times
- **AI-Powered Generation**: Uses Google Generative AI to generate personalized financial aid requests
- **Course Scraping**: Automatically scrapes Coursera course pages to extract course information and specialization details
- **MongoDB Integration**: Stores and retrieves course data from MongoDB Atlas
- **Response Regeneration**: Allows regenerating financial aid requests with the same context

## API Endpoints

- `GET /` - Health check endpoint
- `GET /getAllCourses` - Retrieve all courses from database
- `POST /submit` - Submit course information and scrape course page
- `POST /GetPrompt` - Generate personalized financial aid request prompts
- `POST /regenerate` - Regenerate a financial aid request

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with:
   ```
   MONGO_PASS=your_mongodb_password
   OPENAI_KEY=your_google_genai_api_key
   OPENAI_KEY2=your_secondary_api_key (Use the same key; key2 is backup)
   ```

3. Run the application:
   ```bash
   flask run
   ```

## Live Server

<!-- Add your live server URL here -->
API Server: [Visit server here](https://get-easyaid-server.onrender.com)
