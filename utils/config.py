import os
import dotenv

# Load environment variables
dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise ValueError("❌ Missing Discord Bot Token in environment variables.")
