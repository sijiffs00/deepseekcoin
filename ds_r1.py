import os
from openai import OpenAI

# DeepSeek API 클라이언트 설정하기
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 환경변수에서 API 키 가져오기
    base_url="https://api.deepseek.com"  # DeepSeek 서버 주소
)

def ask_question(question):
    # 대화 메시지 만들기
    messages = [
        {"role": "user", "content": question}
    ]
    
    # API 호출해서 답변 받아오기
    try:
        response = client.chat.completions.create(
            model="deepseek-reasoner",  # DeepSeek의 추론 모델 사용
            messages=messages
        )
        
        # 모델의 생각 과정과 최종 답변 가져오기
        reasoning = response.choices[0].message.reasoning_content
        answer = response.choices[0].message.content
        
        print("🤔 모델의 생각 과정:")
        print(reasoning)
        print("\n✨ 최종 답변:")
        print(answer)
        
    except Exception as e:
        print(f"오류가 발생했어요: {str(e)}")

# 테스트로 질문해보기
if __name__ == "__main__":
    question = "나는 숙박업을 운영하고있어. 다음은 한국인 손님이 작성한 후기야. 이 후기내용에 대해 해석해줘.\n위치 가격대비 좋습니다 주변 조용합니다 숙소바로 앞에 24시간마트와 로손있고 한블록 건너면 패밀리마트있습니다 캐널시티까진 걸어서 15분 돈키호테 20분 하카타역 10분걸립니다 가격대비 위치좋다고 생각합니다 다만\n깟뻬뜨랑 리뿔이 뜨럽거 므리커럭이 케쇽 냐와쇼 우뤼가 청쇼섀료다혀뚜여\n빡퀴뽈 래섀킈들이 케쇽 냐와서 븅냠... 뱌닼이랑 대 샤이 툼섀로 긔섀끼둘\n둘락냘략 겨료여 그트믏 막으셋욧"
    ask_question(question)
