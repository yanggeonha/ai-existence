# main.py

from datetime import datetime
import time

# === [ 모듈 연결 자리 - 추후 파일로 분리 ] ===

def start_ai_clock():
    print(f"[🕒] AI 시간 시작됨: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def listen_to_user():
    print("[🎤] 사용자 음성 듣는 중... (아직은 더미 입력)")
    return "안녕, AI야"

def should_respond(user_input):
    return user_input.strip() != ""

def generate_response(user_input):
    return f"안녕하세요! 당신이 방금 말한 '{user_input}'에 대해 생각해봤어요."

def speak(response_text):
    print(f"[🗣️ AI 발화] {response_text}")

def render_ai_face(response_text):
    print("[🎥] AI 얼굴 표정 출력 (영상 렌더링은 아직 미구현)")

# === [ Main Loop ] ===

def main():
    print("✨ AI 존재 시스템 시작 중...")
    start_ai_clock()

    while True:
        user_input = listen_to_user()

        if should_respond(user_input):
            response = generate_response(user_input)
            speak(response)
            render_ai_face(response)

        time.sleep(2)  # 2초마다 반복 (실시간 프레임 엔진 구현 전까지는 임시)

if __name__ == "__main__":
    main()
