# Esad Kaya

Fourth-year Computer Science student at the University of Ottawa focused on AI-driven systems, embedded hardware, and full-stack product development. I like building things that run efficiently on the edge and scale cleanly in the cloud.

## What I Do
- Edge AI and computer vision on Orange Pi 5 (RK3588S NPU) with quantized YOLO/NanoDet/MobileNet models, ONNX Runtime, RKNN Toolkit, and OpenCV.
- Embedded and IoT nodes on ESP32-S3 with mmWave radar, accelerometer (LIS3DH), LTE Cat-1/Cat-4 modems, GPS (u-blox NEO-8M), and camera modules; low-power wake-on-interrupt orchestration.
- Backend and platforms with NestJS (Node/TypeScript), GraphQL (Apollo), PostgreSQL + PostGIS, Redis, Docker, Linux, and REST/gRPC APIs.
- Frontend and applications with React Native (Expo), React Admin, and Streamlit for dashboards and mobile experiences.
- Data/RAG pipelines in Python with ChromaDB, Sentence Transformers, LiteLLM/OpenAI-compatible APIs, Hugging Face Transformers, and PyTorch.
- Comfortable with Git/GitHub, CI basics, Armbian/Linux SBC tuning, and performance/power profiling.

## Selected Projects
- **[Smart Vehicle Sentinel & Enforcement Detection System](https://github.com/Integer-Conversion-Error/Park-Opticon)** - Designed an AI-powered, low-power vehicle sentinel using edge inference on Orange Pi 5 and a mesh of ESP32-S3 nodes with mmWave radar and camera buffers. Built a two-stage detection pipeline (edge YOLOv5n/NanoDet plus cloud YOLOv8-L/ViT) to classify enforcement vehicles with sub-0.1% false negatives, under a 50 Wh per 12-hour power budget via suspend-to-RAM, wake-on-GPIO, and selective inference. Integrated LTE (SIMCom A7670/7600), GPS, distributed sensor fusion, and structured event logging for real-time situational awareness.
- **[AutoScraper (Vehicle Search Automation)](https://github.com/Integer-Conversion-Error/AutoScraper)** - Flask and Bootstrap web app that automates detailed vehicle searches on AutoTrader.ca. Supports saved payloads in Firebase Firestore, auth via Firebase Authentication, keyword inclusion/exclusion filters, concurrent scraping with requests/BeautifulSoup and concurrent.futures, CSV export, batch link opening, and proxy-configurable runs. Adds AI analysis powered by Google Gemini and Custom Search with exchange-rate awareness to rate reliability, pricing, and negotiation angles for each listing, with logging and retry/backoff for robustness.
- **[Note Intelligence (RAG for personal knowledge)](https://github.com/Integer-Conversion-Error/note-splicer)** - Retrieval-augmented generation workflow that converts unstructured notes to structured JSON, builds a persistent ChromaDB vector index with sentence transformers, and answers queries via LLMs (Gemini, Deepseek) through LiteLLM. Includes note extraction, JSON splicing, semantic search, and a Streamlit UI for interactive querying. Stack: Python, ChromaDB, Sentence Transformers, PyTorch, Hugging Face, Transformers.

## Skills Snapshot
- Languages: Python, TypeScript/JavaScript, C++, Java, SQL
- AI/ML: PyTorch, TensorFlow, ONNX Runtime, RKNN Toolkit, YOLOv5/8, NanoDet, MobileNet, OpenCV, LoRA fine-tuning, RAG pipelines
- Backend/Data: NestJS, GraphQL (Apollo), REST/gRPC, PostgreSQL + PostGIS, Redis, Docker, Linux, Armbian, CI/CD fundamentals
- Frontend/Apps: React Native (Expo), React Admin, Streamlit
- Hardware/IoT: Orange Pi 5, ESP32-S3, mmWave radar, LIS3DH accelerometers, LTE Cat-1/Cat-4 modems, GPS, microSD/rolling buffers, ESP-NOW/Wi-Fi mesh

## GitHub Stats
![Esad's GitHub stats](https://github-readme-stats.vercel.app/api?username=Integer-Conversion-Error&show_icons=true&theme=dark)
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=Integer-Conversion-Error&theme=dark)
![GitHub Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Integer-Conversion-Error&theme=github-dark)

## Connect
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/esad-kaya-28b400215/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Website-orange)](https://github.com/Integer-Conversion-Error)

Always open to collaborations or discussing interesting problems.
