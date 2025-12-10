# Get-Easyaid Server

Flask API server for Get-Easyaid application.

## Deployment on Render

This application is configured for deployment on Render.

### Environment Variables

Make sure to set the following environment variables in your Render dashboard:

- `MONGO_PASS`: MongoDB Atlas password
- `OPENAI_KEY`: Google Generative AI API key
- `PORT`: Automatically set by Render (no need to configure)

### Deployment Steps

1. Push your code to GitHub
2. Connect your repository to Render
3. Render will automatically detect the `render.yaml` configuration
4. Set the environment variables (`MONGO_PASS` and `OPENAI_KEY`) in the Render dashboard
5. Deploy!

The application will be available at `https://your-service-name.onrender.com`

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with:
   ```
   MONGO_PASS=your_mongodb_password
   OPENAI_KEY=your_google_genai_api_key
   ```

3. Run the application:
   ```bash
   python app.py
   ```

Or using gunicorn:
```bash
gunicorn app:app
```

