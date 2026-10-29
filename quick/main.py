"""
main.py
Google Cloud Run 배포를 위한 FastAPI 백엔드 서버
셸 정렬, 퀵 정렬, 병합 정렬의 상태 스냅샷 히스토리를 생성하여 반환합니다.
"""

import os
import random
from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models import SortRequest, SortResponse
from algorithms import run_shell_sort, run_quick_sort, run_merge_sort

# 1. FastAPI 애플리케이션 초기화
app = FastAPI(
    title="Sort Visualization Backend API",
    description="셸 정렬, 퀵 정렬, 병합 정렬의 단계별 스냅샷 데이터를 제공하는 Cloud Run 백엔드",
    version="1.0.0"
)

# 2. CORS(Cross-Origin Resource Sharing) 설정
# 구글 앱스 스크립트(GAS) 및 모든 웹 클라이언트 브라우저에서 원활히 호출할 수 있도록 전체 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
