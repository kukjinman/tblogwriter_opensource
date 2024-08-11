from crawlingManager import runCrawlingManager
from gptManager import requestGptAPI
from tblogManager import runtblogManager, writeContentByGptResult, bodystyling_update, publish_newpost

# 1) TistoryBlog의 로그인 구현
runtblogManager()
# 2) techCrunch사이트 webCrawling 구현
contents_crawling_result = runCrawlingManager()
print(contents_crawling_result)

# 3) crawling한 결과를 gptapi에 입력 후 요청
gpt_result = requestGptAPI(contents_crawling_result)
# print("main gpt result : ", gpt_result)

# 4) gpt결과를 read해서 블로그의 제목과 본문을 입력해줍니다.
writeContentByGptResult(gpt_result)


# 5) 본문 스타일링 조작 구현
bodystyling_update()


# 6) 완성글 발행 조작 구현
publish_newpost()


