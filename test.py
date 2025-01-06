from openai import OpenAI
import os  # 환경 변수를 불러오기 위해 추가

# DeepSeek API 클라이언트 설정
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')  # 환경 변수에서 API 키 가져오기

if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY 환경 변수가 설정되지 않았습니다.")

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek(prompt):
    try:
        # API 요청 생성
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        
        # 응답 반환
        return response.choices[0].message.content
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

# 사용 예시
if __name__ == "__main__":
    print("DeepSeek 챗봇과 대화를 시작합니다. 종료하려면 'quit' 또는 'exit'를 입력하세요.")
    while True:
        user_input = input("사용자: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        response = chat_with_deepseek(user_input)
        print("DeepSeek:", response)
