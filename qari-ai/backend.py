from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "QariAI API is running"}

@app.get("/api/surahs")
async def get_surahs():
    return {
        "surahs": [
            {"id": 1, "name": "Al-Fatiha", "name_arabic": "الفاتحة"}
        ]
    }

@app.get("/api/surah/{surah_id}")
async def get_surah(surah_id: int):
    return {
        "surah": {
            "id": 1,
            "name": "Al-Fatiha",
            "ayahs": [
                {
                    "number": 1,
                    "words": ["بِسْمِ", "اللَّهِ", "الرَّحْمَٰنِ", "الرَّحِيمِ"],
                    "translation_ur": "اللہ کے نام سے جو بے حد مہربان، نہایت رحم والا ہے",
                    "translation_en": "In the name of Allah, the Most Gracious, the Most Merciful"
                },
                {
                    "number": 2,
                    "words": ["الْحَمْدُ", "لِلَّهِ", "رَبِّ", "الْعَالَمِينَ"],
                    "translation_ur": "سب تعریف اللہ کے لیے ہے جو تمام جہانوں کا رب ہے",
                    "translation_en": "All praise is due to Allah, Lord of the worlds"
                },
                {
                    "number": 3,
                    "words": ["الرَّحْمَٰنِ", "الرَّحِيمِ"],
                    "translation_ur": "بے حد مہربان، نہایت رحم والا",
                    "translation_en": "The Most Gracious, the Most Merciful"
                },
                {
                    "number": 4,
                    "words": ["مَالِكِ", "يَوْمِ", "الدِّينِ"],
                    "translation_ur": "انصاف کے دن کا مالک",
                    "translation_en": "Master of the Day of Judgment"
                }
            ]
        }
    }

@app.post("/api/check_recitation")
async def check_recitation(
    audio: UploadFile = File(...),
    surah_id: int = 1,
    ayah_num: int = 1,
    word_index: int = 0
):
    # Simulate AI checking (70% correct rate for demo)
    is_correct = random.random() > 0.3
    
    return {
        "is_correct": is_correct,
        "similarity": 0.9 if is_correct else 0.5,
        "errors": [] if is_correct else ["pronunciation"],
        "feedback": "Excellent!" if is_correct else "Please repeat this word correctly"
    }

if __name__ == "__main__":
    print("🚀 Starting QariAI Backend Server...")
    print("📍 Server running at: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)